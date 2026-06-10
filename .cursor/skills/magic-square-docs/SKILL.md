---
name: magic-square-docs
description: MagicSquare_xx 세션 보고서·Transcript·체크리스트 문서 생성. Report/, Prompting/ Export, /export-session, ARRR 세션 마무리, STEP 보고 시 사용.
---

# MagicSquare_xx — Session Docs Skill

## 언제 이 Skill을 켜는가

- `/export-session` 또는 `/export` 호출 시
- ARRR·TDD 세션 **마무리** 보고서 요청 시
- `Report/NN.REPORT.md`, `Prompting/NN.Export-Transcript.md` 생성 시
- STEP 체크리스트·세션 요약 작성 시

**켜지 않는 경우:** `src/`·`tests/` 구현 (`magic-square-tdd` Skill).

---

## SSOT

| 출처 | 용도 |
|------|------|
| `.cursor/commands/export-session.md` | 번호 규칙·파일 쌍·금지 |
| `.cursorrules` | 프로젝트 맥락 |
| `docs/PRD.md` | FR·단계 |
| 현재 채팅 전체 | Transcript 원문 |

---

## 번호 규칙

1. `Report/`, `Prompting/`의 기존 `NN.*` 확인
2. 최대 번호 + 1 (2자리: `01`, `02`, …)
3. 기존 파일 **덮어쓰기 금지**

---

## 생성 파일 (반드시 2개 + 선택 1개)

| 파일 | 템플릿 |
|------|--------|
| `Report/NN.REPORT.md` | [templates/report-template.md](templates/report-template.md) |
| `Prompting/NN.Export-Transcript.md` | [templates/transcript-template.md](templates/transcript-template.md) |
| (선택) `Report/NN.CHECKLIST.md` | [templates/checklist-template.md](templates/checklist-template.md) |

ARRR 세션 시 체크리스트 포함 권장.

---

## 자동 추출 (추가 질문 금지)

| 항목 | 추출 |
|------|------|
| 세션 주제 | 채팅 핵심 (예: D-LOC-01 GREEN, ARRR Command 작성) |
| Phase/Track | 최근 Command·Skill 선언 |
| Test ID | PASS/FAIL/RED 대상 |
| 산출물 | 생성·수정 파일 목록 |
| pytest | 실행했으면 명령·결과 |
| Transcript | User/Cursor 턴 **전문** (요약 아님) |

---

## 절차

1. 다음 NN 결정
2. 템플릿 3종 중 필요한 파일 **직접 생성**
3. 상호 링크: Report ↔ Prompting
4. 짧게 보고: 번호, 경로, 주제 한 줄

---

## ARRR 세션 보고 섹션 (Report에 포함)

| ARRR | Command | 완료 여부 |
|------|---------|-----------|
| Ask | `/red-test-plan` | ☐ |
| Respond | `/red-skeleton` | ☐ |
| Refine | `/green-minimal`, `/golden-master` | ☐ |
| Review | `/refactor-smell`, `/refactor-safe` | ☐ |

---

## 금지

- 사용자에게 주제·번호 **추가 질문**
- Report만 / Transcript만 생성
- `REPORT.md` 단독명 (번호 없음)
- 기존 NN 덮어쓰기

---

## 완료 보고

```
NN=05
Report/05.REPORT.md
Prompting/05.Export-Transcript.md
주제: (한 줄)
```
