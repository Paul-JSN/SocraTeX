<div align="center">

# SocraTeX

### Socratic + LaTeX

**어떤 수학 교재든, Claude와 함께 공부하세요.**

`.md` 파일만 있으면 바로 소크라테스식 문답 시작. 모든 수식은 LaTeX.

---

[English](../README.md) | **한국어** | [中文](README_zh.md) | [日本語](README_ja.md) | [Espanol](README_es.md)

</div>

---

## SocraTeX가 뭔가요?

15개 슬래시 커맨드로 Claude를 소크라테스식 수학 튜터로 만듭니다. 설치 필요 없음, 의존성 없음 — Markdown 파일만 있으면 됩니다.

**답을 바로 주지 않습니다.** 질문, 힌트, 반례를 통해 스스로 답을 발견하도록 유도합니다. 모든 수식은 LaTeX로 표시됩니다.

> **PDF가 있다면?** [MinerU](https://mineru.net) (Precision 모드, `vlm` 모델)로 PDF를 Markdown으로 변환하세요. 무료 플랜 있음.

---

## 주요 기능

| 커맨드 | 설명 |
|--------|------|
| `/study [챕터]` | 소크라테스식 학습 — 정의/정리를 질문으로 유도, 답 직접 안 줌 |
| `/exercise [주제]` | 연습문제 — 단계별 힌트, 시도 횟수 추적, 유사 문제 생성 |
| `/exam-prep [범위]` | 시험 대비 — 공식 치트시트, 정리 요약, 필수 문제, 증명 전략, 흔한 실수, 개념도 |
| `/mock-test [범위]` | 모의고사 — 난이도 분포(쉬움 30% / 보통 50% / 어려움 20%), 풀이 숨김 |
| `/study-guide [범위]` | 스터디 가이드 — 개념 계층, 섹션 요약, 공식 시트, 추천 공부 순서 |
| `/review-test [파일]` | 리뷰 분석 — 시험 패턴 예측, 빈틈 찾기, 맞춤 연습문제 생성 |
| `/proof [정리]` | 증명 모드 — 한 줄씩 증명 작성, Claude가 논리 검증 |
| `/compare [A vs B]` | 비교 — 정의, 차이점, 유사점, 반례 |
| `/visualize [개념]` | ASCII 시각화 — 함수 그래프, 집합 다이어그램, 입실론-델타 |
| `/quiz [범위]` | 퀴즈 10문제 — 참/거짓, 빈칸 채우기, 정의 매칭 |
| `/latex [수식]` | LaTeX 토글 — 수식 설명, 소스코드 복사, 텍스트→LaTeX 변환 |
| `/translate [언어]` | 번역 — LaTeX 보존, 원어 병기 설정 가능 |
| `/btw [질문]` | 딴 질문 — sub-agent로 격리 답변, 자동으로 학습 재개 |
| `/settings [설정]` | 설정 변경 — 언어, 난이도, 원어 병기, 힌트 수, 렌더 모드 |
| `/progress` | 진도 확인 — 공부한 챕터, 약한 부분, 다음 추천 |

---

## 빠른 시작

### 1. 클론

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
```

### 2. 교재 파일 넣기

```bash
mkdir -p books/my-textbook
# .md 파일을 여기에 넣기
```

> **PDF 변환?** [MinerU](https://mineru.net) 추천 — 무료, LaTeX 보존, 깔끔한 Markdown 출력.

### 3. 공부 시작

<table>
<tr>
<th>Claude Code (VS Code) — 전체 기능</th>
<th>Claude.ai — 간편 사용</th>
</tr>
<tr>
<td>

```bash
claude
/settings lang=ko
/study ch01
```

VS Code Markdown Preview에서 `session.md` 열면 LaTeX 렌더링됨.

</td>
<td>

1. claude.ai에서 **프로젝트** 생성
2. `.md` 파일 → Project Knowledge에 업로드
3. `claude-ai/system-prompt.md` → Custom Instructions에 붙여넣기
4. "3장 공부하자" 라고 채팅

</td>
</tr>
</table>

### 4. 글로벌 설치 (선택)

```bash
./install.sh        # macOS / Linux
./install.ps1       # Windows (PowerShell)
```

---

## 설정

`socratex.config.md`를 직접 수정하거나 `/settings` 사용:

```yaml
study_language: ko            # 공부 언어
show_original_terms: true     # 원어 병기 (수렴 (convergence))
term_format: "translated (original)"
render_mode: desktop          # desktop | vscode
difficulty: adaptive          # easy | medium | hard | adaptive
hints_before_answer: 3        # 답 공개 전 최소 힌트 수
```

---

## 필수 요소

| 필요한 것 | 비고 |
|-----------|------|
| Claude Code 또는 Claude.ai | 아무 플랜 |
| `.md` 교재 파일 | LaTeX 포함 (`$...$`, `$$...$$`) |
| VS Code + [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath) | LaTeX 렌더링 추천 |

---

## 라이선스

**CC BY-NC-ND 4.0** — 사용 가능. 상업적 이용 불가. 수정 배포 불가.
