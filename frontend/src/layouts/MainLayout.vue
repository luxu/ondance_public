<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title>
          On Dance
        </q-toolbar-title>
        
        <!-- Spacer to push link to the right -->
        <div style="flex: 1;" />

        <q-btn
          flat
          round
          dense
          :icon="isDark ? 'light_mode' : 'dark_mode'"
          :aria-label="isDark ? 'Modo claro' : 'Modo escuro'"
          @click="toggleDark"
          style="color: var(--od-text-1, #333); margin-right: 12px;"
        />

        <template v-if="isAuthenticated">
          <div class="row items-center" style="gap: 12px; margin-right: 12px;">
            <q-avatar size="34px" color="primary" text-color="white">
              {{ userInitials }}
            </q-avatar>
            <div style="display: flex; flex-direction: column; justify-content: center; min-width: 0;">
              <span style="font-size: 14px; font-weight: 600; color: var(--od-text-1); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                {{ userName }}
              </span>
              <small style="font-size: 11px; color: var(--od-text-3);">
                {{ user?.email }}
              </small>
            </div>
          </div>

          <q-btn
            flat
            dense
            round
            icon="logout"
            aria-label="Logout"
            @click="handleLogout"
            style="color: var(--od-text-1, #333);"
          />
        </template>

        <template v-else>
          <router-link
            to="/register"
            style="
              color: var(--od-text-1, #333);
              text-decoration: none;
              font-size: 14px;
              font-weight: 500;
              padding: 8px 16px;
              border-radius: 4px;
              transition: all 0.3s ease;
            "
            @mouseenter="e => e.target.style.backgroundColor = 'var(--od-bg-subtle, #f5f5f5)'"
            @mouseleave="e => e.target.style.backgroundColor = 'transparent'"
          >
            Cadastro
          </router-link>
        </template>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label header>
          Menu
        </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import EssentialLink from 'components/EssentialLink.vue'
import { useDarkMode } from 'src/composables/useDarkMode'
import { useAuth } from 'src/composables/useAuth'

const { isDark, toggle: toggleDark } = useDarkMode()
const { isAuthenticated, user, logout } = useAuth()
const router = useRouter()

const userName = computed(() => {
  if (!user.value) return 'Usuario'
  return user.value.name || user.value.email || 'Usuario'
})

const userInitials = computed(() => {
  const name = user.value?.name || user.value?.email || 'U'
  const parts = name.split(' ').filter(Boolean)
  if (parts.length === 0) return 'U'
  if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase()
  return (parts[0][0] + parts[1][0]).toUpperCase()
})

function handleLogout () {
  logout()
  router.push('/login')
}

const linksList = [
  {
    title: 'Início',
    icon: 'home',
    to: '/'
  },
  {
    title: 'Aluno',
    icon: 'person',
    to: '/students'
  },
  {
    title: 'Professor',
    icon: 'school',
    to: '/professores'
  },
  {
    title: 'Cursos',
    icon: 'book',
    to: '/courses'
  },
  {
    title: 'Cidades',
    icon: 'city',
    to: '/cities'
  },
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
