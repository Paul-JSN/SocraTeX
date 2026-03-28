<div align="center">

# SocraTeX

### Socratic + LaTeX

**用 Claude 学习任何数学教材。**

投入 PDF → 转换为 Markdown → 开始苏格拉底式对话。

---

[English](../README.md) | [한국어](README_ko.md) | **中文** | [日本語](README_ja.md) | [Espanol](README_es.md)

</div>

---

## SocraTeX 是什么?

将任何数学教材 PDF 转化为 Claude 驱动的互动学习系统。

```
PDF  ──>  MinerU API  ──>  结构化 .md  ──>  Claude 引导学习
                                              (苏格拉底式对话法)
```

**不直接给答案。** 通过提问、提示和反例，引导你自己发现解答。所有数学公式以 LaTeX 呈现。

---

## 主要功能

| 命令 | 说明 |
|------|------|
| `/study [章节]` | 苏格拉底式学习 — 通过提问引导理解定义和定理 |
| `/exercise [主题]` | 练习题 — 逐步提示，跟踪尝试次数，生成类似题目 |
| `/exam-prep [范围]` | 考试准备 — 公式速查、定理总结、必做题、证明策略、常见错误、概念图 |
| `/mock-test [范围]` | 模拟考试 — 难度分布 30/50/20，含分值和时间分配 |
| `/study-guide [范围]` | 学习指南 — 概念层次、章节摘要、公式表、学习顺序 |
| `/review-test [文件]` | 复习分析 — 预测考试题型，找出覆盖缺口，生成针对性练习 |
| `/latex [表达式]` | LaTeX 切换 — 公式解释、源码复制、文字转 LaTeX |
| `/translate [语言]` | 翻译 — 保留 LaTeX，支持双语术语显示 |
| `/btw [问题]` | 旁问 — 通过子代理隔离回答，自动恢复学习流程 |
| `/settings [设置]` | 配置 — 语言、难度、术语标注、提示次数 |
| `/progress` | 进度追踪 — 已学章节、薄弱环节、下一步建议 |

---

## 快速开始

### 1. 克隆 & 安装

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
pip install -r requirements.txt
```

### 2. 设置 MinerU API 令牌

在 [mineru.net/apiManage](https://mineru.net/apiManage) 获取令牌:

```bash
cp .env.example .env
# 编辑 .env，填入 MINERU_API_TOKEN
```

### 3. 转换教材

```bash
python -m converter 教材路径.pdf
```

### 4. 开始学习

**Claude Code (VS Code):**
```bash
cd SocraTeX
claude
/settings lang=zh
/study ch01
```

**Claude.ai:**
1. 创建项目 → 上传 `.md` 文件 → 粘贴 `system-prompt.md`
2. 输入: "开始学习第3章"

---

## 仅技能模式 (无需转换器)

已有 `.md` 文件？使用 **[SocraTeX Skills](https://github.com/Paul-JSN/SocraTeX-skills)** — 零依赖版本，仅包含 15 个斜杠命令。无需 Python。

```bash
git clone https://github.com/Paul-JSN/SocraTeX-skills.git
cd SocraTeX-skills
# 将 .md 文件放入 books/ 目录
claude
/study ch01
```

---

## 配置

```yaml
study_language: zh
show_original_terms: true      # 收敛 (convergence)
term_format: "translated (original)"
difficulty: adaptive
hints_before_answer: 3
```

---

## 许可证

**CC BY-NC-ND 4.0** — 可自由使用，禁止商用，禁止修改分发。

