<template>
  <q-page class="q-pa-lg">
    <div class="row items-center justify-between q-mb-lg">
      <div>
        <div class="od-display" style="font-size: 24px; color: var(--od-text-1);">Meus Cursos</div>
        <p style="color: var(--od-text-3); margin: 4px 0 0; font-size: 14px;">Gerencie os cursos que você criou</p>
      </div>
      <q-btn unelevated no-caps icon="add" label="Novo Curso" to="/professor/cursos/novo"
        style="background: var(--od-accent); color: #fff; border-radius: 8px;" />
    </div>
    <q-card flat bordered class="od-card">
      <q-card-section class="text-center q-py-xl">
        <q-icon name="video_library" size="48px" style="color: var(--od-text-5);" />
        <p style="margin-top: 12px; color: var(--od-text-3);">Lista de cursos — em construção</p>
      </q-card-section>
    </q-card>
  </q-page>
</template>
