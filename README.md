<div align="center">

# Socratex

### Socratic + LaTeX

**Study any math textbook with Claude.**

Drop a PDF. Get structured Markdown. Start a Socratic dialogue.

[English](#english) | [한국어](#한국어) | [中文](#中文) | [日本語](#日本語) | [Espanol](#español)

---

<img src="https://img.shields.io/badge/license-CC--BY--NC--ND--4.0-blue" alt="License" />
<img src="https://img.shields.io/badge/python-3.10+-yellow" alt="Python" />
<img src="https://img.shields.io/badge/platform-Claude_Code_%7C_Claude.ai-blueviolet" alt="Platform" />

</div>

---

<a name="english"></a>

## What is Socratex?

Socratex turns any math textbook PDF into an interactive study system powered by Claude.

```
PDF  -->  MinerU API  -->  Structured .md  -->  Claude teaches you
                                                 (Socratic method)
```

**No direct answers.** Claude guides you with questions, hints, and counterexamples until you discover the solution yourself. All math is rendered in beautiful LaTeX.

## Features

| Command | Description |
|---------|-------------|
| `/study [chapter]` | Socratic walkthrough of any chapter |
| `/exercise [topic]` | Guided practice with incremental hints |
| `/exam-prep [range]` | Formula sheets, theorem summaries, must-do exercises |
| `/mock-test [range]` | Timed practice exams with hidden solutions |
| `/study-guide [range]` | Structured overview with study order |
| `/review-test [file]` | Analyze review tests, predict exam patterns |
| `/latex [expr]` | Toggle between LaTeX source and explanation |
| `/translate [lang]` | Translate content, preserve all math notation |
| `/btw [question]` | Side questions without breaking study flow |
| `/settings [k=v]` | Configure language, difficulty, term display |
| `/progress` | Track what you've covered and what's next |

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/your-username/socratex.git
cd socratex
pip install -r requirements.txt
```

### 2. Set Up MinerU API Token

Get your token at [mineru.net/apiManage](https://mineru.net/apiManage), then:

```bash
cp .env.example .env
# Edit .env and add your MINERU_API_TOKEN
```

### 3. Convert Your Textbook

```bash
python -m converter path/to/textbook.pdf
```

This creates structured chapter files in `books/your-textbook/`.

### 4. Start Studying

**Option A: Claude Code (VS Code)**
```bash
cd socratex
claude   # or open in VS Code with Claude Code extension
/study ch01
```

Open `session.md` in VS Code's Markdown Preview for rendered LaTeX.

**Option B: Claude.ai**
1. Create a Project on claude.ai
2. Upload the `.md` files from `books/` to Project Knowledge
3. Copy `claude-ai/system-prompt.md` into Custom Instructions
4. Start chatting: "Let's study chapter 3"

### 5. Install Globally (Optional)

```bash
# macOS/Linux
./install.sh

# Windows
./install.ps1
```

Now use `/socratex:study`, `/socratex:exercise`, etc. from any directory.

## How It Works

```
┌──────────────────────────────────────────────────┐
│ VS Code                                          │
│ ┌─────────────────┐  ┌────────────────────────┐  │
│ │  Claude Code    │  │  Markdown Preview      │  │
│ │                 │  │  (session.md)          │  │
│ │  > /study ch03  │  │                        │  │
│ │                 │  │  § 3.1 Convergence     │  │
│ │  What do you    │  │                        │  │
│ │  think this ε   │  │  ∀ε>0, ∃N∈ℕ s.t.      │  │
│ │  condition      │  │  n≥N ⟹ |aₙ-L| < ε   │  │
│ │  means?         │  │                        │  │
│ └─────────────────┘  └────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

- **Left panel**: Conversation with Claude (Socratic dialogue)
- **Right panel**: Rendered LaTeX in real-time via `session.md`

## Configuration

Edit `socratex.config.md` or use `/settings`:

```yaml
study_language: en           # Any language (en, ko, ja, zh, es, fr, de, ...)
show_original_terms: false   # Show original English terms alongside translations
term_format: "translated (original)"  # How to display bilingual terms
difficulty: adaptive         # easy | medium | hard | adaptive
hints_before_answer: 3       # Minimum hints before revealing solutions
```

## Requirements

- Python 3.10+
- [MinerU API token](https://mineru.net/apiManage) (free tier available)
- Claude Code or Claude.ai account
- VS Code + [Markdown+Math extension](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath) (recommended for LaTeX rendering)

---

<a name="한국어"></a>

## 한국어

### Socratex가 뭔가요?

수학 교재 PDF를 Claude와 함께 공부하는 시스템입니다. PDF를 넣으면 자동으로 Markdown으로 변환하고, Claude가 소크라테스식 문답법으로 가르쳐줍니다.

**답을 바로 주지 않습니다.** 질문, 힌트, 반례를 통해 스스로 답을 발견하도록 유도합니다. 모든 수식은 LaTeX로 표시됩니다.

### 빠른 시작

```bash
git clone https://github.com/your-username/socratex.git
cd socratex
pip install -r requirements.txt
cp .env.example .env          # MinerU API 토큰 입력
python -m converter 교재.pdf   # PDF 변환
```

**Claude Code에서:**
```
/study ch01           # 1장 공부 시작
/exercise 수렴        # 수렴 관련 연습문제
/exam-prep ch1-ch5    # 중간고사 대비
/settings lang=ko     # 한국어로 설정
```

**Claude.ai에서:**
1. 프로젝트 생성 → `.md` 파일 업로드 → `system-prompt.md` 적용
2. "3장 공부하자", "연습문제 내줘", "시험 대비 해줘" 등 자연어로 사용

### 주요 기능

- `/exam-prep` — 공식 치트시트, 정리 요약, 필수 문제, 증명 전략, 흔한 실수, 개념 관계도
- `/mock-test` — 모의 시험 생성 (풀이 숨김)
- `/review-test` — 리뷰 테스트 분석 → 시험 유형 예측
- `/btw` — 흐름 끊지 않고 딴 질문하기
- `/settings terms=on format="translated (original)"` — 수렴 (convergence) 형태로 표시

---

<a name="中文"></a>

## 中文

### Socratex 是什么?

将任何数学教材 PDF 转化为与 Claude 互动的学习系统。投入 PDF，自动转换为 Markdown，Claude 以苏格拉底式对话法引导学习。

**不直接给答案。** 通过提问、提示和反例引导你自己发现解答。所有数学公式以 LaTeX 呈现。

### 快速开始

```bash
git clone https://github.com/your-username/socratex.git
cd socratex
pip install -r requirements.txt
cp .env.example .env            # 填入 MinerU API token
python -m converter 教材.pdf     # 转换 PDF
```

**在 Claude Code 中:**
```
/study ch01           # 开始学习第1章
/exercise 收敛        # 收敛相关练习题
/exam-prep ch1-ch5    # 期中考试准备
/settings lang=zh     # 设置为中文
```

### 主要功能

- `/exam-prep` — 公式速查表、定理总结、必做习题、证明策略、常见错误、概念图
- `/mock-test` — 生成模拟考试
- `/review-test` — 分析复习测试，预测考试题型
- `/btw` — 不打断学习流的旁问
- `/settings terms=on` — 显示双语术语，如：收敛 (convergence)

---

<a name="日本語"></a>

## 日本語

### Socratex とは?

数学の教科書 PDF を Claude と一緒に勉強するシステムです。PDF を投入すると自動で Markdown に変換し、Claude がソクラテス式対話法で教えます。

**直接答えは教えません。** 質問、ヒント、反例を通じて自分で答えを発見できるよう導きます。すべての数式は LaTeX で表示されます。

### クイックスタート

```bash
git clone https://github.com/your-username/socratex.git
cd socratex
pip install -r requirements.txt
cp .env.example .env              # MinerU API トークンを入力
python -m converter textbook.pdf   # PDF 変換
```

**Claude Code で:**
```
/study ch01           # 第1章の学習開始
/exercise 収束        # 収束に関する練習問題
/exam-prep ch1-ch5    # 中間試験対策
/settings lang=ja     # 日本語に設定
```

### 主な機能

- `/exam-prep` — 公式チートシート、定理要約、必須問題、証明戦略、よくある間違い
- `/mock-test` — 模擬試験の生成
- `/btw` — 学習の流れを止めずにサイド質問

---

<a name="español"></a>

## Espanol

### Que es Socratex?

Un sistema para estudiar cualquier libro de texto de matematicas con Claude. Introduce un PDF, se convierte automaticamente a Markdown, y Claude te ensena con el metodo socratico.

**No da respuestas directas.** Te guia con preguntas, pistas y contraejemplos hasta que descubras la solucion. Todas las formulas en LaTeX.

### Inicio Rapido

```bash
git clone https://github.com/your-username/socratex.git
cd socratex
pip install -r requirements.txt
cp .env.example .env                # Agrega tu token de MinerU API
python -m converter libro.pdf        # Convierte el PDF
```

**En Claude Code:**
```
/study ch01           # Estudiar capitulo 1
/exercise limites     # Ejercicios sobre limites
/exam-prep ch1-ch5    # Preparacion para examen parcial
/settings lang=es     # Configurar en espanol
```

---

<div align="center">

## License

CC BY-NC-ND 4.0 — Free to use, no commercial use or derivatives.

Built with [Claude](https://claude.ai) + [MinerU](https://mineru.net)

</div>
