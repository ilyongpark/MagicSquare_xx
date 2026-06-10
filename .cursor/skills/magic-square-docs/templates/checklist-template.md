# MagicSquare_xx — {세션 주제} 체크리스트

| 항목 | 내용 |
|------|------|
| NN | {NN} |
| Test ID | {D-* / U-*} |
| Track | {Logic / UI} |
| 날짜 | {YYYY-MM-DD} |

관련: [Report/{NN}.REPORT.md](../Report/{NN}.REPORT.md) · [Prompting/{NN}.Export-Transcript.md](../Prompting/{NN}.Export-Transcript.md)

---

## ARRR Command 체크리스트

| # | ARRR | Command | 완료 | 비고 |
|---|------|---------|:----:|------|
| 1 | **A**sk | `/red-test-plan` | ☐ | C2C 4블록, 파일 없음 |
| 2 | **R**espond | `/red-skeleton` | ☐ | tests/ only, pytest FAIL |
| 3 | **R**efine | `/green-minimal` | ☐ | src/ 최소, pytest PASS |
| 4 | **R**efine+ | `/golden-master` | ☐ | golden matched |
| 5 | **R**eview | `/refactor-smell` | ☐ | 스멜 표, 수정 없음 |
| 6 | **R**eview+ | `/refactor-safe` | ☐ | 기법 1개, PASS 유지 |
| 7 | — | `/export-session` | ☐ | Report + Transcript |

---

## TDD · ECB 체크리스트

| # | 항목 | 완료 | 비고 |
|---|------|:----:|------|
| C1 | Phase 선언 (첫 줄) | ☐ | |
| C2 | 10선 R1~R4·C1~C4·D1·D2 | ☐ | Mom Test |
| C3 | Logic Track Domain Mock 없음 | ☐ | |
| C4 | entity E001~E005 emit 없음 | ☐ | |
| C5 | MagicConstant SSOT (34/16/4/0) | ☐ | |
| C6 | skip / xfail 없음 | ☐ | |
| C7 | `python -m pytest` (세션 종료 시) | ☐ | |

---

## Test ID 진행 (reference.md)

| Test ID | RED | GREEN | Golden | REFACTOR |
|---------|:---:|:-----:|:------:|:--------:|
| {D-LOC-01} | ☐ | ☐ | ☐ | ☐ |
| {다음 ID} | ☐ | ☐ | ☐ | ☐ |

---

## 세션 완료 기준

- [ ] ARRR 1~7 중 해당 단계 완료
- [ ] Report/{NN}.REPORT.md 생성
- [ ] Prompting/{NN}.Export-Transcript.md 생성
- [ ] git commit은 사용자 요청 시에만

---

*본 문서는 Report/{NN}.CHECKLIST.md — {세션 주제} 체크리스트입니다.*
