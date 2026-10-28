"""Gera o card da página CEO DAS NOTÍCIAS (Facebook) a partir de fofoca/posts/<pasta>/post.json.

Uso: python3 fofoca/gerar_card.py fofoca/posts/<pasta>

post.json:
{
  "categoria": "FAMOSOS",                 # FAMOSOS, REALITY, NOTÍCIAS, TV, MÚSICA
  "manchete": "FULANO FAZ ISSO E <em>AQUILO</em>",   # <em> destaca na cor da categoria
  "foto_url": "https://.../imagem.jpg",   # og:image da matéria-fonte (opcional)
  "foto_recorte": [x1, y1, x2, y2],       # opcional: recorta a foto original antes de usar
  "foto_posicao": "50% 25%",              # opcional: enquadramento (object-position)
  "credito": "Reprodução / CNN Brasil",
  "legenda": "...",
  "fontes": ["https://...", "https://..."]
}

Saída na mesma pasta: foto.jpg (se houver), card.png, legenda.txt
"""
import base64, io, json, os, subprocess, sys, urllib.request

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RENDER = os.path.join(HERE, "..", "modelo", "render.js")

CATEGORIAS = {
    "FAMOSOS": ("#FF2D55", "⭐"),
    "REALITY": ("#00B7FF", "📺"),
    "NOTÍCIAS": ("#00C27A", "📣"),
    "TV": ("#9B5CFF", "🎬"),
    "MÚSICA": ("#FF9F1A", "🎵"),
}


def baixar_foto(post, pasta):
    url = post.get("foto_url")
    if not url:
        return None
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    im = Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=30).read())).convert("RGB")
    if post.get("foto_recorte"):
        im = im.crop(tuple(post["foto_recorte"]))
    destino = os.path.join(pasta, "foto.jpg")
    im.save(destino, quality=92)
    return destino


def main(pasta):
    pasta = os.path.abspath(pasta)
    post = json.load(open(os.path.join(pasta, "post.json"), encoding="utf-8"))
    cor, icone = CATEGORIAS[post["categoria"]]
    css = open(os.path.join(HERE, "card.css"), encoding="utf-8").read()
    css = css.replace("COLOR", cor).replace("POS", post.get("foto_posicao", "50% 25%"))

    foto = baixar_foto(post, pasta)
    if foto:
        b64 = base64.b64encode(open(foto, "rb").read()).decode()
        fundo = f'<img class="ph" src="data:image/jpeg;base64,{b64}"><div class="fade"></div><div class="cred">Foto: {post.get("credito", "Reprodução")}</div>'
    else:
        fundo = '<div class="semfoto"></div><div class="fade"></div>'

    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
{fundo}
<div class="box"><div class="chip"><span class="i">{icone}</span>{post["categoria"]}</div><h1>{post["manchete"]}</h1></div>
<div class="logo"><small>PORTAL</small><b>CEO DAS <i>NOTÍCIAS</i></b></div><div class="line"></div>
</body></html>"""
    open(os.path.join(pasta, "card01.html"), "w", encoding="utf-8").write(html)
    subprocess.run(["node", RENDER, pasta, "1", "card", "1080", "1350"], check=True)
    os.remove(os.path.join(pasta, "card01.html"))
    os.replace(os.path.join(pasta, "card01.png"), os.path.join(pasta, "card.png"))
    open(os.path.join(pasta, "legenda.txt"), "w", encoding="utf-8").write(post["legenda"].strip() + "\n")
    print("card gerado em", pasta)


if __name__ == "__main__":
    main(sys.argv[1])
