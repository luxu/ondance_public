<template>
  <q-page class="q-pa-lg">

    <!-- Header -->
    <div class="row items-center q-mb-lg" style="gap: 12px;">
      <q-btn flat round dense icon="arrow_back" :style="{ color: 'var(--od-text-2)' }" @click="$router.push('/cities/initial')" />
      <div>
        <div class="od-display" style="font-size: 22px; color: var(--od-text-1);">Nova Cidade</div>
        <p style="color: var(--od-text-3); margin: 2px 0 0; font-size: 13px;">Preencha as informações da cidade</p>
      </div>
    </div>

    <div style="max-width: 480px;">
      <q-form ref="formRef" @submit.prevent="handleSubmit">

        <q-card flat bordered class="od-card q-mb-md">
          <q-card-section>
            <div class="od-card-title od-display q-mb-md">Informações da cidade</div>
            <div class="column q-gutter-sm">

              <q-input
                v-model="form.name"
                outlined dense
                label="Nome *"
                :rules="[val => !!val || 'Campo obrigatório']"
              />

              <q-select
                v-model="form.state"
                outlined dense
                use-input
                hide-selected
                fill-input
                input-debounce="300"
                label="Estado *"
                :options="stateOptions"
                option-value="id"
                option-label="name"
                emit-value map-options
                :loading="loadingStates"
                no-error-icon
                :rules="[val => !!val || 'Campo obrigatório']"
                @filter="filterStates"
              >
                <template #no-option>
                  <q-item>
                    <q-item-section style="font-size: 13px; color: var(--od-text-4);">
                      {{ stateQuery.length < 3 ? 'Digite ao menos 3 letras' : 'Nenhum estado encontrado' }}
                    </q-item-section>
                  </q-item>
                </template>
              </q-select>

            </div>
          </q-card-section>
        </q-card>

        <div class="row q-gutter-sm justify-end">
          <q-btn
            flat no-caps
            label="Cancelar"
            style="color: var(--od-text-3);"
            @click="$router.push('/cities/initial')"
          />
          <q-btn
            unelevated no-caps
            type="submit"
            label="Salvar"
            :loading="saving"
            style="background: var(--od-accent); color: #fff; border-radius: 8px; font-weight: 500;"
          />
        </div>

      </q-form>
    </div>

  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { cityService } from 'src/services/city'
import { stateService } from 'src/services/state'

const router  = useRouter()
const formRef = ref(null)
const saving  = ref(false)

const form         = ref({ name: '', state: null })
const stateOptions = ref([])
const loadingStates = ref(false)
const stateQuery   = ref('')

async function filterStates (query, update, abort) {
  stateQuery.value = query

  if (query.length < 3) {
    update(() => { stateOptions.value = [] })
    return
  }

  loadingStates.value = true
  try {
    const { data } = await stateService.list(query)
    update(() => {
      stateOptions.value = Array.isArray(data) ? data : (data.results ?? [])
    })
  } catch {
    abort()
  } finally {
    loadingStates.value = false
  }
}

async function handleSubmit () {
  saving.value = true
  try {
    await cityService.create(form.value)
    router.push('/cities/initial')
  } finally {
    saving.value = false
  }
}
</script>
