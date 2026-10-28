# Posts do Kayk (@kayk.ceo)

Este repositório guarda o modelo visual e todos os carrosséis publicados no LinkedIn pessoal do Kayk.
Os arquivos ficam públicos por link (`raw.githubusercontent.com`), e o Metricool usa esses links para publicar.

## Estrutura

- `modelo/estilo.css`: estilo base (fundo preto, Montserrat/Poppins, destaque verde-limão `#C6FF3D`)
- `modelo/story.css`: ajustes para stories 1080×1920 (classes extras: `cta` botão verde, `q` caixa de pergunta)
- `modelo/avatar.jpg`: foto de perfil (já recortada)
- `modelo/gerar.py`: gera os PNGs (slides e stories), o PDF e as legendas a partir de `post.json` (ver o cabeçalho do arquivo)
- `modelo/render.js`: renderiza o HTML em PNG 1080×1350 com Playwright
- `posts/AAAA-MM-DD-slug/`: uma pasta por dia. Use os posts existentes como referência de estilo e tom
  (`2026-10-27-6x1-boato` tem exemplo de slides, stories e legenda do Threads).

Para gerar: `python3 modelo/gerar.py posts/AAAA-MM-DD-slug`

### Classes disponíveis no HTML dos slides

`big` (frase de impacto), `stat` (número gigante), `huge` (número/data grande, definido via `css_extra`), `tag` (rótulo verde em caixa alta),
`acc` (texto verde), `mut` (texto cinza), `src` (linha de fonte), `vs` (tabela comparativa em 2 colunas, primeira linha com `hd` e `hd r`),
`ol > li` (lista numerada 01, 02…), `bars/br` (barras comparativas). Cabeçalho (foto + nome) e rodapé (barra de progresso + 01/08) são automáticos.

## Rotina automática de publicação

### 0. Que dia é hoje
A rotina roda todo dia de manhã. Calcule `n` = número de dias entre 2026-10-28 e hoje (America/Sao_Paulo).

- **`n` par → DIA DE CARROSSEL:** 1 carrossel (LinkedIn + Instagram feed + Threads) **e** 3 stories no Instagram divulgando esse carrossel.
- **`n` ímpar → DIA DE STORIES:** só 3 stories no Instagram, sobre um assunto em alta do dia (nada no feed, LinkedIn ou Threads).

| Item | Dia de carrossel | Dia de stories |
|---|---|---|
| Carrossel LinkedIn | 09:00 | — |
| Carrossel Instagram (feed) | 09:00 | — |
| Threads | 09:00 | — |
| Story 1 | 09:30 (chamada para o post novo) | 09:30 (gancho do assunto) |
| Story 2 | 13:00 (o dado/fato principal) | 13:00 (o dado/fato principal) |
| Story 3 | 18:00 (pergunta para responder no direct) | 18:00 (opinião + pergunta) |

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
- Formato do carrossel: 7 a 9 slides (máximo 10, limite do Instagram). Capa com gancho forte, um número/ideia por slide, menos de 25 palavras por slide quando possível.
- Variar o formato ao longo da semana: dado + opinião, desmentido de boato, "X vs Y", passo a passo.
- Último slide: frase de impacto + chamada para comentar ou compartilhar.
- `legenda_linkedin`: 800–1.500 caracteres, frases curtas, fontes citadas, termina com uma pergunta. Sem hashtags.
- `legenda_instagram`: mais curta, com pedido para salvar/compartilhar e 4–5 hashtags.
- `titulo`: título interno do post (curto, com o gancho). Não é enviado ao LinkedIn.
- `legenda_threads`: até 450 caracteres (limite do Threads é 500), sem hashtags, tom de conversa.
- `stories`: sempre 3. Uma ideia por story, no máximo ~20 palavras, texto grande. Os stories são imagens:
  links e enquetes não funcionam, então peça resposta "no direct". Mesmas regras de checagem de fatos.

### 4. Gerar e conferir
- Criar `posts/AAAA-MM-DD-slug/post.json` (dia de stories: só `stories`, sem `slides`) e rodar `python3 modelo/gerar.py`.
- Abrir os PNGs (slides e stories) e conferir: nada cortado, nada sobreposto, texto legível. Corrigir e gerar de novo se precisar.

### 5. Publicar o repositório
- `git add posts/AAAA-MM-DD-slug && git commit && git push origin main`.
- Conferir que **cada PNG** (slides e stories) responde em
  `https://raw.githubusercontent.com/kaykbecker1234/linkedinkayk/main/posts/AAAA-MM-DD-slug/slideNN.png` (ou `storyNN.png`)
  (`curl -sI` deve dar 200 para slide01, slide02… até o último) antes de agendar.

### 6. Agendar no Metricool
- Marca: **KAYK.CEO**, `blogId` **7692194**, fuso `America/Sao_Paulo`. Redes da marca: Instagram @kayk.ceo, Threads @kayk_offf, LinkedIn.
- **Nunca publicar na marca resolveia.app.**
- Um `createScheduledPost` **por rede** (cada uma tem seu texto). Use `getScheduledPosts` antes para não duplicar algo já agendado hoje.
- URLs: sempre as raw do GitHub, em ordem.

**Dia de carrossel (09:00):**
- LinkedIn: `providers` `[{"network":"linkedin"}]`, `media` = todos os `slideNN.png`, `linkedinData` = `{"type":"post","publishImagesAsPDF":false}` (sem `documentTitle`, sem PDF), `text` = `legenda_linkedin`.
- Instagram feed: `providers` `[{"network":"instagram"}]`, `media` = todos os `slideNN.png`, `instagramData` = `{"type":"POST"}`, `text` = `legenda_instagram`.
- Threads: `providers` `[{"network":"threads"}]`, `media` = todos os `slideNN.png`, `threadsData` = `{}`, `text` = `legenda_threads`.

**Stories (todo dia, 09:30 / 13:00 / 18:00):**
- Um post por story: `providers` `[{"network":"instagram"}]`, `media` = `[storyNN.png]`, `instagramData` = `{"type":"STORY"}`, **sem `text`**.

- Se já passou do horário de algum item, agende para a próxima hora cheia livre. Se a manhã toda já passou (rotina atrasada), ainda publique, mantendo a ordem.

### 7. Relatar
- Terminar com um resumo curto: tipo do dia (carrossel ou stories), tema, por que foi escolhido, fontes, cada `plannerUrl` do Metricool e link da pasta no GitHub.
- Se algo falhar (sem tema confiável, erro no Metricool, push recusado), não forçar: relatar o problema e parar.
