# CEO DAS NOTÍCIAS (página de fofoca no Facebook)

Página 100% de fofoca e entretenimento, no estilo dos grandes portais de celebridades:
notícia rápida, manchete forte, tom de bastidor. **Identidade própria**: nunca usar nome, logo ou marca de outro portal.

## Estrutura

- `fofoca/card.css`: visual do card (foto em cima, degradê, selo da categoria, manchete, marca "PORTAL CEO DAS NOTÍCIAS")
- `fofoca/gerar_card.py`: gera `card.png` e `legenda.txt` a partir de `post.json` (formato no cabeçalho do arquivo)
- `fofoca/exemplos/`: cards aprovados pelo Kayk. Use como referência de manchete, legenda e enquadramento.
- `fofoca/posts/AAAA-MM-DD-HHMM-slug/`: um card por pasta

Categorias: `FAMOSOS` (⭐ vermelho), `REALITY` (📺 azul), `NOTÍCIAS` (📣 verde), `TV` (🎬 roxo), `MÚSICA` (🎵 laranja).

## Rotina (cada execução gera 2 cards)

| Execução | Cards |
|---|---|
| Manhã | 09:00 e 13:00 |
| Tarde | 17:00 e 21:00 |

### 1. Achar as fofocas
- Ver o que está em alta: trends do X Brasil, Google Trends, "mais lidas" dos portais.
- Ler as últimas notícias dos portais de entretenimento: CNN Brasil Pop, gshow, g1 Pop & Arte, Quem, UOL Splash, Folha F5,
  Terra Diversão, Extra, Notícias da TV, NaTelinha, OFuxico, Contigo, Caras, Metrópoles.
- Ver `fofoca/posts/` dos últimos 3 dias para **não repetir** uma fofoca já publicada (a menos que haja fato novo).
- Escolher as 2 mais quentes e mais confirmadas.

### 2. Checar (obrigatório)
- O fato precisa estar em **pelo menos 2 portais** diferentes da lista acima, ou ter sido dito/postado pela própria pessoa.
- **Citações entre aspas só se forem literais** e aparecerem em matéria. Nunca inventar ou "melhorar" uma frase.
- Especulação vira especulação no texto: "fãs especulam", "rumores apontam", nunca afirmação.
- Fora de pauta: menores de idade como assunto, pessoas anônimas, doença/morte tratadas como fofoca,
  acusação de crime sem processo público, conteúdo íntimo/nudez, temas político-partidários.
- Não usar páginas anônimas de fofoca (Instagram/X) como fonte.

### 3. Escrever
- `manchete`: MAIÚSCULAS, 10 a 20 palavras, fórmula **QUEM + O QUE FEZ + O DETALHE QUE CHOCA**, citação curta entre “aspas” quando houver.
  Destaque com `<em>` a parte mais forte (vira a cor da categoria). Verbos fortes: acaba, detona, rebate, revela, expõe, assume, pede.
- `legenda`: abre com frase curta de impacto + emoji, 2 a 3 parágrafos curtos com os fatos (quem, o quê, quando),
  uma pergunta para comentarem, e no fim `Fontes: <veículos>.` Sem hashtags.

### 4. Foto
- `foto_url` = imagem de destaque (`og:image`) da matéria usada como fonte: `curl -s -A "Mozilla/5.0" <url> | grep og:image`.
  Tirar os parâmetros de corte da URL (`?w=...&h=...&crop=1`) para pegar a imagem inteira.
- `credito` = `Reprodução / <veículo>`.
- Gerar, **abrir o card.png e conferir**: rosto da pessoa visível e bem enquadrado, sem pedaço de outra imagem de montagem,
  sem texto da matéria por cima. Ajustar `foto_recorte` / `foto_posicao` e gerar de novo.
- Não usar a foto se ela mostrar menor de idade em destaque, nudez ou pessoa anônima: escolher outra matéria ou deixar sem `foto_url`.

### 5. Publicar
- `git pull`, `git add fofoca/posts/...`, commit e `git push origin main`.
- Conferir `curl -sI https://raw.githubusercontent.com/kaykbecker1234/linkedinkayk/main/fofoca/posts/<pasta>/card.png` → 200.
- Metricool, marca **KAYK.CEO** (`blogId` **7692194**), fuso `America/Sao_Paulo`:
  `providers` = `[{"network":"facebook"}]` **somente**, `media` = `[URL raw do card.png]`,
  `facebookData` = `{"type":"POST"}`, `text` = legenda.
- **Nunca** publicar fofoca no Instagram, Threads ou LinkedIn (são do perfil de negócios do Kayk).
- Usar `getScheduledPosts` antes para não duplicar.

### 6. Pedido de remoção
Se aparecer qualquer pedido de remoção de foto ou texto (veículo, fotógrafo, pessoa citada), não publicar mais nada daquela fonte e avisar no resumo.

### 7. Relatar
No resumo final: as 2 manchetes, fontes de cada uma, horário agendado e `plannerUrl`.
Se não houver 2 fofocas confirmadas, publicar só as que passaram na checagem (ou nenhuma) e explicar.
