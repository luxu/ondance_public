const alunoRoutes = {
  path: '/aluno',
  component: () => import('layouts/StudentLayout.vue'),
  meta: { role: 'aluno' },
  children: [
    { path: '',             redirect: '/aluno/inicio' },
    { path: 'inicio',       name: 'aluno-inicio',       component: () => import('pages/aluno/InicioPage.vue') },
    { path: 'meus-cursos',  name: 'aluno-meus-cursos',  component: () => import('pages/aluno/MeusCursosPage.vue') },
    { path: 'cursos/:id/assistir', name: 'aluno-assistir', component: () => import('pages/aluno/AssistirPage.vue') },
    { path: 'progresso',    name: 'aluno-progresso',    component: () => import('pages/aluno/ProgressoPage.vue') },
    { path: 'certificados', name: 'aluno-certificados', component: () => import('pages/aluno/CertificadosPage.vue') },
    { path: 'explorar',     name: 'aluno-explorar',     component: () => import('pages/aluno/ExplorarPage.vue') },
    { path: 'configuracoes',name: 'aluno-config',       component: () => import('pages/aluno/ConfigPage.vue') },
  ]
}

const professorRoutes = {
  path: '/professor',
  component: () => import('layouts/ProfessorLayout.vue'),
  meta: { role: 'professor' },
  children: [
    { path: '',                    redirect: '/professor/dashboard' },
    { path: 'dashboard',           name: 'prof-dashboard', component: () => import('pages/professor/DashboardPage.vue') },
    { path: 'cursos',              name: 'prof-cursos',    component: () => import('pages/professor/CursosPage.vue') },
    { path: 'cursos/novo',         name: 'prof-novo',      component: () => import('pages/courses/CourseAdd.vue') },
    { path: 'cursos/:id/editar',   name: 'prof-editar',    component: () => import('pages/professor/EditarCursoPage.vue') },
    { path: 'cursos/:id/aulas',    name: 'prof-aulas',     component: () => import('pages/professor/AulasPage.vue') },
    { path: 'alunos',              name: 'prof-alunos',    component: () => import('pages/professor/AlunosPage.vue') },
    { path: 'ganhos',              name: 'prof-ganhos',    component: () => import('pages/professor/GanhosPage.vue') },
    { path: 'config',              name: 'prof-config',    component: () => import('pages/professor/ConfigPage.vue') },
  ]
}

const adminRoutes = {
  path: '/admin',
  component: () => import('layouts/AdminLayout.vue'),
  meta: { role: 'admin' },
  children: [
    { path: '',            redirect: '/admin/overview' },
    { path: 'overview',   name: 'admin-overview',   component: () => import('pages/admin/OverviewPage.vue') },
    { path: 'cursos',     name: 'admin-cursos',     component: () => import('pages/admin/CursosPage.vue') },
    { path: 'usuarios',   name: 'admin-usuarios',   component: () => import('pages/admin/UsuariosPage.vue') },
    { path: 'analytics',  name: 'admin-analytics',  component: () => import('pages/admin/AnalyticsPage.vue') },
    { path: 'categorias', name: 'admin-categorias', component: () => import('pages/admin/CategoriasPage.vue') },
    { path: 'campanhas',  name: 'admin-campanhas',  component: () => import('pages/admin/CampanhasPage.vue') },
    { path: 'config',     name: 'admin-config',     component: () => import('pages/admin/ConfigPage.vue') },
  ]
}

const loginRoutes = {
  path: '/login',
  component: () => import('layouts/MainLayout.vue'),
  meta: { guest: true },
  children: [
    { path: '', name: 'login', component: () => import('pages/LoginPage.vue') }
  ]
}

const registerRoutes = {
  path: '/register',
  component: () => import('layouts/MainLayout.vue'),
  meta: { guest: true },
  children: [
    { path: '', name: 'register', component: () => import('pages/RegisterPage.vue') }
  ]
}

const profileRoute = {
  path: '/perfil',
  component: () => import('layouts/CoursesLayout.vue'),
  children: [
    { path: '', name: 'profile', component: () => import('pages/ProfilePage.vue') }
  ]
}

const mainRoutes = {
  path: '/',
  component: () => import('layouts/MainLayout.vue'),
  meta: { guest: true },
  children: [
    { path: '', name: 'home', component: () => import('pages/IndexPage.vue') },
  ]
}

const routes = [
  alunoRoutes,
  professorRoutes,
  adminRoutes,
  loginRoutes,
  registerRoutes,
  profileRoute,
  mainRoutes,
  { path: '/:catchAll(.*)*', name: '404', component: () => import('pages/ErrorNotFound.vue') }
]

export default routes
