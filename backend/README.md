# OnDance Backend

Backend da plataforma OnDance — Django 6 + Django REST Framework.

## Configuração inicial

### 1. Instalar dependências

```bash
uv sync
```

### 2. Configurar variáveis de ambiente

```bash
cp contrib/env-sample .env
python contrib/env_gen.py  # gera SECRET_KEY aleatória
```

### 3. Aplicar migrações

```bash
task migrate
```

### 4. Carregar dados de referência

Estados e cidades brasileiras são dados fixos e precisam ser carregados uma única vez:

```bash
task load_states   # 27 estados (deve ser executado antes das cidades)
task load_cities   # 5.571 municípios com FK para os estados
```

> **Ordem importa:** `load_states` deve rodar antes de `load_cities` por causa da chave estrangeira.

### 5. (Opcional) Regenerar fixture de cidades

O arquivo `user/fixtures/cities.json` já está commitado. Caso precise regenerá-lo com dados atualizados do IBGE:

```bash
python contrib/gen_cities_fixture.py
```

---

## Rodar o servidor

```bash
task runserver
```
