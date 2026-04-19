<template>
  <q-page class="q-pa-lg">

    <!-- Header -->
    <div class="q-mb-lg">
      <div class="od-display" style="font-size: 24px; color: var(--od-text-1);">Usuários</div>
      <p style="color: var(--od-text-3); margin: 4px 0 0; font-size: 14px;">
        Gerencie alunos e professores da plataforma
      </p>
    </div>

    <!-- Filtros -->
    <div class="row items-center q-mb-md" style="gap: 8px; flex-wrap: wrap;">
      <q-btn
        v-for="tab in tabs"
        :key="tab.value"
        unelevated no-caps dense
        :label="tab.label"
        :style="activeRole === tab.value
          ? { background: 'var(--od-accent)', color: '#fff', borderRadius: '8px', fontSize: '12px', padding: '4px 14px' }
          : { background: 'var(--od-bg-subtle)', color: 'var(--od-text-3)', borderRadius: '8px', fontSize: '12px', padding: '4px 14px' }"
        @click="setRole(tab.value)"
      />
      <q-input
        v-model="search"
        outlined dense
        placeholder="Buscar por nome ou e-mail"
        style="min-width: 220px; flex: 1;"
        debounce="300"
        @update:model-value="onSearch"
      >
        <template #prepend>
          <q-icon name="search" size="16px" style="color: var(--od-text-4);" />
        </template>
        <template #append>
          <q-icon
            v-if="search"
            name="close"
            size="14px"
            style="color: var(--od-text-4); cursor: pointer;"
            @click="clearSearch"
          />
        </template>
      </q-input>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="column items-center justify-center" style="min-height: 240px; gap: 12px;">
      <q-spinner size="30px" :style="{ color: 'var(--od-accent)' }" />
      <span style="font-size: 13px; color: var(--od-text-4);">Carregando usuários...</span>
    </div>

    <!-- Lista vazia -->
    <div v-else-if="users.length === 0" class="column items-center justify-center" style="min-height: 240px; gap: 10px;">
      <q-icon name="manage_accounts" size="40px" style="color: var(--od-text-5);" />
      <p style="font-size: 14px; color: var(--od-text-4); margin: 0;">
        {{ search ? 'Nenhum usuário encontrado para esta busca' : 'Nenhum usuário cadastrado' }}
      </p>
    </div>

    <!-- Lista de usuários -->
    <q-card v-else flat bordered class="od-card">
      <div
        v-for="(u, idx) in users"
        :key="u.email"
        class="row items-center q-px-md q-py-sm"
        :style="{
          borderTop: idx > 0 ? '0.5px solid var(--od-border-light)' : 'none',
          gap: '12px',
        }"
      >
        <!-- Avatar -->
        <q-avatar size="36px" :style="{ flexShrink: 0 }">
          <img v-if="u.photo" :src="u.photo" style="object-fit: cover;" />
          <span v-else :style="{ background: avatarColor(u.email), color: '#fff', fontSize: '13px', fontWeight: 600, width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }">
            {{ initials(u) }}
          </span>
        </q-avatar>

        <!-- Nome e e-mail -->
        <div class="col" style="min-width: 0;">
          <div style="font-size: 13px; font-weight: 500; color: var(--od-text-1); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            {{ u.name || '—' }}
          </div>
          <div style="font-size: 12px; color: var(--od-text-4); margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            {{ u.email }}
          </div>
        </div>

        <!-- Cidade -->
        <div
          v-if="u.city_detail"
          style="font-size: 12px; color: var(--od-text-4); white-space: nowrap; flex-shrink: 0;"
          class="gt-sm"
        >
          {{ u.city_detail.name }}, {{ u.city_detail.state }}
        </div>

        <!-- Badge de role -->
        <q-badge
          :color="u.role === 'professor' ? 'purple' : 'blue'"
          :label="u.role === 'professor' ? 'Professor' : 'Aluno'"
          style="font-size: 10px; border-radius: 6px; padding: 3px 8px; flex-shrink: 0;"
        />
      </div>
    </q-card>

    <!-- Paginação -->
    <div v-if="totalPages > 1" class="row justify-center q-mt-md">
      <q-pagination
        v-model="page"
        :max="totalPages"
        :max-pages="5"
        boundary-numbers
        :color="'var(--od-accent)'"
        @update:model-value="loadPage"
      />
    </div>

  </q-page>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useQuasar } from 'quasar'
import { profileService } from 'src/services/profile'

const $q = useQuasar()

const loading = ref(true)
const users = ref([])
const activeRole = ref(null)
const search = ref('')
const page = ref(1)
const total = ref(0)
const pageSize = 25

const totalPages = computed(() => Math.ceil(total.value / pageSize))

const tabs = [
  { label: 'Todos',       value: null },
  { label: 'Alunos',      value: 'aluno' },
  { label: 'Professores', value: 'professor' },
]

async function load () {
  loading.value = true
  try {
    const { data } = await profileService.adminList({ role: activeRole.value, search: search.value })
    const results = data.results ?? data
    users.value = results
    total.value = data.count ?? results.length
  } catch {
    $q.notify({ type: 'negative', message: 'Erro ao carregar usuários.', position: 'top', timeout: 3000 })
  } finally {
    loading.value = false
  }
}

function setRole (value) {
  activeRole.value = value
  page.value = 1
  load()
}

function onSearch () {
  page.value = 1
  load()
}

function clearSearch () {
  search.value = ''
  page.value = 1
  load()
}

function loadPage (p) {
  page.value = p
  load()
}

function initials (u) {
  const str = u.name || u.email || ''
  return str.split(' ').slice(0, 2).map(w => w[0]).join('').toUpperCase() || '?'
}

const COLORS = ['#6366F1', '#8B5CF6', '#EC4899', '#F59E0B', '#10B981', '#3B82F6', '#EF4444']
function avatarColor (email) {
  let hash = 0
  for (const c of email) hash = (hash * 31 + c.charCodeAt(0)) & 0xffffffff
  return COLORS[Math.abs(hash) % COLORS.length]
}

onMounted(load)
</script>
