<div align="center">

# SocraTeX

### Socratic + LaTeX

**どんな数学の教科書でも、Claude と一緒に勉強。**

`.md` ファイルがあればすぐソクラテス式対話が始まる。すべての数式は LaTeX。

---

[English](../README.md) | [한국어](README_ko.md) | [中文](README_zh.md) | **日本語** | [Espanol](README_es.md)

</div>

---

## SocraTeX とは?

15のスラッシュコマンドがClaudeをソクラテス式数学チューターに変えます。セットアップ不要、依存関係なし — Markdownファイルだけ。

**直接答えは教えません。** 質問、ヒント、反例を通じて、自分で答えを発見できるよう導きます。

> **PDFがある場合？** [MinerU](https://mineru.net)（Precisionモード、`vlm`モデル）でMarkdownに変換。無料プランあり。

---

## 主な機能

| コマンド | 説明 |
|---------|------|
| `/study [章]` | ソクラテス式学習 — 定義や定理を質問で導く |
| `/exercise [テーマ]` | 練習問題 — 段階的ヒント、試行回数追跡、類似問題生成 |
| `/exam-prep [範囲]` | 試験対策 — 公式チートシート、定理要約、必須問題、証明戦略、よくある間違い、概念図 |
| `/mock-test [範囲]` | 模擬試験 — 難易度分布 30/50/20、配点、時間配分付き |
| `/study-guide [範囲]` | 学習ガイド — 概念階層、セクション要約、公式シート、学習順序 |
| `/review-test [ファイル]` | 復習分析 — 試験パターン予測、カバレッジギャップ発見 |
| `/proof [定理]` | 証明モード — 一行ずつ証明、Claudeが論理検証 |
| `/compare [A vs B]` | 比較 — 定義、違い、類似点、反例 |
| `/visualize [概念]` | ASCII可視化 — 関数グラフ、集合図、ε-δ図示 |
| `/quiz [範囲]` | クイズ10問 — 正誤、穴埋め、定義マッチング |
| `/latex [式]` | LaTeX切替 — 数式説明、ソースコード、テキスト→LaTeX |
| `/translate [言語]` | 翻訳 — LaTeX保持、バイリンガル用語表示設定可能 |
| `/btw [質問]` | サイド質問 — サブエージェントで隔離回答、学習フロー自動復帰 |
| `/settings [設定]` | 設定 — 言語、難易度、用語注釈、ヒント回数 |
| `/progress` | 進捗確認 — 学習済み章、弱点、次の推奨内容 |

---

## クイックスタート

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
mkdir -p books/my-textbook
# .md ファイルを books/my-textbook/ に配置
```

> **PDF変換？** [MinerU](https://mineru.net) 推奨 — 無料、LaTeX保持。

```bash
claude
/settings lang=ja
/study ch01
```

---

## 設定

```yaml
study_language: ja
show_original_terms: true      # 収束 (convergence)
term_format: "translated (original)"
render_mode: desktop
difficulty: adaptive
hints_before_answer: 3
```

---

## ライセンス

**CC BY-NC-ND 4.0** — 自由に使用可能。商用利用・改変配布は不可。
