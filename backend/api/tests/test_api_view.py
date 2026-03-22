import pytest
# from django.urls import reverse_lazy

from user.models import User

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return User.objects.create(
        name='luxu',
        password='2'
    )


@pytest.fixture
def cliente():
    return User.objects.create(
        name="João Vitor",
        email='teste@teste.gmail'
    )

# def test_list_cliente(client, cliente):
#     resp = client.get('/api/users/')
#     assert resp.status_code == 200
#     assert len(resp.json()['data']) == 1
#     assert resp.json()['data'][0]['name'] == 'João Vitor'

# def test_create_cliente(client, cliente):
#     resp = client.post(
#         '/api/create_user/',
#         data=cliente
#     )
#     assert resp.status_code == 200
#
