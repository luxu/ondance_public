<template>
  <q-page class="q-pa-lg">

    <!-- Header -->
    <div class="row items-center justify-between q-mb-lg">
      <div>
        <div class="od-display" style="font-size: 22px; color: var(--od-text-1);">Cidades</div>
        <p style="color: var(--od-text-3); margin: 2px 0 0; font-size: 13px;">
          {{ filteredCities.length }} cidade{{ filteredCities.length !== 1 ? 's' : '' }} encontrada{{ filteredCities.length !== 1 ? 's' : '' }}
        </p>
      </div>
      <q-btn
        unelevated no-caps
        icon="add"
        label="Nova Cidade"
        style="background: var(--od-accent); color: #fff; border-radius: 8px; font-weight: 500;"
        to="/cities/new"
      />
    </div>

    <!-- Filtro -->
    <div class="row items-center q-gutter-sm q-mb-lg">
      <q-input
        v-model="search"
        outlined dense
        placeholder="Buscar por nome ou estado..."
        style="width: 300px;"
      >
        <template #prepend>
          <q-icon name="search" size="16px" :style="{ color: 'var(--od-text-4)' }" />
        </template>
        <template v-if="search" #append>
          <q-icon name="close" size="14px" :style="{ color: 'var(--od-text-4)', cursor: 'pointer' }" @click="search = ''" />
        </template>
      </q-input>
    </div>

    <!-- Estado de carregamento -->
    <div v-if="loading" class="text-center q-py-xl">
      <q-spinner size="32px" :style="{ color: 'var(--od-accent)' }" />
      <p style="font-size: 14px; margin-top: 12px;" :style="{ color: 'var(--od-text-4)' }">Carregando cidades...</p>
    </div>

    <!-- Estado de erro -->
    <div v-else-if="error" class="text-center q-py-xl">
      <q-icon name="wifi_off" size="48px" :style="{ color: 'var(--od-text-5)' }" />
      <p style="font-size: 14px; margin-top: 12px;" :style="{ color: 'var(--od-text-4)' }">{{ error }}</p>
      <q-btn unelevated no-caps label="Tentar novamente" style="background: var(--od-accent); color: #fff; border-radius: 8px; margin-top: 8px;" @click="fetchCities" />
    </div>

    <!-- Lista vazia -->
    <div v-else-if="filteredCities.length === 0" class="text-center q-py-xl">
      <q-icon name="search_off" size="48px" :style="{ color: 'var(--od-text-5)' }" />
      <p style="font-size: 14px; margin-top: 12px;" :style="{ color: 'var(--od-text-4)' }">Nenhuma cidade encontrada</p>
    </div>

    <!-- Lista -->
    <div v-else class="column q-gutter-sm">
      <q-card
        v-for="city in filteredCities"
        :key="city.id"
        flat bordered
        class="od-card"
      >
        <q-card-section class="row items-center" style="gap: 16px; padding: 14px 16px;">

          <q-icon name="location_city" size="20px" :style="{ color: 'var(--od-accent)', flexShrink: 0 }" />

          <div style="flex: 1; min-width: 0;">
            <div style="font-size: 14px; font-weight: 500;" :style="{ color: 'var(--od-text-1)' }">{{ city.name }}</div>
            <div v-if="city.state" style="font-size: 12px;" :style="{ color: 'var(--od-text-3)' }">{{ city.state }}</div>
          </div>

        </q-card-section>
      </q-card>
    </div>

  </q-page>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { cityService } from 'src/services/city'

const cities  = ref([])
const search  = ref('')
const loading = ref(false)
const error   = ref(null)

const filteredCities = computed(() =>
  cities.value.filter(c => {
    if (!search.value) return true
    const q = search.value.toLowerCase()
    return (
      c.name?.toLowerCase().includes(q) ||
      c.state?.toLowerCase().includes(q)
    )
  })
)

async function fetchCities () {
  loading.value = true
  error.value   = null
  try {
    const { data } = await cityService.list()
    cities.value = Array.isArray(data) ? data : (data.results ?? [])
  } catch {
    error.value = 'Não foi possível carregar as cidades. Verifique a conexão com a API.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchCities)
</script>
