"""Gera os slides de um post a partir de posts/<pasta>/post.json.

Uso: python3 modelo/gerar.py posts/<pasta>

post.json:
{
  "titulo": "Título do documento no LinkedIn",
  "css_extra": "",                       # opcional
  "slides": ["<html do slide 1>", ...],  # só o miolo; cabeçalho e rodapé são automáticos
  "legenda_linkedin": "...",
  "legenda_instagram": "...",
  "fontes": ["https://..."]
}

Saída na mesma pasta: slide01.png ... slideNN.png, carrossel.pdf,
legenda-linkedin.txt, legenda-instagram.txt
"""
import base64, json, os, subprocess, sys

from PIL import Image

NAME, HANDLE, ACC = "Kayk", "@kayk.ceo", "#C6FF3D"
HERE = os.path.dirname(os.path.abspath(__file__))


def main(pasta):
    pasta = os.path.abspath(pasta)
    post = json.load(open(os.path.join(pasta, "post.json"), encoding="utf-8"))
    css = open(os.path.join(HERE, "estilo.css"), encoding="utf-8").read().replace("ACC", ACC)
    css += post.get("css_extra", "")
    avatar = base64.b64encode(open(os.path.join(HERE, "avatar.jpg"), "rb").read()).decode()
    slides = post["slides"]
    total = len(slides)

    for i, body in enumerate(slides, 1):
        html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="head"><img class="av" src="data:image/jpeg;base64,{avatar}"><div><div class="n">{NAME}</div><div class="h">{HANDLE}</div></div></div>
{body}
<div class="foot"><div class="bar"><i style="width:{int(i / total * 100)}%"></i></div><div class="num">{i:02d}/{total:02d}</div></div>
</body></html>"""
        open(os.path.join(pasta, f"slide{i:02d}.html"), "w", encoding="utf-8").write(html)

    subprocess.run(["node", os.path.join(HERE, "render.js"), pasta, str(total)], check=True)

    pngs = [os.path.join(pasta, f"slide{i:02d}.png") for i in range(1, total + 1)]
    ims = [Image.open(p).convert("RGB") for p in pngs]
    ims[0].save(os.path.join(pasta, "carrossel.pdf"), save_all=True, append_images=ims[1:], resolution=150)

    for i in range(1, total + 1):
        os.remove(os.path.join(pasta, f"slide{i:02d}.html"))
    for rede in ("linkedin", "instagram"):
        texto = post.get(f"legenda_{rede}")
        if texto:
            open(os.path.join(pasta, f"legenda-{rede}.txt"), "w", encoding="utf-8").write(texto.strip() + "\n")
    print(f"{total} slides gerados em {pasta}")


if __name__ == "__main__":
    main(sys.argv[1])
