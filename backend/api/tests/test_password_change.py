import pytest

from user.models import User

pytestmark = pytest.mark.django_db


def test_password_change_requires_auth(api_client):
    payload = {
        'old_password': 'senha1234',
        'new_password': 'senha12345',
    }
    resp = api_client.post('/api/password/change/', data=payload, format='json')

    assert resp.status_code == 401


def test_password_change_success(api_client):
    user = User.objects.create_user(email='aluno@teste.com', password='senha1234')
    api_client.force_authenticate(user=user)
    payload = {
        'old_password': 'senha1234',
        'new_password': 'novaSenha123',
    }
    resp = api_client.post('/api/password/change/', data=payload, format='json')

    assert resp.status_code == 204
    user.refresh_from_db()
    assert user.check_password('novaSenha123') is True


def test_password_change_rejects_wrong_old_password(api_client):
    user = User.objects.create_user(email='aluno@teste.com', password='senha1234')
    api_client.force_authenticate(user=user)
    payload = {
        'old_password': 'errada',
        'new_password': 'novaSenha123',
    }
    resp = api_client.post('/api/password/change/', data=payload, format='json')

    assert resp.status_code == 400
    assert 'old_password' in resp.data


def test_password_change_rejects_short_new_password(api_client):
    user = User.objects.create_user(email='aluno@teste.com', password='senha1234')
    api_client.force_authenticate(user=user)
    payload = {
        'old_password': 'senha1234',
        'new_password': '1234567',
    }
    resp = api_client.post('/api/password/change/', data=payload, format='json')

    assert resp.status_code == 400
    assert 'new_password' in resp.data
