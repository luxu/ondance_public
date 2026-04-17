<template>
  <q-page class="q-pa-lg">

    <div class="q-mb-lg">
      <div class="od-display" style="font-size: 24px; color: var(--od-text-1);">Dashboard</div>
      <p style="color: var(--od-text-3); margin: 4px 0 0; font-size: 14px;">Desempenho dos seus cursos</p>
    </div>

    <div class="row q-gutter-sm q-mb-lg">
      <MetricCard class="col" label="Cursos publicados" value="3"   change="↑ 1 este mês"    change-type="up"      accent-color="var(--od-accent)" />
      <MetricCard class="col" label="Alunos matriculados" value="263" change="↑ 41 esta semana" change-type="up"    accent-color="#1D9E75" />
      <MetricCard class="col" label="Aulas criadas"      value="30"  change="↑ 8 recentes"    change-type="up"      accent-color="#7F77DD" />
      <MetricCard class="col" label="Rascunhos"          value="1"   change="aguardando revisão" change-type="neutral" accent-color="#378ADD" />
    </div>

    <div class="row q-gutter-md">
      <div class="col-12 col-md-7">
        <q-card flat bordered class="od-card">
          <q-card-section>
            <div class="row items-center justify-between q-mb-md">
              <div class="od-card-title od-display">Meus cursos recentes</div>
              <q-btn flat no-caps label="ver todos →" style="color: var(--od-accent); font-size: 12px;" to="/professor/cursos" />
            </div>
            <div
              v-for="course in courses" :key="course.id"
              class="row items-center q-py-sm"
              :style="{ borderBottom: '0.5px solid var(--od-border-light)', gap: '12px' }"
            >
              <div class="od-course-thumb" :style="{ background: course.thumbBg }">{{ course.emoji }}</div>
              <div style="flex: 1; min-width: 0;">
                <div style="font-size: 13px; font-weight: 500; color: var(--od-text-1);">{{ course.name }}</div>
                <div style="font-size: 11.5px; color: var(--od-text-3); margin-top: 2px;">{{ course.students }} alunos · {{ course.lessons }} aulas</div>
              </div>
              <q-badge :label="course.status === 'published' ? 'Publicado' : 'Rascunho'"
                :style="course.status === 'published' ? 'background:#D1FAE5;color:#065F46' : 'background:#FEF3C7;color:#92400E'"
                style="font-size:10px; border-radius:6px; padding: 3px 8px;" />
            </div>
          </q-card-section>
        </q-card>
      </div>

      <div class="col">
        <q-card flat bordered class="od-card">
          <q-card-section>
            <div class="od-card-title od-display q-mb-md">Matrículas — 7 dias</div>
            <div class="row items-end" style="height: 80px; gap: 5px;">
              <div v-for="(bar, i) in weekBars" :key="i" class="col"
                style="border-radius: 3px 3px 0 0; background: var(--od-accent); transition: opacity 0.2s;"
                :style="{ height: bar + '%', opacity: i === 4 ? 1 : 0.55 }" />
            </div>
            <div class="row justify-between q-mt-xs" :style="{ fontSize: '10px', color: 'var(--od-text-4)' }">
              <span v-for="d in ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']" :key="d">{{ d }}</span>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>

  </q-page>
</template>

<script setup>
import MetricCard from 'components/shared/MetricCard.vue'

const weekBars = [20, 45, 30, 60, 85, 40, 55]
const courses = [
  { id: 1, name: 'Salsa para Iniciantes', students: 87,  lessons: 12, status: 'published', emoji: '💃', thumbBg: '#FAEEDA' },
  { id: 2, name: 'Forró Universitário',   students: 64,  lessons:  8, status: 'published', emoji: '🕺', thumbBg: '#E1F5EE' },
  { id: 3, name: 'Soltinho Moderno',      students: 112, lessons: 10, status: 'published', emoji: '🪩', thumbBg: '#EEEDFE' },
  { id: 4, name: 'Zouk Avançado',         students:  0,  lessons:  5, status: 'draft',     emoji: '🌊', thumbBg: '#EFF6FF' },
]
</script>
