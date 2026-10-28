"""Gera as imagens de um post a partir de posts/<pasta>/post.json.

Uso: python3 modelo/gerar.py posts/<pasta>

post.json (todas as chaves são opcionais, exceto que precisa ter "slides" ou "stories"):
{
  "titulo": "Título interno do post",
  "css_extra": "",                         # CSS adicional para slides e stories
  "slides": ["<html do slide 1>", ...],    # carrossel 1080x1350; cabeçalho e rodapé automáticos
  "stories": ["<html do story 1>", ...],   # stories 1080x1920; cabeçalho e rodapé automáticos
  "threads": [{"card": "<html>", "texto": "..."}, ...],  # posts avulsos do Threads: 1 card 1080x1350 + texto
  "legenda_linkedin": "...",
  "legenda_instagram": "...",
  "legenda_threads": "...",
  "fontes": ["https://..."]
}

Saída na mesma pasta: slide01.png..., carrossel.pdf, story01.png..., thread01.png..., legenda-<rede>.txt, thread01.txt...
"""
import base64, json, os, subprocess, sys

from PIL import Image

NAME, HANDLE, ACC = "Kayk", "@kayk.ceo", "#FFFFFF"
HERE = os.path.dirname(os.path.abspath(__file__))


def head(avatar, pg=""):
    pg = f'<span class="pg">{pg}</span>' if pg else ""
    return f'<div class="head"><img class="av" src="data:image/jpeg;base64,{avatar}"><div><div class="n">{NAME}</div><div class="h">{HANDLE}</div></div>{pg}</div>'


def foot(i, total):
    if i == 1:
        return '<div class="foot"><span>Arrasta pro lado</span><b>SALVA ESSE POST</b></div>'
    if i == total:
        return '<div class="foot"><span>Manda pra um sócio</span><b>SALVA ESSE POST</b></div>'
    return '<div class="foot"><span>Arrasta pro lado</span><span>→</span></div>'


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
{head(avatar, f"{i:02d}/{total:02d}")}
<div class="miolo">{body}</div>
{foot(i, total)}
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
</body></html>""" for body in stories]
        render(pasta, "story", paginas, 1080, 1920)
        print(f"{len(stories)} stories gerados")

    threads = post.get("threads", [])
    if threads:
        thread_css = ".big{font-size:130px}p{font-size:46px}.tag{font-size:30px}.src{font-size:24px}"
        paginas = [f"""<!doctype html><html><head><meta charset="utf-8"><style>{base}{thread_css}{extra}</style></head><body>
{head(avatar)}
<div class="miolo">{t["card"]}</div>
</body></html>""" for t in threads]
        render(pasta, "thread", paginas, 1080, 1350)
        for i, t in enumerate(threads, 1):
            open(os.path.join(pasta, f"thread{i:02d}.txt"), "w", encoding="utf-8").write(t["texto"].strip() + "\n")
        print(f"{len(threads)} posts de Threads gerados")

    for rede in ("linkedin", "instagram", "threads"):
        texto = post.get(f"legenda_{rede}")
        if texto:
            open(os.path.join(pasta, f"legenda-{rede}.txt"), "w", encoding="utf-8").write(texto.strip() + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
