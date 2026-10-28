# Posts do Kayk (@kayk.ceo)

> Este repositório tem **duas linhas de conteúdo separadas**:
> - **Negócios** (este arquivo): Instagram @kayk.ceo, Threads @kayk_offf e LinkedIn. **Nunca** publicar no Facebook.
> - **Fofoca** (`fofoca/FOFOCA.md`): página CEO DAS NOTÍCIAS, **só no Facebook**.

Este repositório guarda o modelo visual e todos os carrosséis publicados no LinkedIn pessoal do Kayk.
Os arquivos ficam públicos por link (`raw.githubusercontent.com`), e o Metricool usa esses links para publicar.

## Estrutura

- `modelo/estilo.css`: estilo base (fundo preto, Anton + Montserrat, destaque marca-texto branco)
- `modelo/story.css`: ajustes para stories 1080×1920 (classes extras: `cta` botão branco, `q` caixa de pergunta)
- `modelo/avatar.jpg`: foto de perfil (já recortada)
- `modelo/gerar.py`: gera os PNGs (slides e stories), o PDF e as legendas a partir de `post.json` (ver o cabeçalho do arquivo)
- `modelo/render.js`: renderiza o HTML em PNG 1080×1350 com Playwright
- `exemplos-empresario/`: **referência principal** de visual e conteúdo (carrossel de 8 slides, 3 stories, card de Threads e legendas).
- `posts/AAAA-MM-DD-slug/`: uma pasta por dia. Os posts até 28/10/2026 usam o visual antigo (verde-limão) e a linha antiga
  (notícia do dia); servem só como referência de tom e de formato das legendas, não de visual.
- `exemplos-threads/`: 5 posts avulsos de Threads aprovados (card + texto), um de cada formato (o visual dos cards agora segue o estilo novo).

Para gerar: `python3 modelo/gerar.py posts/AAAA-MM-DD-slug`

### Visual (aprovado pelo Kayk em 28/10/2026: estilo "Impacto" monocromático)

Fundo preto, títulos gigantes em Anton caixa alta, destaque com **marca-texto branco** (texto preto, levemente inclinado),
textos em Montserrat. **Sem cor nenhuma além de preto, branco e cinza.** Referência completa: `exemplos-empresario/`.

Classes disponíveis no HTML dos slides:
`big` (título gigante Anton; a parte mais forte vai em `<span class="acc">`, que vira o marca-texto branco),
`stat` (número gigante, ex.: `R$ 57 MIL`), `tag` (rótulo cinza pequeno, ex.: "Número 1 de 5"),
`box` (caixa cinza com barra branca à esquerda, com `<p>` dentro), `bg` (número gigante apagado ao fundo, ex.: `<div class="bg">01</div>`),
`p` com `<b>` (texto com negrito branco), `mut` (texto cinza), `src` (linha de fonte),
`vs` (tabela em 2 colunas, primeira linha com `hd` e `hd r`), `ol > li` (lista 01, 02… com número em marca-texto).
Stories: também `cta` (botão branco) e `q` (caixa de pergunta).
Cabeçalho (foto + nome + 01/08) e rodapé ("Arrasta pro lado" / "Salva esse post") são automáticos.
Títulos `big` com no máximo ~6 palavras; texto corrido curto.

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

**Threads avulso: 5 posts por dia, TODOS os dias** (além do carrossel nos dias de carrossel):

| Execução | Posts de Threads |
|---|---|
| Manhã (≈05:47) | 08:30, 11:30 e 14:30 |
| Tarde (≈12:47) | 17:30 e 20:30 |

### 1. Escolher o tema
**Linha editorial (desde 28/10/2026): conteúdo que AGREGA a empresários.** O público é dono de pequena e média empresa.
O post tem que ensinar algo que ele aplica na própria empresa (conta prática com exemplo em reais, passo a passo, erro comum + como evitar),
do tipo que a pessoa salva e manda para o sócio. Temas: finanças da empresa (margem, caixa, precificação, pró-labore, ponto de equilíbrio),
vendas, contratação e liderança, gestão de time, processos, IA aplicada para economizar tempo/dinheiro, impostos e regime tributário.
- Pelo menos 3 de cada 4 carrosséis são **educativos** (atemporais). No máximo 1 em 4 pode partir de uma **notícia** em alta,
  e só se ela afeta diretamente o empresário (imposto, juros, lei trabalhista, crédito); mesmo assim, o foco é "o que fazer na sua empresa".
- Para notícia: pesquisar os assuntos em alta no Brasil (X, notícias, Google) dos últimos 1–3 dias.
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
- Variar o formato ao longo da semana: "N números/erros/passos" (como `exemplos-empresario/`), conta prática, "Achismo vs gestão" / "X vs Y", passo a passo, notícia + o que fazer.
- Conteúdo educativo com contas ilustrativas não precisa de fonte, mas a conta tem que estar certa e o conceito correto. "Regras práticas" do mercado devem ser apresentadas como tal.
- Último slide: frase de impacto + chamada para comentar ou compartilhar.
- `legenda_linkedin`: 800–1.500 caracteres, frases curtas, fontes citadas, termina com uma pergunta. Sem hashtags.
- `legenda_instagram`: mais curta, com pedido para salvar/compartilhar e 4–5 hashtags.
- `titulo`: título interno do post (curto, com o gancho). Não é enviado ao LinkedIn.
- `legenda_threads`: até 450 caracteres (limite do Threads é 500), sem hashtags, tom de conversa.
- `threads` (posts avulsos): cada item tem `card` (HTML de UM card, ideia em até ~15 palavras, texto grande) e
  `texto` (até 450 caracteres, frases curtas, tom de conversa, sem hashtags). Os 5 do dia devem variar entre os formatos:
  **assunto do dia** (opinião sobre notícia de negócios em alta), **dado + comentário**, **pergunta para o público**,
  **frase de impacto** (lição de gestão), **opinião provocativa** ("X não é o mesmo que Y"). Nunca repetir o mesmo assunto
  em dois posts do mesmo dia; podem complementar o tema do carrossel. Mesmas regras de checagem para números e fatos.
  Na execução da tarde, ler o `post.json` de hoje e acrescentar os novos itens em `threads` (não apagar os da manhã).
- `stories`: sempre 3. Uma ideia por story, no máximo ~20 palavras, texto grande. Os stories são imagens:
  links e enquetes não funcionam, então peça resposta "no direct". Mesmas regras de checagem de fatos.

### 4. Gerar e conferir
- Criar `posts/AAAA-MM-DD-slug/post.json` (dia de stories: `stories` + `threads`, sem `slides`) e rodar `python3 modelo/gerar.py`.
- Abrir os PNGs (slides e stories) e conferir: nada cortado, nada sobreposto, texto legível. Corrigir e gerar de novo se precisar.

### 5. Publicar o repositório
- `git add posts/AAAA-MM-DD-slug && git commit && git push origin main`.
- Conferir que **cada PNG** (slides e stories) responde em
  `https://raw.githubusercontent.com/kaykbecker1234/linkedinkayk/main/posts/AAAA-MM-DD-slug/slideNN.png` (ou `storyNN.png`)
  (`curl -sI` deve dar 200 para slide01, slide02… até o último; idem `threadNN.png`) antes de agendar.

### 6. Agendar no Metricool
- Marca: **KAYK.CEO**, `blogId` **7692194**, fuso `America/Sao_Paulo`. Redes da marca: Instagram @kayk.ceo, Threads @kayk_offf, LinkedIn.
- **Nunca publicar na marca resolveia.app.**
- Um `createScheduledPost` **por rede** (cada uma tem seu texto). Use `getScheduledPosts` antes para não duplicar algo já agendado hoje.
- URLs: sempre as raw do GitHub, em ordem.

**Dia de carrossel (09:00):**
- LinkedIn: `providers` `[{"network":"linkedin"}]`, `media` = todos os `slideNN.png`, `linkedinData` = `{"type":"post","publishImagesAsPDF":false}` (sem `documentTitle`, sem PDF), `text` = `legenda_linkedin`.
- Instagram feed: `providers` `[{"network":"instagram"}]`, `media` = todos os `slideNN.png`, `instagramData` = `{"type":"POST"}`, `text` = `legenda_instagram`.
- Threads: `providers` `[{"network":"threads"}]`, `media` = todos os `slideNN.png`, `threadsData` = `{}`, `text` = `legenda_threads`.

**Threads avulso (todo dia, 08:30 / 11:30 / 14:30 de manhã; 17:30 / 20:30 à tarde):**
- Um post por item: `providers` `[{"network":"threads"}]`, `media` = `[threadNN.png]`, `threadsData` = `{}`, `text` = conteúdo de `threadNN.txt`.

**Stories (todo dia, 09:30 / 13:00 / 18:00):**
- Um post por story: `providers` `[{"network":"instagram"}]`, `media` = `[storyNN.png]`, `instagramData` = `{"type":"STORY"}`, **sem `text`**.

- Se já passou do horário de algum item, agende para a próxima hora cheia livre. Se a manhã toda já passou (rotina atrasada), ainda publique, mantendo a ordem.

### 7. Relatar
- Terminar com um resumo curto: tipo do dia (carrossel ou stories), tema, por que foi escolhido, fontes, cada `plannerUrl` do Metricool e link da pasta no GitHub.
- Se algo falhar (sem tema confiável, erro no Metricool, push recusado), não forçar: relatar o problema e parar.
