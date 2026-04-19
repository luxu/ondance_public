import pytest

from user.models import Profile, User

pytestmark = pytest.mark.django_db

ADMIN_USERS_URL = '/api/admin/users/'


@pytest.fixture
def student(db):
    u = User.objects.create_user(email='aluno@teste.com', password='senha123')
    u.is_student = True
    u.is_teacher = False
    u.save()
    Profile.objects.create(user=u, name='Carlos Aluno')
    return u


@pytest.fixture
def professor(db):
    u = User.objects.create_user(email='professor@teste.com', password='senha123')
    u.is_teacher = True
    u.is_student = False
    u.save()
    Profile.objects.create(user=u, name='Ana Professora')
    return u


# ── Autenticação e permissão ───────────────────────────────────────────────


def test_anonimo_recebe_401(api_client):
    resp = api_client.get(ADMIN_USERS_URL)
    assert resp.status_code == 401


def test_usuario_comum_recebe_403(api_client, user):
    api_client.force_authenticate(user=user)
    resp = api_client.get(ADMIN_USERS_URL)
    assert resp.status_code == 403


def test_professor_recebe_403(api_client, teacher):
    api_client.force_authenticate(user=teacher)
    resp = api_client.get(ADMIN_USERS_URL)
    assert resp.status_code == 403


def test_admin_recebe_200(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    assert resp.status_code == 200


# ── Estrutura da resposta ──────────────────────────────────────────────────


def test_retorna_campos_corretos(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    usuario = resp.json()['results'][0]
    assert set(usuario.keys()) == {'email', 'name', 'photo', 'role', 'city_detail'}


def test_retorna_email_do_usuario(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    emails = [u['email'] for u in resp.json()['results']]
    assert student.email in emails


def test_retorna_role_aluno(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    usuario = next(u for u in resp.json()['results'] if u['email'] == student.email)
    assert usuario['role'] == 'aluno'


def test_retorna_role_professor(api_client, admin_user, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    usuario = next(u for u in resp.json()['results'] if u['email'] == professor.email)
    assert usuario['role'] == 'professor'


def test_city_detail_e_none_sem_cidade(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    usuario = next(u for u in resp.json()['results'] if u['email'] == student.email)
    assert usuario['city_detail'] is None


def test_city_detail_contem_nome_e_estado(api_client, admin_user, city):
    u = User.objects.create_user(email='comcidade@teste.com', password='senha123')
    Profile.objects.create(user=u, name='Com Cidade', city=city)
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    usuario = next(u for u in resp.json()['results'] if u['email'] == 'comcidade@teste.com')
    assert usuario['city_detail']['name'] == city.name
    assert usuario['city_detail']['state'] == 'SP'


# ── Ordenação ──────────────────────────────────────────────────────────────


def test_lista_em_ordem_alfabetica_por_nome(api_client, admin_user, student, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    nomes = [u['name'] for u in resp.json()['results'] if u['name']]
    assert nomes == sorted(nomes)


# ── Filtro por role ────────────────────────────────────────────────────────


def test_filtra_por_role_aluno(api_client, admin_user, student, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'role': 'aluno'})
    roles = [u['role'] for u in resp.json()['results']]
    assert all(r == 'aluno' for r in roles)
    emails = [u['email'] for u in resp.json()['results']]
    assert student.email in emails
    assert professor.email not in emails


def test_filtra_por_role_professor(api_client, admin_user, student, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'role': 'professor'})
    roles = [u['role'] for u in resp.json()['results']]
    assert all(r == 'professor' for r in roles)
    emails = [u['email'] for u in resp.json()['results']]
    assert professor.email in emails
    assert student.email not in emails


def test_sem_filtro_retorna_todos(api_client, admin_user, student, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL)
    emails = [u['email'] for u in resp.json()['results']]
    assert student.email in emails
    assert professor.email in emails


# ── Busca ──────────────────────────────────────────────────────────────────


def test_busca_por_nome(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'search': 'Carlos'})
    emails = [u['email'] for u in resp.json()['results']]
    assert student.email in emails


def test_busca_por_email(api_client, admin_user, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'search': 'professor@'})
    emails = [u['email'] for u in resp.json()['results']]
    assert professor.email in emails


def test_busca_case_insensitive(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'search': 'carlos'})
    emails = [u['email'] for u in resp.json()['results']]
    assert student.email in emails


def test_busca_sem_resultado_retorna_vazio(api_client, admin_user, student):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'search': 'xyz_inexistente'})
    assert resp.json()['results'] == []


def test_busca_com_filtro_de_role(api_client, admin_user, student, professor):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.get(ADMIN_USERS_URL, {'role': 'aluno', 'search': 'Carlos'})
    emails = [u['email'] for u in resp.json()['results']]
    assert student.email in emails
    assert professor.email not in emails
