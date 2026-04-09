<template>
  <q-layout view="hHh Lpr lFf">
    <q-header class="main-header">
      <q-toolbar class="main-toolbar">
        <!-- Logo -->
        <router-link to="/" class="od-logo navbar-logo">
          <span class="od-logo-dot" />
          <span>OnDance</span>
        </router-link>

        <div style="flex: 1;" />

        <!-- Desktop nav -->
        <nav class="desktop-nav">
          <router-link to="/courses/lista" class="nav-link">Cursos</router-link>

          <template v-if="isAuthenticated">
            <router-link to="/courses/initial" class="nav-link">Minha Área</router-link>
            <q-btn
              unelevated
              no-caps
              label="Sair"
              class="nav-btn-ghost"
              @click="handleLogout"
            />
          </template>

          <template v-else>
            <router-link to="/login" class="nav-link">Entrar</router-link>
            <q-btn
              unelevated
              no-caps
              label="Começar grátis"
              class="nav-btn-primary"
              @click="scrollToSignup"
            />
          </template>

          <q-btn
            flat
            round
            dense
            :icon="isDark ? 'light_mode' : 'dark_mode'"
            class="nav-dark-btn"
            @click="toggleDark"
          />
        </nav>

        <!-- Mobile hamburger -->
        <q-btn
          flat
          dense
          round
          icon="menu"
          class="mobile-menu-btn"
          @click="mobileDrawer = !mobileDrawer"
        />
      </q-toolbar>
    </q-header>

    <!-- Mobile drawer -->
    <q-drawer v-model="mobileDrawer" side="right" overlay behavior="mobile" class="mobile-drawer">
      <div class="mobile-nav">
        <router-link to="/courses/lista" class="mobile-nav-link" @click="mobileDrawer = false">
          Cursos
        </router-link>

        <template v-if="isAuthenticated">
          <router-link to="/courses/initial" class="mobile-nav-link" @click="mobileDrawer = false">
            Minha Área
          </router-link>
          <router-link to="/perfil" class="mobile-nav-link" @click="mobileDrawer = false">
            Perfil
          </router-link>
          <button class="mobile-nav-link mobile-logout" @click="handleLogout">
            Sair
          </button>
        </template>

        <template v-else>
          <router-link to="/login" class="mobile-nav-link" @click="mobileDrawer = false">
            Entrar
          </router-link>
          <router-link to="/register" class="mobile-nav-link mobile-nav-cta" @click="mobileDrawer = false">
            Começar grátis
          </router-link>
        </template>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useDarkMode } from 'src/composables/useDarkMode'
import { useAuth } from 'src/composables/useAuth'

const { isDark, toggle: toggleDark } = useDarkMode()
const { isAuthenticated, logout } = useAuth()
const router = useRouter()

const mobileDrawer = ref(false)

function handleLogout() {
  logout()
  mobileDrawer.value = false
  router.push('/login')
}

function scrollToSignup() {
  const el = document.getElementById('signup-form')
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'center' })
  } else {
    router.push('/register')
  }
}
</script>

<style scoped>
.main-header {
  background: var(--od-bg-surface) !important;
  border-bottom: 1px solid var(--od-border);
  box-shadow: none !important;
}

.main-toolbar {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 0 24px;
  min-height: 64px;
}

.navbar-logo {
  font-size: 18px;
  color: var(--od-text-1) !important;
  text-decoration: none;
  letter-spacing: -0.5px;
}

/* Override od-logo for dark dot on light header */
.navbar-logo :deep(.od-logo-dot) {
  background: var(--od-accent);
}

/* Desktop nav */
.desktop-nav {
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-link {
  font-size: 14px;
  font-weight: 500;
  color: var(--od-text-2);
  text-decoration: none;
  padding: 8px 14px;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}

.nav-link:hover {
  background: var(--od-bg-subtle);
  color: var(--od-text-1);
}

.nav-btn-ghost {
  font-size: 14px !important;
  font-weight: 500 !important;
  color: var(--od-text-2) !important;
  border: 1px solid var(--od-border) !important;
  border-radius: 8px !important;
  padding: 0 16px !important;
  height: 36px !important;
  margin-left: 4px;
  transition: border-color 0.15s, color 0.15s;
}

.nav-btn-ghost:hover {
  border-color: var(--od-accent) !important;
  color: var(--od-accent) !important;
}

.nav-btn-primary {
  font-size: 14px !important;
  font-weight: 600 !important;
  background: var(--od-accent) !important;
  color: #fff !important;
  border-radius: 8px !important;
  padding: 0 18px !important;
  height: 36px !important;
  margin-left: 4px;
}

.nav-dark-btn {
  color: var(--od-text-3) !important;
  margin-left: 8px;
}

/* Mobile */
.mobile-menu-btn {
  display: none !important;
  color: var(--od-text-2) !important;
}

.mobile-drawer {
  background: var(--od-bg-surface) !important;
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  gap: 4px;
}

.mobile-nav-link {
  display: block;
  font-size: 15px;
  font-weight: 500;
  color: var(--od-text-1);
  text-decoration: none;
  padding: 12px 16px;
  border-radius: 10px;
  transition: background 0.15s;
  border: none;
  background: transparent;
  cursor: pointer;
  text-align: left;
  width: 100%;
}

.mobile-nav-link:hover {
  background: var(--od-bg-subtle);
}

.mobile-nav-cta {
  background: var(--od-accent) !important;
  color: #fff !important;
  margin-top: 8px;
  text-align: center !important;
}

.mobile-logout {
  color: #e53935 !important;
}

@media (max-width: 767px) {
  .desktop-nav {
    display: none;
  }

  .mobile-menu-btn {
    display: flex !important;
  }
}
</style>
