# Visualization Guide

Reference for `/visualize`. The page shell (tokens, full-bleed stage, title, status chip, dock, motion loop) comes from `example-epsilon-delta.html`; this file covers the stage.

## Pinned Libraries

Load only what the stage needs. Always Geist + Pretendard + KaTeX.

| Library | Tags |
|---|---|
| Geist | `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap">` |
| Pretendard | `<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">` |
| KaTeX 0.16.22 | `katex.min.css` + `katex.min.js`, tags copied from the example (with `integrity`) |
| JSXGraph 1.10.1 | `jsxgraph.css` + `jsxgraphcore.js`, tags copied from the example (with `integrity`) |
| Plotly 2.35.2 | `<script defer src="https://cdn.jsdelivr.net/npm/plotly.js-dist-min@2.35.2/plotly.min.js" integrity="sha384-cCVCZkAjYNxaYKbM8lsArLznDF/SvMFr1jcZrvOpSTCa0W40ZAdLzHCEulnUa5i7" crossorigin="anonymous"></script>` |
| three.js 0.160.0 | import map: `"three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"`, `"three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"` |

Use `defer` on classic scripts and start the page from `DOMContentLoaded`, as the example does. Every CDN script and stylesheet except Google Fonts and Pretendard carries its `integrity` hash and `crossorigin="anonymous"`.

## Which Stage for Which Topic

| Topic | Library | Stage |
|---|---|---|
| Limits, continuity, ε-δ, sequences | JSXGraph | bands drawn with `curve.updateDataArray` (see example) |
| Derivative, tangent vs secant, linear approximation | JSXGraph | glider point on the graph, `h` slider for the secant |
| Riemann sums, definite integral, FTC | JSXGraph | rectangles in one curve, `n` and left/mid/right controls |
| Taylor / Fourier / partial sums | JSXGraph | `functiongraph` whose function reads `target.n`; step `n` only through degrees that change the sum (odd degrees for $\sin$); status line = error at the chosen $x$ vs the remainder bound |
| 2×2 linear maps, eigenvectors, determinant | JSXGraph (`keepAspectRatio: true`) | transformed grid + unit square, draggable column vectors |
| Slope fields, phase portraits, ODE solutions | JSXGraph | arrow grid + draggable initial point, RK4 curve |
| Surfaces, tangent planes, contours, gradients, Lagrange | Plotly | `surface` + `contour`; update with `Plotly.react` |
| 3D linear maps, solids of revolution, parametric surfaces | three.js | `OrbitControls`, rebuild geometry on input |
| Complex functions | Canvas 2D | domain coloring with `ImageData` |
| Distributions, CLT, sampling, regression | Plotly | histogram + density line, resample button |
| Euclidean geometry, conics | JSXGraph | free points + constructions |

Colors: use the example's tokens (`--curve` for the main object, `--c1` `--c2` `--c3` for up to three parameters, matched to their sliders, and the unused ones for other marks on the stage; `--ok` and `--bad` for the chip and failure markers). Read them with `getComputedStyle(document.documentElement).getPropertyValue('--c1')` so light and dark mode both work. For Plotly set `paper_bgcolor` and `plot_bgcolor` to `'rgba(0,0,0,0)'`, `font.color` to `--muted`, and redraw from `view` inside the motion loop with `Plotly.react`.

## Recipes

**Riemann sum rectangles (JSXGraph)**

```js
const rects = board.create('curve', [[], []], { fillColor: css('--c2'), fillOpacity: 0.16, strokeColor: css('--c2'), strokeWidth: 1 });
rects.updateDataArray = function () {
  const { a, b, rule } = target, n = Math.max(1, Math.round(view.n)),   // view.n eases toward target.n w = (b - a) / n, X = [], Y = [];
  for (let i = 0; i < n; i++) {
    const x0 = a + i * w, xs = rule === 'left' ? x0 : rule === 'right' ? x0 + w : x0 + w / 2;
    X.push(x0, x0, x0 + w, x0 + w, NaN); Y.push(0, f(xs), f(xs), 0, NaN);   // NaN breaks the path between rectangles
  }
  this.dataX = X; this.dataY = Y;
};
```

**Tangent and secant (JSXGraph)**

```js
const graph = board.create('functiongraph', [f]);
const P = board.create('glider', [1, f(1), graph], { name: 'P' });
const Q = board.create('point', [() => P.X() + view.h, () => f(P.X() + view.h)], { name: 'Q' });   // view.h eases toward target.h
board.create('line', [P, Q], { strokeColor: css('--c1') });                       // secant
board.create('tangent', [P], { strokeColor: css('--c2'), dash: 2 });            // tangent
// status line: slope of PQ = (f(x+h) - f(x)) / h versus f'(x) from a central difference with tiny h
```

**Surface with tangent plane (Plotly)**

```js
const xs = linspace(-2, 2, 60), ys = linspace(-2, 2, 60);
const z = ys.map(y => xs.map(x => f(x, y)));
function draw() {
  const { x0, y0 } = view, z0 = f(x0, y0), fx = dfdx(x0, y0), fy = dfdy(x0, y0);
  const plane = ys.map(y => xs.map(x => z0 + fx * (x - x0) + fy * (y - y0)));
  Plotly.react('stage', [
    { type: 'surface', x: xs, y: ys, z, colorscale: 'Viridis', showscale: false, opacity: 0.95 },
    { type: 'surface', x: xs, y: ys, z: plane, colorscale: [[0, css('--c1')], [1, css('--c1')]], showscale: false, opacity: 0.45 },
    { type: 'scatter3d', mode: 'markers', x: [x0], y: [y0], z: [z0], marker: { size: 5, color: css('--bad') } },
  ], { margin: { l: 0, r: 0, t: 0, b: 0 }, paper_bgcolor: 'rgba(0,0,0,0)', scene: { aspectmode: 'cube' } }, { displaylogo: false, responsive: true });
}
```

Compute derivatives analytically when the textbook gives them; otherwise use a central difference with `h = 1e-5` and say so in the status line.

## Checklist Before Showing

- [ ] No console errors after load and after moving every control
- [ ] Status chip changes when a parameter changes, and its claim is true
- [ ] Main object draws in on load; parameter changes glide; nothing moves on its own
- [ ] Title, chip and dock do not cover axis labels or the figure
- [ ] Light and dark mode both readable
- [ ] Layout works at 375px width (cards stack)
- [ ] All UI text in `study_language`; all math in KaTeX
