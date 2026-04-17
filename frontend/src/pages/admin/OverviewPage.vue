<template>
  <q-page class="q-pa-lg">

    <div class="q-mb-lg">
      <div class="od-display" style="font-size: 24px; color: var(--od-text-1);">Visão Geral</div>
      <p style="color: var(--od-text-3); margin: 4px 0 0; font-size: 14px;">KPIs globais da plataforma</p>
    </div>

    <div class="row q-gutter-sm q-mb-lg">
      <MetricCard class="col" label="Usuários ativos"    value="1.2k" change="↑ 89 este mês"   change-type="up"      accent-color="var(--od-accent)" />
      <MetricCard class="col" label="Cursos publicados"  value="18"   change="↑ 3 esta semana"  change-type="up"      accent-color="#1D9E75" />
      <MetricCard class="col" label="Matrículas totais"  value="4.7k" change="↑ 210 este mês"   change-type="up"      accent-color="#7F77DD" />
      <MetricCard class="col" label="Aprovações pendentes" value="7" change="aguardando revisão" change-type="neutral" accent-color="#E97B3C" />
    </div>

    <div class="row q-gutter-md">
      <div class="col-12 col-md-6">
        <q-card flat bordered class="od-card">
          <q-card-section>
            <div class="od-card-title od-display q-mb-md">Cursos aguardando aprovação</div>
            <div v-for="c in pendingCourses" :key="c.id" class="row items-center q-py-sm"
              :style="{ borderBottom: '0.5px solid var(--od-border-light)', gap: '12px' }">
              <div class="od-course-thumb" :style="{ background: c.thumbBg }">{{ c.emoji }}</div>
              <div style="flex:1; min-width:0;">
                <div style="font-size: 13px; font-weight: 500; color: var(--od-text-1);">{{ c.name }}</div>
                <div style="font-size: 11.5px; color: var(--od-text-3);">{{ c.teacher }}</div>
              </div>
              <q-btn dense flat no-caps label="Revisar" style="color: var(--od-accent); font-size: 11px;" to="/admin/cursos" />
            </div>
          </q-card-section>
        </q-card>
      </div>

      <div class="col">
        <q-card flat bordered class="od-card">
          <q-card-section>
            <div class="od-card-title od-display q-mb-md">Novos usuários — 7 dias</div>
            <div class="row items-end" style="height: 80px; gap: 5px;">
              <div v-for="(bar, i) in weekBars" :key="i" class="col"
                style="border-radius: 3px 3px 0 0; background: var(--od-accent);"
                :style="{ height: bar + '%', opacity: i === 5 ? 1 : 0.45 }" />
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

const weekBars = [35, 55, 42, 68, 50, 90, 45]
const pendingCourses = [
  { id: 1, name: 'Zouk Avançado',       teacher: 'Prof. Renata Souza', emoji: '🌊', thumbBg: '#EFF6FF' },
  { id: 2, name: 'Axé Groove',          teacher: 'Prof. Marta Silva',  emoji: '🎶', thumbBg: '#FEF9EE' },
  { id: 3, name: 'Lambada Contemporânea', teacher: 'Prof. Paulo Jr.',   emoji: '🌀', thumbBg: '#F0FDF4' },
]
</script>
