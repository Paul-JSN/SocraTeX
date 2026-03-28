<div align="center">

# SocraTeX

### Socratic + LaTeX

**どんな数学の教科書でも、Claude と一緒に勉強。**

PDF を入れる → Markdown に変換 → ソクラテス式対話が始まる。

---

[English](../README.md) | [한국어](README_ko.md) | [中文](README_zh.md) | **日本語** | [Espanol](README_es.md)

</div>

---

## SocraTeX とは?

数学の教科書 PDF を Claude で学ぶインタラクティブな学習システムです。

```
PDF  ──>  MinerU API  ──>  構造化 .md  ──>  Claude が教える
                                              (ソクラテス式対話法)
```

**直接答えは教えません。** 質問、ヒント、反例を通じて、自分で答えを発見できるよう導きます。すべての数式は LaTeX で表示されます。

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
| `/latex [式]` | LaTeX 切替 — 数式の説明、ソースコードコピー、テキスト→LaTeX変換 |
| `/translate [言語]` | 翻訳 — LaTeX 保持、バイリンガル用語表示対応 |
| `/btw [質問]` | サイド質問 — サブエージェントで隔離回答、学習フロー自動復帰 |
| `/settings [設定]` | 設定 — 言語、難易度、用語注釈、ヒント回数 |
| `/progress` | 進捗確認 — 学習済み章、弱点、次の推奨内容 |

---

## クイックスタート

### 1. クローン & インストール

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
pip install -r requirements.txt
```

### 2. MinerU API トークン設定

[mineru.net/apiManage](https://mineru.net/apiManage) でトークンを取得:

```bash
cp .env.example .env
# .env を編集して MINERU_API_TOKEN を入力
```

### 3. 教科書を変換

```bash
python -m converter textbook.pdf
```

### 4. 学習開始

**Claude Code (VS Code):**
```bash
cd SocraTeX
claude
/settings lang=ja
/study ch01
```

**Claude.ai:**
1. プロジェクト作成 → `.md` ファイルをアップロード → `system-prompt.md` を貼付
2. 「第3章を勉強しよう」と入力

---

## スキルのみモード (コンバーター不要)

すでに `.md` ファイルがある場合は **[SocraTeX Skills](https://github.com/Paul-JSN/SocraTeX-skills)** をご利用ください — Python不要、15のスラッシュコマンドのみの軽量版です。

```bash
git clone https://github.com/Paul-JSN/SocraTeX-skills.git
cd SocraTeX-skills
# .md ファイルを books/ に配置
claude
/study ch01
```

---

## 設定

```yaml
study_language: ja
show_original_terms: true      # 収束 (convergence)
term_format: "translated (original)"
difficulty: adaptive
hints_before_answer: 3
```

---

## ライセンス

**CC BY-NC-ND 4.0** — 自由に使用可能。商用利用・改変配布は不可。

