# 🌐 OnDance

Plataforma digital de ensino de dança da ABCAA (Associação Beneficente e Cultural Amor em Ação), onde alunos podem acessar cursos online com professores, assistir aulas, acompanhar progresso e receber certificados.

## 📋 Sobre o projeto

O OnDance conecta alunos e professores de dança em um ambiente digital: professores publicam cursos e aulas, alunos se matriculam, acompanham seu progresso e, ao concluir, recebem certificados. A plataforma é gerenciada pela ABCAA e desenvolvida por um squad voluntário.

## 🛠️ Stack

**Backend**
- Python 3.13 + Django 6 + Django REST Framework 3.17
- Autenticação JWT (`djangorestframework-simplejwt`) + OAuth social (`django-allauth`)
- Gerenciador de pacotes: `uv` | Task runner: `taskipy`

**Frontend**
- Vue 3 + Quasar 2 (UI framework) + Vue Router 5
- HTTP client: Axios | Build: Vite (`@quasar/app-vite`)
- Gerenciador de pacotes: `yarn`

## 🚀 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/abcaa-ong/ondance.git
cd ondance
```

**Backend**
```bash
cd backend
uv sync                          # instalar dependências
cp contrib/env-sample .env       # configurar variáveis de ambiente
task migrate                     # aplicar migrações
task runserver                   # rodar em desenvolvimento (porta 8000)
```

**Frontend**
```bash
cd frontend
yarn install                     # instalar dependências
yarn dev                         # rodar em desenvolvimento (porta 9000)
```

## 📁 Estrutura de pastas

```
ondance/
├── backend/                → Backend Django
│   ├── kernel/             → Configuração Django (settings, urls, wsgi)
│   ├── user/               → App de usuários e perfis
│   ├── course/             → App de cursos, progresso e certificados
│   ├── api/                → Camada REST API (serializers, views)
│   └── contrib/            → Utilitários (env_gen.py, env-sample)
├── frontend/               → Frontend Vue 3 + Quasar
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── layouts/
│       ├── router/
│       └── services/
├── .github/
│   ├── ISSUE_TEMPLATE/     → Templates de bug report e feature request
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/          → CI: lint + testes (backend) e lint + build (frontend)
├── CONTRIBUTING.md
└── README.md
```

## 👥 Squad responsável

Time: `squad-ondance`
Líder: @luciano_martins

## 📌 Links úteis

- [Tarefas no Asana](#)
- [Figma / Protótipo](#)
- [Ambiente de homologação](#)

## 🤝 Como contribuir

Leia o [CONTRIBUTING.md](./CONTRIBUTING.md) antes de abrir um PR.
