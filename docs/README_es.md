<div align="center">

# SocraTeX

### Socratic + LaTeX

**Estudia cualquier libro de matematicas con Claude.**

Solo necesitas archivos `.md`. Dialogo socratico con todas las formulas en LaTeX.

---

[English](../README.md) | [한국어](README_ko.md) | [中文](README_zh.md) | [日本語](README_ja.md) | **Espanol**

</div>

---

## Que es SocraTeX?

15 comandos slash que convierten a Claude en un tutor matematico socratico. Sin instalacion, sin dependencias — solo archivos Markdown.

**No da respuestas directas.** Te guia con preguntas, pistas y contraejemplos hasta que descubras la solucion.

> **Tienes un PDF?** Usa [MinerU](https://mineru.net) (modo Precision, modelo `vlm`) para convertir a Markdown. Gratis.

---

## Funciones Principales

| Comando | Descripcion |
|---------|------------|
| `/study [capitulo]` | Estudio socratico — guia por definiciones y teoremas con preguntas |
| `/exercise [tema]` | Ejercicios — pistas incrementales, seguimiento de intentos, genera problemas similares |
| `/exam-prep [rango]` | Preparacion de examen — formulas, resumen de teoremas, ejercicios clave, estrategias de prueba, errores comunes, mapa conceptual |
| `/mock-test [rango]` | Examen simulado — distribucion de dificultad 30/50/20, con puntajes y tiempo |
| `/study-guide [rango]` | Guia de estudio — jerarquia de conceptos, resumenes, hoja de formulas, orden de estudio |
| `/review-test [archivo]` | Analisis de repaso — predice patrones del examen, encuentra brechas, genera practica dirigida |
| `/proof [teorema]` | Modo prueba — escribe tu prueba linea por linea, Claude verifica la logica |
| `/compare [A vs B]` | Comparacion — definiciones, diferencias, similitudes, contraejemplos |
| `/visualize [concepto]` | Visualizacion ASCII — graficas, diagramas de conjuntos, epsilon-delta |
| `/quiz [rango]` | Quiz rapido 10 preguntas — V/F, completar, emparejar definiciones |
| `/latex [expr]` | Alternar LaTeX — explicar formula, copiar codigo fuente, convertir texto a LaTeX |
| `/translate [idioma]` | Traducir — preserva LaTeX, soporte bilingue configurable |
| `/sideq [pregunta]` | Pregunta lateral — respuesta aislada via sub-agente, retoma el estudio automaticamente |
| `/settings [config]` | Configuracion — idioma, dificultad, anotaciones de terminos, numero de pistas |
| `/progress` | Seguimiento — capitulos cubiertos, areas debiles, siguientes recomendaciones |

---

## Instalacion

### Claude Code

```
/install github:Paul-JSN/SocraTeX
```

### Codex

```
Fetch and follow instructions from https://raw.githubusercontent.com/Paul-JSN/SocraTeX/refs/heads/main/.codex/INSTALL.md
```

Empieza a estudiar:

```
/study ch01
```

---

## Inicio Rapido (manual)

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
mkdir -p books/my-textbook
# Coloca tus archivos .md en books/my-textbook/
```

> **Convertir PDF?** Recomendamos [MinerU](https://mineru.net) — gratis, preserva LaTeX.

```bash
claude
/settings lang=es
/study ch01
```

---

## Configuracion

```yaml
study_language: es
show_original_terms: true      # convergencia (convergence)
term_format: "translated (original)"
render_mode: desktop
difficulty: adaptive
hints_before_answer: 3
```

---

## Licencia

**CC BY-NC-ND 4.0** — Uso libre. Sin uso comercial. Sin derivados.
