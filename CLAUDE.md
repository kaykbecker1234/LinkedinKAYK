# Posts do Kayk (@kayk.ceo)

Este repositório guarda o modelo visual e todos os carrosséis publicados no LinkedIn pessoal do Kayk.
Os arquivos ficam públicos por link (`raw.githubusercontent.com`), e o Metricool usa esses links para publicar.

## Estrutura

- `modelo/estilo.css`: estilo base (fundo preto, Montserrat/Poppins, destaque verde-limão `#C6FF3D`)
- `modelo/avatar.jpg`: foto de perfil (já recortada)
- `modelo/gerar.py`: gera os PNGs, o PDF e as legendas a partir de `post.json`
- `modelo/render.js`: renderiza o HTML em PNG 1080×1350 com Playwright
- `posts/AAAA-MM-DD-slug/`: um post por pasta. Use os posts existentes como referência de estilo e tom.

Para gerar: `python3 modelo/gerar.py posts/AAAA-MM-DD-slug`

### Classes disponíveis no HTML dos slides

`big` (frase de impacto), `stat` (número gigante), `huge` (número/data grande, definido via `css_extra`), `tag` (rótulo verde em caixa alta),
`acc` (texto verde), `mut` (texto cinza), `src` (linha de fonte), `vs` (tabela comparativa em 2 colunas, primeira linha com `hd` e `hd r`),
`ol > li` (lista numerada 01, 02…), `bars/br` (barras comparativas). Cabeçalho (foto + nome) e rodapé (barra de progresso + 01/08) são automáticos.

## Rotina automática de publicação

### 1. Escolher o tema
- Pesquisar os assuntos em alta no Brasil (X, notícias, Google) dos últimos 1–3 dias.
- Filtrar para temas de **negócios, gestão, empreendedorismo, trabalho, IA aplicada a empresas, economia que afeta empresas**.
- Descartar: futebol, celebridades, tragédias, crimes, temas que só façam sentido como disputa partidária.
- Ver `posts/` para não repetir um tema já publicado nos últimos 14 dias (a menos que exista fato novo relevante).

### 2. Checar os fatos (obrigatório)
- Todo número, data e afirmação precisa estar confirmado em **pelo menos 2 fontes confiáveis** (grandes veículos, órgãos oficiais, agências de checagem, pesquisas com autor identificado).
- Se o tema for um boato, o post pode desmentir, mas só com checagem publicada que sustente isso.
- Se não houver confirmação suficiente, escolher outro tema. **Nunca publicar algo não confirmado.**
- Registrar as URLs em `fontes` no `post.json`.

### 3. Escrever
- Tom: direto, provocador, chama atenção. Pode usar gancho agressivo ("FALSO", "você vai pagar caro"), mas **sem mentir e sem exagerar números**.
- Política: falar do **impacto no negócio**, nunca defender ou atacar partido, governo ou político.
- Formato: 7 a 9 slides. Capa com gancho forte, um número/ideia por slide, menos de 25 palavras por slide quando possível.
- Variar o formato ao longo da semana: dado + opinião, desmentido de boato, "X vs Y", passo a passo.
- Último slide: frase de impacto + chamada para comentar ou compartilhar.
- `legenda_linkedin`: 800–1.500 caracteres, frases curtas, fontes citadas, termina com uma pergunta. Sem hashtags.
- `legenda_instagram`: mais curta, com pedido para salvar/compartilhar e 4–5 hashtags.
- `titulo`: título do documento no LinkedIn (curto, com o gancho).

### 4. Gerar e conferir
- Criar `posts/AAAA-MM-DD-slug/post.json` e rodar `python3 modelo/gerar.py`.
- Abrir os PNGs e conferir: nada cortado, nada sobreposto, texto legível. Corrigir e gerar de novo se precisar.

### 5. Publicar o repositório
- `git add posts/AAAA-MM-DD-slug && git commit && git push origin main`.
- Conferir que o PDF responde em
  `https://raw.githubusercontent.com/kaykbecker1234/linkedinkayk/main/posts/AAAA-MM-DD-slug/carrossel.pdf`
  (`curl -sI` deve dar 200) antes de agendar.

### 6. Agendar no Metricool
- Marca: **KAYK.CEO**, `blogId` **7692194**, rede `linkedin`, fuso `America/Sao_Paulo`.
- `media`: a URL raw do `carrossel.pdf`.
- `linkedinData`: `{"documentTitle": "<titulo>", "type": "post"}`.
- `text`: a `legenda_linkedin`.
- Horário padrão: 09:00 (America/Sao_Paulo) do dia da execução; se já passou, o próximo horário cheio disponível.
- Instagram: só agendar se a marca KAYK.CEO tiver Instagram conectado (`getBrandSettings`). Nunca publicar na marca resolveia.app.

### 7. Relatar
- Terminar com um resumo curto: tema, por que foi escolhido, fontes, link do post no Metricool (`plannerUrl`) e link da pasta no GitHub.
- Se algo falhar (sem tema confiável, erro no Metricool, push recusado), não forçar: relatar o problema e parar.
