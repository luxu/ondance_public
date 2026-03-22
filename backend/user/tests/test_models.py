import pytest
from django.db.models import ProtectedError

from user.models import City, Profile, State, User

pytestmark = pytest.mark.django_db


def test_cria_usuario_com_email_e_senha():
    user = User.objects.create_user(email='novo@teste.com', password='senha123')
    assert user.email == 'novo@teste.com'
    assert user.check_password('senha123')


def test_levanta_erro_ao_criar_usuario_sem_email():
    with pytest.raises(ValueError):
        User.objects.create_user(email='', password='senha123')


def test_normaliza_email_ao_criar_usuario():
    user = User.objects.create_user(email='Teste@TESTE.COM', password='senha123')
    assert user.email == 'Teste@teste.com'


def test_superuser_tem_is_staff_e_is_superuser():
    user = User.objects.create_superuser(email='admin@teste.com', password='senha123')
    assert user.is_staff is True
    assert user.is_superuser is True


def test_str_user_retorna_email(user):
    assert str(user) == 'usuario@teste.com'


def test_novo_usuario_tem_defaults_corretos(user):
    assert user.is_student is True
    assert user.is_teacher is False
    assert user.is_active is True
    assert user.is_staff is False


def test_email_duplicado_levanta_erro(user):
    with pytest.raises(Exception):
        User.objects.create_user(email='usuario@teste.com', password='outrasenha')


def test_str_state_retorna_nome_e_sigla(state):
    assert str(state) == 'São Paulo (SP)'


def test_sigla_de_state_duplicada_levanta_erro(state):
    with pytest.raises(Exception):
        State.objects.create(name='Outro Estado', abbreviation='SP')


def test_str_city_retorna_nome_traco_sigla_estado(city):
    assert str(city) == 'Campinas - SP'


def test_deletar_estado_deleta_cidades_em_cascata(city, state):
    state.delete()
    assert City.objects.count() == 0


def test_str_profile_retorna_perfil_de_nome(profile):
    assert str(profile) == 'Perfil de Usuário Teste'


def test_profile_referencia_user_correto(profile, user):
    assert profile.user == user


def test_deletar_user_deleta_profile_em_cascata(profile, user):
    user.delete()
    assert Profile.objects.count() == 0


def test_deletar_city_com_profile_levanta_protected_error(profile, city):
    with pytest.raises(ProtectedError):
        city.delete()
