import pytest

from user.models import City, Profile, State, User


@pytest.fixture
def state(db):
    return State.objects.create(name='São Paulo', abbreviation='SP')


@pytest.fixture
def city(state):
    return City.objects.create(name='Campinas', state=state)


@pytest.fixture
def user(db):
    return User.objects.create_user(email='usuario@teste.com', password='senha123')


@pytest.fixture
def profile(user, city):
    return Profile.objects.create(
        user=user,
        name='Usuário Teste',
        city=city,
        celular='11999999999',
    )
