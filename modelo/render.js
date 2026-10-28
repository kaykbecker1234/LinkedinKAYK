// Renderiza <prefixo>01.html ... <prefixo>NN.html em PNG.
// Uso: node render.js <pasta> <quantidade> [prefixo=slide] [largura=1080] [altura=1350]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [dir, nStr, prefix = 'slide', w = '1080', h = '1350'] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  for (let i = 1; i <= +nStr; i++) {
    const nome = `${prefix}${String(i).padStart(2, '0')}`;
    await p.goto('file://' + path.join(dir, `${nome}.html`));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(dir, `${nome}.png`) });
  }
  await b.close();
})();
