<template>
  <q-page class="q-pa-lg" style="max-width: 800px; margin: 0 auto;">

    <div style="margin-bottom: 32px;">
      <div class="od-display" style="font-size: 28px; color: var(--od-text-1); margin-bottom: 8px;">
        📖 Como usar o OnDance
      </div>
      <p style="color: var(--od-text-3); font-size: 15px; margin: 0;">
        Guia completo para aproveitar a plataforma de cursos de dança da ABCAA.
      </p>
    </div>

    <!-- Primeiros passos -->
    <q-card flat bordered class="od-card q-mb-lg">
      <q-card-section>
        <div class="od-card-title od-display" style="font-size: 18px; margin-bottom: 16px;">
          🚀 Primeiros passos
        </div>
        <div style="font-size: 14px; color: var(--od-text-3); line-height: 1.7;">
          <p style="margin: 4px 0;"><strong>1.</strong> Acesse o site e clique em <strong>Cadastrar</strong>.</p>
          <p style="margin: 4px 0;"><strong>2.</strong> Use seu email e crie uma senha segura.</p>
          <p style="margin: 4px 0;"><strong>3.</strong> Escolha se você é <strong>Aluno</strong> ou <strong>Professor</strong>.</p>
          <p style="margin: 4px 0;"><strong>4.</strong> Complete seu perfil com nome, foto e cidade.</p>
        </div>
      </q-card-section>
    </q-card>

    <!-- Guia para Alunos -->
    <q-card flat bordered class="od-card q-mb-lg">
      <q-card-section>
        <div class="od-card-title od-display" style="font-size: 18px; margin-bottom: 16px;">
          🎓 Para Alunos
        </div>

        <q-list padding class="q-gutter-y-sm">
          <q-expansion-item
            expand-separator
            icon="explore"
            label="Como explorar cursos"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                No menu lateral, clique em <strong>Explorar</strong>. Você verá todos os cursos publicados e aprovados pela equipe OnDance. Clique em um curso para ver a descrição, o professor e a quantidade de aulas.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            icon="play_circle"
            label="Como assistir aulas"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Acesse <strong>Meus Cursos</strong> no menu lateral. Clique no curso desejado e escolha a aula que quer assistir. O vídeo abrirá na página de reprodução. Você pode pausar, voltar e avançar no seu ritmo.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            icon="bar_chart"
            label="Como acompanhar meu progresso"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                O dashboard mostra seu progresso geral em porcentagem. Acesse <strong>Progresso</strong> no menu para ver o detalhe de cada curso: aulas concluídas, tempo assistido e o que falta para terminar.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            icon="workspace_premium"
            label="Como obter certificados"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Ao concluir todas as aulas de um curso, o sistema gera automaticamente seu certificado. Acesse <strong>Certificados</strong> no menu para visualizar e baixar o PDF com seu código único de validação.
              </q-card-section>
            </q-card>
          </q-expansion-item>
        </q-list>
      </q-card-section>
    </q-card>

    <!-- Guia para Professores -->
    <q-card flat bordered class="od-card q-mb-lg">
      <q-card-section>
        <div class="od-card-title od-display" style="font-size: 18px; margin-bottom: 16px;">
          🎤 Para Professores
        </div>

        <q-list padding class="q-gutter-y-sm">
          <q-expansion-item
            expand-separator
            icon="add_circle"
            label="Como criar um curso"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                No painel do professor, clique em <strong>Criar Curso</strong>. Preencha o título, descrição, duração estimada e nível (Iniciante, Intermediário ou Avançado). Escolha um emoji e a cor do card para deixar o curso com a sua cara. Depois, clique em <strong>Salvar</strong>.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            icon="video_library"
            label="Como adicionar módulos e aulas"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Acesse o curso que criou e clique em <strong>Aulas</strong>. Clique em <strong>Adicionar módulo</strong> e dê um nome (ex: "Módulo 1 — Passos Básicos"). Dentro do módulo, clique em <strong>Adicionar aula</strong>, insira o título e o link do vídeo (YouTube, Vimeo, etc.). Você pode reorganizar a ordem dos módulos e aulas.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            icon="publish"
            label="Como publicar um curso"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Quando seu curso estiver completo, ele é enviado automaticamente para a equipe OnDance. O status muda para <strong>Pendente</strong>. Após a moderação, ele pode ser <strong>Aprovado</strong> (fica no ar) ou <strong>Rejeitado</strong> (você recebe orientações para ajustar). Você acompanha o status em <strong>Meus Cursos</strong>.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            icon="group"
            label="Como ver meus alunos"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                No menu lateral, clique em <strong>Meus Alunos</strong>. Você verá a lista de alunos matriculados em seus cursos, com nome, email, data de início e se já concluíram. É possível filtrar por curso para ver o desempenho de uma turma específica.
              </q-card-section>
            </q-card>
          </q-expansion-item>
        </q-list>
      </q-card-section>
    </q-card>

    <!-- Moderação -->
    <q-card flat bordered class="od-card q-mb-lg">
      <q-card-section>
        <div class="od-card-title od-display" style="font-size: 18px; margin-bottom: 16px;">
          📋 Como funciona a moderação
        </div>
        <div style="font-size: 14px; color: var(--od-text-3); line-height: 1.7;">
          <p style="margin: 4px 0;"><strong>Pendente</strong> — Curso criado e aguardando análise da equipe OnDance.</p>
          <p style="margin: 4px 0;"><strong>Aprovado</strong> — Curso publicado e visível para todos os alunos.</p>
          <p style="margin: 4px 0;"><strong>Rejeitado</strong> — Curso não atendeu aos critérios e precisa de ajustes.</p>
        </div>
      </q-card-section>
    </q-card>

    <!-- Dúvidas comuns -->
    <q-card flat bordered class="od-card q-mb-lg">
      <q-card-section>
        <div class="od-card-title od-display" style="font-size: 18px; margin-bottom: 16px;">
          ❓ Dúvidas comuns
        </div>

        <q-list padding class="q-gutter-y-sm">
          <q-expansion-item
            expand-separator
            label="Esqueci minha senha"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Na tela de login, clique em <strong>Esqueci a senha</strong>. Digite seu email e enviaremos instruções para redefinição. O link é válido por 24 horas.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            label="Quem pode ver meu curso?"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Após aprovação, qualquer aluno cadastrado pode visualizar e se matricular. Cursos pendentes ou rejeitados não aparecem no catálogo.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            label="Posso ser aluno e professor ao mesmo tempo?"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Não. No cadastro você escolhe um perfil. Caso queira mudar, entre em contato com o suporte da ABCAA.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            label="Onde fica meu certificado?"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                Acesse <strong>Certificados</strong> no menu lateral. Lá você encontra todos os certificados conquistados, com código de validação e opção de download em PDF.
              </q-card-section>
            </q-card>
          </q-expansion-item>

          <q-expansion-item
            expand-separator
            label="Como mudar para modo escuro?"
            header-class="help-expansion-header"
          >
            <q-card flat>
              <q-card-section style="font-size: 14px; color: var(--od-text-3); line-height: 1.6;">
                No canto superior direito da tela, clique no ícone de <strong>lua</strong> para ativar o modo escuro. Para voltar ao modo claro, clique no ícone de <strong>sol</strong>.
              </q-card-section>
            </q-card>
          </q-expansion-item>
        </q-list>
      </q-card-section>
    </q-card>

    <!-- Footer -->
    <div style="text-align: center; padding: 24px 0; color: var(--od-text-4); font-size: 13px;">
      Ainda tem dúvidas? Entre em contato com o suporte da ABCAA.
      <br>
      Última atualização: 12 de junho de 2026
    </div>

  </q-page>
</template>

<script setup>
// Nenhuma lógica necessária — página estática de ajuda
</script>

<style scoped>
.help-expansion-header {
  font-weight: 500;
  font-size: 14px;
  color: var(--od-text-1);
  border-radius: 8px;
}
</style>
