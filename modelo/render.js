// Renderiza slide01.html ... slideNN.html em PNG 1080x1350.
// Uso: node render.js <pasta> <quantidade>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = process.argv[2], n = +process.argv[3];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let i = 1; i <= n; i++) {
    const nome = `slide${String(i).padStart(2, '0')}`;
    await p.goto('file://' + path.join(dir, `${nome}.html`));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(dir, `${nome}.png`) });
  }
  await b.close();
})();
