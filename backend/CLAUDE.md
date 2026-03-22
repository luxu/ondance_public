# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Sobre o projeto

**OnDance** é o backend da plataforma da ABCAA para gerenciar cursos de dança: cadastro de usuários (professores e alunos), cursos, progresso e certificados. Construído com Django 6 + Django REST Framework.

## Comandos

O projeto usa `uv` como gerenciador de pacotes e `taskipy` para atalhos:

```bash
# Ambiente
uv sync                     # Instalar dependências

# Servidor
task runserver              # Rodar em desenvolvimento

# Banco de dados
task makemigrations         # Gerar migrações
task migrate                # Aplicar migrações
task createsuperuser        # Criar superusuário

# Qualidade de código
task lint                   # Verificar com ruff
task format                 # Formatar com ruff

# Testes
task test                   # Roda lint + pytest + coverage HTML
pytest -s -x -vv -k "nome_do_teste"   # Rodar um teste específico

# Utilitários
task shell_plus             # Shell interativo com modelos já importados
python contrib/env_gen.py   # Gerar arquivo .env com SECRET_KEY aleatória
```

## Configuração do ambiente

Copie `contrib/env-sample` para `.env` na raiz do backend. Variáveis obrigatórias:

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost
DATABASE_URL=postgres://postgres:postgres@localhost/postgres  # ou omitir para SQLite
```

## Arquitetura

```
backend/
├── kernel/          # Configuração Django (settings, urls raiz, wsgi/asgi)
├── user/            # App de usuários (modelo customizado, paginação)
├── course/          # App de cursos, progresso e certificados
├── api/             # Serializers, views e URLs da REST API
└── contrib/         # Utilitários de infraestrutura (env_gen.py, env-sample)
```

**Modelo de usuário customizado** (`user.User`): autenticação por e-mail (não username), com flags `is_teacher` e `is_student`. Definido em `AUTH_USER_MODEL = 'user.User'`.

**Apps e responsabilidades:**
- `user`: `User`, `Profile`, `State`, `City` — dados de identidade e localização
- `course`: `Course`, `UserCourse` (progresso), `Certificate` — fluxo de aprendizado
- `api`: camada HTTP — serializers, views genéricas do DRF e roteamento

**Permissões customizadas** (`course/permissions.py`): `IsTeacher` e `IsOnDanceAdmin` verificam `request.user.role`.

**Paginação** (`user/pagination.py`): `CustomPagination` com `page_size=25`, `max_page_size=100`, configurada globalmente no DRF.

**Testes**: usam `pytest-django` com `APIClient` do DRF. Fixtures ficam em `api/tests/conftest.py`.

## Fluxo de contribuição

**Branches**: `tipo/descricao-curta` — `feat/`, `fix/`, `docs/`, `refactor/`, `test/`

**Commits**: `tipo: descrição curta no imperativo` (ex: `feat: adiciona endpoint de certificados`)

**PRs** para `main`, referenciar sempre a Issue com `Closes #NNN`.
