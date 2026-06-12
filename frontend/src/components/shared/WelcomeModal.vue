<template>
  <q-dialog v-model="show" persistent>
    <q-card style="width: 480px; max-width: 92vw; border-radius: 16px; padding: 0; background: var(--od-bg-surface);">

      <!-- Header com indicador de passo -->
      <q-card-section style="padding: 24px 24px 12px;">
        <div class="row items-center justify-between" style="margin-bottom: 8px;">
          <div style="display: flex; gap: 6px;">
            <div
              v-for="n in totalSteps"
              :key="n"
              style="width: 8px; height: 8px; border-radius: 50%; transition: background 0.3s;"
              :style="{ background: n === step ? 'var(--od-accent)' : 'var(--od-border)' }"
            />
          </div>
          <q-btn flat round dense icon="close" size="sm" style="color: var(--od-text-3);" @click="dismiss" />
        </div>
      </q-card-section>

      <!-- Conteúdo do passo -->
      <q-card-section style="padding: 0 24px 16px;">
        <div v-if="step === 1" class="text-center">
          <div style="font-size: 48px; margin-bottom: 12px;">🎉</div>
          <div style="font-size: 20px; font-weight: 600; color: var(--od-text-1); margin-bottom: 8px;">
            Bem-vindo ao OnDance!
          </div>
          <div style="font-size: 14px; color: var(--od-text-3); line-height: 1.5;">
            A plataforma de cursos de dança da ABCAA. Aqui você aprende, ensina e evolui.
          </div>
        </div>

        <div v-if="step === 2">
          <div style="font-size: 18px; font-weight: 600; color: var(--od-text-1); margin-bottom: 16px; text-align: center;">
            🎓 Para Alunos
          </div>
          <div class="wm-step-list">
            <div class="wm-step-item">
              <div class="wm-step-icon">🔍</div>
              <div>
                <div class="wm-step-title">Explore cursos</div>
                <div class="wm-step-desc">Navegue pelo catálogo e descubra aulas de diversos estilos.</div>
              </div>
            </div>
            <div class="wm-step-item">
              <div class="wm-step-icon">📝</div>
              <div>
                <div class="wm-step-title">Matricule-se</div>
                <div class="wm-step-desc">Escolha um curso e comece a aprender imediatamente.</div>
              </div>
            </div>
            <div class="wm-step-item">
              <div class="wm-step-icon">▶️</div>
              <div>
                <div class="wm-step-title">Assista e pratique</div>
                <div class="wm-step-desc">Acompanhe as aulas no seu ritmo e marque o progresso.</div>
              </div>
            </div>
            <div class="wm-step-item">
              <div class="wm-step-icon">🏆</div>
              <div>
                <div class="wm-step-title">Ganhe certificados</div>
                <div class="wm-step-desc">Ao concluir, receba seu certificado de participação.</div>
              </div>
            </div>
          </div>
        </div>

        <div v-if="step === 3">
          <div style="font-size: 18px; font-weight: 600; color: var(--od-text-1); margin-bottom: 16px; text-align: center;">
            🎤 Para Professores
          </div>
          <div class="wm-step-list">
            <div class="wm-step-item">
              <div class="wm-step-icon">📚</div>
              <div>
                <div class="wm-step-title">Crie seu curso</div>
                <div class="wm-step-desc">Defina título, descrição, nível e personalize a aparência.</div>
              </div>
            </div>
            <div class="wm-step-item">
              <div class="wm-step-icon">📹</div>
              <div>
                <div class="wm-step-title">Adicione aulas</div>
                <div class="wm-step-desc">Organize em módulos e insira os links dos vídeos.</div>
              </div>
            </div>
            <div class="wm-step-item">
              <div class="wm-step-icon">🚀</div>
              <div>
                <div class="wm-step-title">Publique</div>
                <div class="wm-step-desc">Envie para moderação e, após aprovação, seu curso fica no ar.</div>
              </div>
            </div>
            <div class="wm-step-item">
              <div class="wm-step-icon">📊</div>
              <div>
                <div class="wm-step-title">Acompanhe alunos</div>
                <div class="wm-step-desc">Veja quem se matriculou e o progresso de cada um.</div>
              </div>
            </div>
          </div>
        </div>

        <div v-if="step === 4" class="text-center">
          <div style="font-size: 48px; margin-bottom: 12px;">💡</div>
          <div style="font-size: 18px; font-weight: 600; color: var(--od-text-1); margin-bottom: 12px;">
            Dicas rápidas
          </div>
          <div style="font-size: 14px; color: var(--od-text-3); line-height: 1.6; text-align: left;">
            <p style="margin: 4px 0;">• Complete seu perfil para uma experiência personalizada.</p>
            <p style="margin: 4px 0;">• Use o modo escuro no ícone de lua no canto superior.</p>
            <p style="margin: 4px 0;">• Precisa de ajuda? Acesse <strong>Como usar</strong> no menu lateral.</p>
          </div>
        </div>
      </q-card-section>

      <!-- Actions -->
      <q-card-actions align="right" style="padding: 8px 24px 24px;">
        <q-btn
          v-if="step > 1"
          flat no-caps
          label="Voltar"
          style="color: var(--od-text-3); font-size: 13px;"
          @click="step--"
        />
        <q-btn
          v-if="step < totalSteps"
          unelevated no-caps
          label="Próximo"
          style="background: var(--od-accent); color: #fff; border-radius: 8px; font-size: 13px;"
          @click="step++"
        />
        <q-btn
          v-else
          unelevated no-caps
          label="Começar"
          style="background: var(--od-accent); color: #fff; border-radius: 8px; font-size: 13px;"
          @click="finish"
        />
      </q-card-actions>

    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const emit = defineEmits(['close'])

const show = ref(false)
const step = ref(1)
const totalSteps = 4

onMounted(() => {
  const seen = localStorage.getItem('ondance_welcome_seen')
  if (!seen) {
    show.value = true
  }
})

function dismiss() {
  localStorage.setItem('ondance_welcome_seen', 'true')
  show.value = false
  emit('close')
}

function finish() {
  localStorage.setItem('ondance_welcome_seen', 'true')
  show.value = false
  emit('close')
}
</script>

<style scoped>
.wm-step-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.wm-step-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 10px;
  background: var(--od-bg-page);
}

.wm-step-icon {
  font-size: 24px;
  flex-shrink: 0;
  line-height: 1;
}

.wm-step-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--od-text-1);
  margin-bottom: 2px;
}

.wm-step-desc {
  font-size: 12.5px;
  color: var(--od-text-3);
  line-height: 1.4;
}
</style>
