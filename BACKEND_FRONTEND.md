# Checklist de Alinhamento Backend ↔ Frontend

> Status atual: 2026-03-22 — UUID aplicado em todos os models.
> Marque `[x]` conforme os itens forem implementados/corrigidos.

---

## Legenda

- `[x]` Implementado e alinhado
- `[ ]` Pendente / divergente
- `[~]` Parcialmente implementado

---

## 1. Entidades e Models

### 1.1 Usuário (`User`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `id` | number | ✅ UUIDField (primary_key) | `[x]` |
| `email` | string (login) | ✅ EmailField único | `[x]` |
| `name` | string | ✅ CharField | `[x]` |
| `password` | string (write-only) | ✅ herdado de AbstractBaseUser | `[x]` |
| `role` | `'aluno' \| 'professor' \| 'admin'` | ❌ não existe — backend usa `is_teacher` / `is_student` / `is_staff` (booleanos separados) | `[ ]` |
| `is_teacher` | — | ✅ BooleanField | `[x]` |
| `is_student` | — | ✅ BooleanField | `[x]` |

### 1.2 Perfil (`Profile`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `photo` | — (implícito) | ✅ ImageField | `[x]` |
| `city` | string | ✅ FK → City | `[~]` serializer precisa achatar |
| `state` | string | ✅ via City → State | `[~]` serializer precisa achatar |
| `celular` | — | ✅ CharField | `[x]` |
| `birthday` | — | ✅ DateField | `[x]` |

### 1.3 Curso (`Course`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `id` | number | ✅ UUIDField (primary_key) | `[x]` |
| `title` | string (`name` em algumas views) | ✅ CharField | `[~]` nome do campo inconsistente entre views do frontend |
| `teacher` | string (nome) | ✅ FK → User (objeto) | `[~]` serializer precisa retornar nome |
| `status` | `'published' \| 'draft'` | ❌ backend usa `PENDING / APPROVED / REJECTED` + `is_published` | `[ ]` |
| `level` | `'Iniciante' \| 'Intermediário' \| 'Avançado'` | ❌ não existe no model | `[ ]` |
| `lessons` | number (quantidade de aulas) | ❌ não existe (sem model de Lesson) | `[ ]` |
| `modules` | number (quantidade de módulos) | ❌ não existe (sem model de Module) | `[ ]` |
| `students` | number (matriculados) | ❌ não existe diretamente (seria COUNT de UserCourse) | `[ ]` |
| `emoji` | string | ❌ não existe | `[ ]` |
| `thumbBg` | string (cor hex) | ❌ não existe | `[ ]` |
| `description` | string | ❌ não existe no model | `[ ]` |
| `duration` | string | ❌ não existe no model | `[ ]` |

### 1.4 Módulo (`Module`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `id` | number | ❌ model não existe | `[ ]` |
| `title` | string | ❌ model não existe | `[ ]` |
| `lessons` | Lesson[] | ❌ model não existe | `[ ]` |
| `courseId` | number | ❌ model não existe | `[ ]` |

### 1.5 Aula (`Lesson`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `id` | number | ❌ model não existe | `[ ]` |
| `title` | string | ❌ model não existe | `[ ]` |
| `moduleId` | number | ❌ model não existe | `[ ]` |

### 1.6 Progresso do Aluno (`UserCourse`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `courseId` | number | ✅ FK → Course | `[x]` |
| `profileId` | — | ✅ FK → Profile | `[x]` |
| `progress` | number (0–100) | ❌ não existe — backend só tem `is_completed` + datas | `[ ]` |
| `started_at` | — | ✅ DateTimeField | `[x]` |
| `completed_at` | — | ✅ DateTimeField nullable | `[x]` |
| `is_completed` | — | ✅ BooleanField | `[x]` |

### 1.7 Certificado (`Certificate`)

| Campo | Frontend espera | Backend tem | Status |
|-------|----------------|-------------|--------|
| `courseId` | number | ✅ FK → Course | `[x]` |
| `profileId` | — | ✅ FK → Profile | `[x]` |
| `issue_date` | — | ✅ DateField | `[x]` |
| `code` | — | ✅ CharField único | `[x]` |
| `file` | — | ✅ FileField | `[x]` |

---

## 2. Serializers

| Serializer | Status | Problema |
|-----------|--------|---------|
| `UserSerializer` | `[ ]` | Referencia campos inexistentes no model: `address`, `ein`, `cellphone`, `phone` — causará erro em produção |
| Serializer para `Course` | `[ ]` | Não existe |
| Serializer para `UserCourse` | `[ ]` | Não existe |
| Serializer para `Certificate` | `[ ]` | Não existe |
| Serializer para `Profile` | `[ ]` | Não existe |
| Serializer para `Module` | `[ ]` | Model não existe |
| Serializer para `Lesson` | `[ ]` | Model não existe |

---

## 3. Endpoints da API

### 3.1 Autenticação

| Método | URL esperada pelo frontend | Backend tem | Status |
|--------|--------------------------|-------------|--------|
| `POST` | `/api/auth/login/` | ❌ não implementado | `[ ]` |
| `POST` | `/api/auth/logout/` | ❌ não implementado | `[ ]` |
| `GET` | `/api/auth/me/` | ❌ não implementado | `[ ]` |
| `POST` | `/api/auth/register/` | `[~]` `/api/api/create_user/` (prefixo duplicado) | `[ ]` |

### 3.2 Usuários

| Método | URL esperada | Backend tem | Status |
|--------|-------------|-------------|--------|
| `GET` | `/api/users/` | `[~]` `/api/api/users/` (prefixo duplicado) | `[ ]` |
| `POST` | `/api/users/` | `[~]` `/api/api/create_user/` (URL diferente, prefixo duplicado) | `[ ]` |
| `GET` | `/api/users/:id/` | ❌ não implementado | `[ ]` |
| `PUT` | `/api/users/:id/` | ❌ não implementado | `[ ]` |
| `DELETE` | `/api/users/:id/` | ❌ não implementado | `[ ]` |

### 3.3 Cursos

| Método | URL esperada | Backend tem | Status |
|--------|-------------|-------------|--------|
| `GET` | `/api/courses/` | ❌ não implementado | `[ ]` |
| `POST` | `/api/courses/` | ❌ não implementado | `[ ]` |
| `GET` | `/api/courses/:id/` | ❌ não implementado | `[ ]` |
| `PUT` | `/api/courses/:id/` | ❌ não implementado | `[ ]` |
| `DELETE` | `/api/courses/:id/` | ❌ não implementado | `[ ]` |
| `PUT` | `/api/courses/:id/publish/` | ❌ não implementado | `[ ]` |

### 3.4 Módulos e Aulas

| Método | URL esperada | Backend tem | Status |
|--------|-------------|-------------|--------|
| `GET` | `/api/courses/:id/modules/` | ❌ model não existe | `[ ]` |
| `POST` | `/api/courses/:id/modules/` | ❌ model não existe | `[ ]` |
| `GET` | `/api/modules/:id/lessons/` | ❌ model não existe | `[ ]` |
| `POST` | `/api/modules/:id/lessons/` | ❌ model não existe | `[ ]` |

### 3.5 Progresso e Matrícula

| Método | URL esperada | Backend tem | Status |
|--------|-------------|-------------|--------|
| `GET` | `/api/students/courses/` | ❌ não implementado | `[ ]` |
| `POST` | `/api/students/courses/:id/enroll/` | ❌ não implementado | `[ ]` |
| `PUT` | `/api/students/courses/:id/progress/` | ❌ não implementado | `[ ]` |
| `GET` | `/api/students/certificates/` | ❌ não implementado | `[ ]` |

---

## 4. Permissões

| Permissão | Status | Problema |
|-----------|--------|---------|
| `IsTeacher` | `[ ]` | Verifica `request.user.role == 'TEACHER'`, mas o model não tem atributo `role` (tem `is_teacher: bool`) |
| `IsOnDanceAdmin` | `[ ]` | Verifica `request.user.role == 'ADMIN'`, mas o model não tem atributo `role` (tem `is_staff: bool`) |

---

## 5. Roteamento

| Problema | Status |
|---------|--------|
| Prefixo de URL duplicado: `api/urls.py` define `/api/` e já é incluído em `kernel/urls.py` com `path('api/', ...)`, resultando em `/api/api/...` | `[ ]` |

---

## 6. Bugs conhecidos no Serializer

| Arquivo | Problema | Status |
|---------|---------|--------|
| `api/serializers.py` — `UserSerializer` | Campos `address`, `ein`, `cellphone`, `phone` declarados mas não existem em `user.User` | `[ ]` |

---

## Resumo

| Área | Total | Alinhado | Pendente |
|------|-------|----------|----------|
| Campos de entidades | ~40 | ~15 | ~25 |
| Serializers | 7 | 0 | 7 |
| Endpoints | ~20 | 0 | ~20 |
| Permissões | 2 | 0 | 2 |
| Roteamento | 1 | 0 | 1 |
