import pytest

from course.models import Course
from user.models import User

pytestmark = pytest.mark.django_db


@pytest.fixture
def teacher():
    return User.objects.create_user(email='teacher@teste.com', password='senha123')


@pytest.fixture
def courses(teacher):
    Course.objects.create(title='Ballet Clássico', teacher=teacher)
    Course.objects.create(title='Jazz Avançado', teacher=teacher)


def test_lista_courses_retorna_200(api_client, courses):
    resp = api_client.get('/api/courses/')
    assert resp.status_code == 200


def test_lista_courses_retorna_campos_corretos(api_client, courses):
    resp = api_client.get('/api/courses/')
    primeiro = resp.json()['results'][0]
    assert set(primeiro.keys()) == {
        'id',
        'title',
        'teacher',
        'is_published',
        'status',
    }


def test_lista_courses_em_ordem_alfabetica(api_client, courses):
    resp = api_client.get('/api/courses/')
    titulos = [c['title'] for c in resp.json()['results']]
    assert titulos == sorted(titulos)


def test_teacher_no_response_e_email(api_client, courses, teacher):
    resp = api_client.get('/api/courses/')
    assert resp.json()['results'][0]['teacher'] == teacher.email


def test_cria_course_com_defaults(api_client, teacher):
    payload = {
        'title': 'Contemporâneo',
        'teacher': teacher.email,
    }
    resp = api_client.post('/api/courses/', data=payload, format='json')
    assert resp.status_code == 201
    body = resp.json()
    assert body['title'] == 'Contemporâneo'
    assert body['teacher'] == teacher.email
    assert body['is_published'] is False
    assert body['status'] == 'PENDING'
