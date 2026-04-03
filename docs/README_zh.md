<div align="center">

# SocraTeX

### Socratic + LaTeX

**用 Claude 学习任何数学教材。**

只需 `.md` 文件，即可开始苏格拉底式对话。所有数学公式以 LaTeX 呈现。

---

[English](../README.md) | [한국어](README_ko.md) | **中文** | [日本語](README_ja.md) | [Espanol](README_es.md)

</div>

---

## SocraTeX 是什么?

15 个斜杠命令将 Claude 变成苏格拉底式数学导师。无需安装，无依赖 — 只需 Markdown 文件。

**不直接给答案。** 通过提问、提示和反例，引导你自己发现解答。

> **有 PDF？** 用 [MinerU](https://mineru.net)（Precision 模式，`vlm` 模型）转换为 Markdown。免费。

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
| `/proof [定理]` | 证明模式 — 逐行写证明，Claude 验证逻辑 |
| `/compare [A vs B]` | 概念对比 — 定义、差异、相似点、反例 |
| `/visualize [概念]` | ASCII 可视化 — 函数图、集合图、ε-δ 图示 |
| `/quiz [范围]` | 快速测验 10 题 — 判断、填空、定义匹配 |
| `/latex [表达式]` | LaTeX 切换 — 解释公式、源代码、文本转 LaTeX |
| `/translate [语言]` | 翻译 — 保留 LaTeX，可配置双语术语显示 |
| `/sideq [问题]` | 旁问 — 子代理隔离回答，自动恢复学习流程 |
| `/settings [设置]` | 配置 — 语言、难度、术语标注、提示次数 |
| `/progress` | 进度追踪 — 已学章节、薄弱环节、下一步建议 |

---

## 安装

### Claude Code

添加市场:

```
/plugin marketplace add Paul-JSN/SocraTeX
```

安装插件:

```
/plugin install SocraTeX@Paul-JSN
```

重新加载插件:

```
/reload-plugins
```

### Codex

```
Fetch and follow instructions from https://raw.githubusercontent.com/Paul-JSN/SocraTeX/refs/heads/main/.codex/INSTALL.md
```

开始学习:

```
/study ch01
```

---

## 配置

```yaml
study_language: zh
show_original_terms: true      # 收敛 (convergence)
term_format: "translated (original)"
render_mode: desktop
difficulty: adaptive
hints_before_answer: 3
```

---

## 许可证

**CC BY-NC-ND 4.0** — 可自由使用，禁止商用，禁止修改分发。
