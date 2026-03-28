<div align="center">

# SocraTeX

### Socratic + LaTeX

**Estudia cualquier libro de matematicas con Claude.**

Introduce un PDF → Convierte a Markdown → Comienza un dialogo socratico.

---

[English](../README.md) | [한국어](README_ko.md) | [中文](README_zh.md) | [日本語](README_ja.md) | **Espanol**

</div>

---

## Que es SocraTeX?

Un sistema que convierte cualquier libro de texto de matematicas en una experiencia de estudio interactiva con Claude.

```
PDF  ──>  MinerU API  ──>  .md estructurado  ──>  Claude te ensena
                                                    (metodo socratico)
```

**No da respuestas directas.** Te guia con preguntas, pistas y contraejemplos hasta que descubras la solucion. Todas las formulas en LaTeX.

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
| `/latex [expr]` | Alternar LaTeX — explicar formula, copiar codigo fuente, convertir texto a LaTeX |
| `/translate [idioma]` | Traducir — preserva LaTeX, soporte bilingue configurable |
| `/btw [pregunta]` | Pregunta lateral — respuesta aislada via sub-agente, retoma el estudio automaticamente |
| `/settings [config]` | Configuracion — idioma, dificultad, anotaciones de terminos, numero de pistas |
| `/progress` | Seguimiento — capitulos cubiertos, areas debiles, siguientes recomendaciones |

---

## Inicio Rapido

### 1. Clonar & Instalar

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
pip install -r requirements.txt
```

### 2. Configurar Token de MinerU API

Obtener token en [mineru.net/apiManage](https://mineru.net/apiManage):

```bash
cp .env.example .env
# Editar .env y agregar MINERU_API_TOKEN
```

### 3. Convertir Libro de Texto

```bash
python -m converter libro.pdf
```

### 4. Empezar a Estudiar

**Claude Code (VS Code):**
```bash
cd SocraTeX
claude
/settings lang=es
/study ch01
```

**Claude.ai:**
1. Crear proyecto → subir archivos `.md` → pegar `system-prompt.md`
2. Escribir: "Estudiemos el capitulo 3"

---

## Modo Solo Skills (sin convertidor)

Ya tienes archivos `.md`? Usa **[SocraTeX Skills](https://github.com/Paul-JSN/SocraTeX-skills)** — version sin dependencias con solo los 15 comandos slash. Sin Python.

```bash
git clone https://github.com/Paul-JSN/SocraTeX-skills.git
cd SocraTeX-skills
# Coloca tus archivos .md en books/
claude
/study ch01
```

---

## Configuracion

```yaml
study_language: es
show_original_terms: true      # convergencia (convergence)
term_format: "translated (original)"
difficulty: adaptive
hints_before_answer: 3
```

---

## Licencia

**CC BY-NC-ND 4.0** — Uso libre. Sin uso comercial. Sin derivados.

