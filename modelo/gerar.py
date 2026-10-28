"""Gera as imagens de um post a partir de posts/<pasta>/post.json.

Uso: python3 modelo/gerar.py posts/<pasta>

post.json (todas as chaves são opcionais, exceto que precisa ter "slides" ou "stories"):
{
  "titulo": "Título interno do post",
  "css_extra": "",                         # CSS adicional para slides e stories
  "slides": ["<html do slide 1>", ...],    # carrossel 1080x1350; cabeçalho e rodapé automáticos
  "stories": ["<html do story 1>", ...],   # stories 1080x1920; cabeçalho e rodapé automáticos
  "legenda_linkedin": "...",
  "legenda_instagram": "...",
  "legenda_threads": "...",
  "fontes": ["https://..."]
}

Saída na mesma pasta: slide01.png..., carrossel.pdf, story01.png..., legenda-<rede>.txt
"""
import base64, json, os, subprocess, sys

from PIL import Image

NAME, HANDLE, ACC = "Kayk", "@kayk.ceo", "#C6FF3D"
HERE = os.path.dirname(os.path.abspath(__file__))


def head(avatar):
    return f'<div class="head"><img class="av" src="data:image/jpeg;base64,{avatar}"><div><div class="n">{NAME}</div><div class="h">{HANDLE}</div></div></div>'


def render(pasta, prefixo, paginas, largura, altura):
    for i, html in enumerate(paginas, 1):
        open(os.path.join(pasta, f"{prefixo}{i:02d}.html"), "w", encoding="utf-8").write(html)
    subprocess.run(["node", os.path.join(HERE, "render.js"), pasta, str(len(paginas)), prefixo, str(largura), str(altura)], check=True)
    for i in range(1, len(paginas) + 1):
        os.remove(os.path.join(pasta, f"{prefixo}{i:02d}.html"))
    return [os.path.join(pasta, f"{prefixo}{i:02d}.png") for i in range(1, len(paginas) + 1)]


def main(pasta):
    pasta = os.path.abspath(pasta)
    post = json.load(open(os.path.join(pasta, "post.json"), encoding="utf-8"))
    base = open(os.path.join(HERE, "estilo.css"), encoding="utf-8").read().replace("ACC", ACC)
    story_css = open(os.path.join(HERE, "story.css"), encoding="utf-8").read().replace("ACC", ACC)
    extra = post.get("css_extra", "")
    avatar = base64.b64encode(open(os.path.join(HERE, "avatar.jpg"), "rb").read()).decode()

    slides = post.get("slides", [])
    if slides:
        total = len(slides)
        paginas = [f"""<!doctype html><html><head><meta charset="utf-8"><style>{base}{extra}</style></head><body>
{head(avatar)}
{body}
<div class="foot"><div class="bar"><i style="width:{int(i / total * 100)}%"></i></div><div class="num">{i:02d}/{total:02d}</div></div>
</body></html>""" for i, body in enumerate(slides, 1)]
        pngs = render(pasta, "slide", paginas, 1080, 1350)
        ims = [Image.open(p).convert("RGB") for p in pngs]
        ims[0].save(os.path.join(pasta, "carrossel.pdf"), save_all=True, append_images=ims[1:], resolution=150)
        print(f"{total} slides gerados")

    stories = post.get("stories", [])
    if stories:
        paginas = [f"""<!doctype html><html><head><meta charset="utf-8"><style>{base}{story_css}{extra}</style></head><body class="story">
{head(avatar)}
<div class="miolo">{body}</div>
<div class="sfoot">{HANDLE}</div>
</body></html>""" for body in stories]
        render(pasta, "story", paginas, 1080, 1920)
        print(f"{len(stories)} stories gerados")

    for rede in ("linkedin", "instagram", "threads"):
        texto = post.get(f"legenda_{rede}")
        if texto:
            open(os.path.join(pasta, f"legenda-{rede}.txt"), "w", encoding="utf-8").write(texto.strip() + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
