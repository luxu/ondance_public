<template>
  <q-page class="index-page q-pa-none">
    <!-- Two Column Layout -->
    <div class="row no-wrap items-center justify-center full-height index-row">
      
      <!-- Left Column - Welcome/Login Section -->
      <div class="left-column col">
        <div class="welcome-section">
          <h1 class="welcome-title">Bem-vindo de volta!</h1>
          <p class="welcome-subtitle">Para se manter conectado, faça login com suas informações pessoais</p>
          
          <router-link to="/login">
            <q-btn
              unelevated
              no-caps
              label="FAZER LOGIN"
              class="welcome-btn"
            />
          </router-link>
        </div>
      </div>

      <!-- Right Column - Signup Section -->
      <div class="right-column col">
        <div class="signup-section">
          <h2 class="signup-title">Criar Conta</h2>
          <p class="signup-subtitle">ou use seu email para se registrar</p>

          <!-- Social Login Icons -->
          <div class="social-icons q-my-md">
            <a href="#" class="social-icon facebook" title="Facebook">
              <q-icon name="fab fa-facebook-f" />
            </a>
            <a href="#" class="social-icon google" title="Google">
              <q-icon name="fab fa-google" />
            </a>
            <a href="#" class="social-icon linkedin" title="LinkedIn">
              <q-icon name="fab fa-linkedin-in" />
            </a>
          </div>

          <!-- Form -->
          <q-form @submit.prevent="handleQuickSignup">
            <div class="form-group">
              <q-input
                v-model="quickForm.email"
                outlined
                dense
                type="email"
                placeholder="Email"
                class="form-input"
                :rules="[
                  val => !!val || 'Campo obrigatório',
                  val => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) || 'Email inválido'
                ]"
              >
                <template #prepend>
                  <q-icon name="mail" />
                </template>
              </q-input>
            </div>

            <div class="form-group">
              <q-input
                v-model="quickForm.password"
                outlined
                dense
                :type="showQuickPassword ? 'text' : 'password'"
                placeholder="Senha (mín. 8 caracteres)"
                class="form-input"
                :rules="[
                  val => !!val || 'Campo obrigatório',
                  val => val.length >= 8 || 'Mínimo 8 caracteres'
                ]"
              >
                <template #prepend>
                  <q-icon name="lock" />
                </template>
                <template #append>
                  <q-icon
                    :name="showQuickPassword ? 'visibility' : 'visibility_off'"
                    class="cursor-pointer"
                    @click="showQuickPassword = !showQuickPassword"
                  />
                </template>
              </q-input>
            </div>

            <q-btn
              unelevated
              no-caps
              type="submit"
              label="CADASTRAR"
              class="signup-btn"
              :loading="signingUp"
            />
          </q-form>

          <p class="form-footer">
            Prefere preencher tudo?
            <router-link to="/register" class="full-form-link">
              Formulário completo
            </router-link>
          </p>
        </div>
      </div>

    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { authService } from 'src/services/auth'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const quickForm = ref({
  email: '',
  password: ''
})

const showQuickPassword = ref(false)
const signingUp = ref(false)

function extractApiError(error, fallback = 'Erro inesperado. Tente novamente.') {
  const data = error.response?.data
  if (!data) return fallback
  const messages = [...new Set(Object.values(data).flat())]
  return messages.length ? messages.join(' ') : fallback
}

async function handleQuickSignup() {
  signingUp.value = true
  try {
    await authService.register({
      email: quickForm.value.email,
      password: quickForm.value.password,
    })

    $q.notify({
      type: 'positive',
      message: 'Cadastro realizado! Verifique seu email.',
      position: 'top'
    })

    quickForm.value = { email: '', password: '' }
  } catch (error) {
    $q.notify({
      type: 'negative',
      message: extractApiError(error, 'Erro ao criar conta. Tente novamente.'),
      position: 'top'
    })
  } finally {
    signingUp.value = false
  }
}
</script>

<style scoped>
.index-page {
  min-height: calc(100vh - 56px);
  background: var(--od-bg-page);
}

.index-row {
  max-width: 1080px;
  width: 100%;
  margin: 0 auto;
  min-height: calc(100vh - 56px);
}

.left-column,
.right-column {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 36px;
  min-height: 100%;
}

.left-column {
  flex: 0 0 360px;
  background: var(--od-bg-surface);
  border-right: 1px solid var(--od-border);
}

.right-column {
  flex: 1 1 520px;
  min-width: 360px;
  background: var(--od-bg-page);
}

.welcome-section {
  max-width: 340px;
  width: 100%;
  text-align: left;
}

.signup-section {
  width: 100%;
  max-width: 420px;
  background: var(--od-bg-surface);
  border: 1px solid var(--od-border);
  border-radius: 32px;
  padding: 32px;
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.06);
}

.welcome-title {
  font-size: 42px;
  font-weight: 700;
  margin: 0 0 18px 0;
  color: var(--od-text-1);
}

.welcome-subtitle {
  font-size: 16px;
  line-height: 1.8;
  margin: 0 0 28px 0;
  color: var(--od-text-2);
}

.welcome-btn {
  background: var(--od-accent) !important;
  color: #fff !important;
  padding: 14px 34px !important;
  border-radius: 24px !important;
  font-weight: 700 !important;
  font-size: 13px !important;
  transition: all 0.3s ease;
}

.welcome-btn:hover {
  transform: translateY(-2px);
}

.right-column {
  min-width: 60%;
  background: var(--od-bg-page);
}

.signup-section {
  width: 100%;
  max-width: 420px;
  background: var(--od-bg-surface);
  border: 1px solid var(--od-border);
  border-radius: 32px;
  padding: 32px;
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.06);
}

.signup-title {
  font-size: 30px;
  font-weight: 700;
  margin: 0 0 10px 0;
  color: var(--od-text-1);
}

.signup-subtitle {
  font-size: 14px;
  color: var(--od-text-3);
  margin: 0 0 24px 0;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--od-border);
}

.social-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid var(--od-border);
  color: var(--od-text-2);
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 16px;
}

.social-icon:hover {
  border-color: var(--od-accent);
  color: var(--od-accent);
  transform: translateY(-2px);
}

.form-group {
  margin-bottom: 14px;
}

.form-input {
  font-size: 13px;
}

:deep(.form-input .q-field__control) {
  padding: 10px 12px !important;
  background: var(--od-bg-subtle);
  border-radius: 16px;
}

:deep(.form-input .q-icon) {
  color: var(--od-text-3);
}

:deep(.form-input.q-focused .q-icon) {
  color: var(--od-accent);
}

.signup-btn {
  width: 100% !important;
  background: var(--od-accent) !important;
  color: white !important;
  padding: 14px !important;
  border-radius: 24px !important;
  font-weight: 700 !important;
  font-size: 13px !important;
  letter-spacing: 0.5px;
  margin-top: 16px;
}

.form-footer {
  text-align: center;
  font-size: 13px;
  color: var(--od-text-3);
  margin-top: 18px;
}

.full-form-link {
  color: var(--od-accent);
  text-decoration: none;
  font-weight: 700;
}

.full-form-link:hover {
  text-decoration: underline;
}

@media (max-width: 960px) {
  .left-column,
  .right-column {
    min-width: 100%;
    padding: 24px;
  }

  .row {
    flex-direction: column;
  }

  .welcome-title {
    font-size: 32px;
  }
}
</style>

