---
name: magic-square-tdd
description: MagicSquare_xx Dual-Track TDD·ECB·ARRR 개발 절차. TDD, RED/GREEN/REFACTOR, /red-test-plan, entity/control/boundary, D-*/U-*, validate_lines, 마방진 34, ECB, MagicConstant SSOT 작업 시 사용.
---

# MagicSquare_xx — Dual-Track TDD Skill

## 언제 이 Skill을 켜는가

다음 **하나 이상**에 해당하면 본 Skill을 적용한다.

- `src/entity`, `src/control`, `src/boundary` 또는 `tests/**` 코드·테스트를 **작성·수정**할 때
- 사용자가 **TDD**, **ARRR**, **RED/GREEN/REFACTOR**, **D-***, **U-***, **ECB**, **Dual-Track**을 언급할 때
- Slash Command: `/red-test-plan`, `/red-skeleton`, `/green-minimal`, `/golden-master`, `/refactor-smell`, `/refactor-safe`
- `validate_lines`, 마방합 34, 빈칸 2개, `int[6]` 출력, `E001`~`E007` 관련 작업 시

**켜지 않는 경우:** Report·Prompting만 수정, git만, Harness 골격 외 문서-only (`magic-square-docs` Skill 사용).

**시작 시 SSOT:** `.cursorrules` → `docs/PRD.md` → [reference.md](reference.md) → `docs/TODO.md`(있으면).

---

## ARRR ↔ Command ↔ TDD

| ARRR | Phase | Command | 산출 |
|------|-------|---------|------|
| **A**sk | RED ③ | `/red-test-plan` | C2C 설계표·테스트 플랜 (파일 없음) |
| **R**espond | RED ④ | `/red-skeleton` | `tests/` pytest.fail 스켈레톤 |
| **R**efine | GREEN | `/green-minimal` | `src/` 최소 구현 + assert |
| **R**efine+ | GREEN | `/golden-master` | `tests/golden/`, `_approval.py` |
| **R**eview | REFACTOR | `/refactor-smell` | 스멜 표 (읽기 전용) |
| **R**eview+ | REFACTOR | `/refactor-safe` | 기법 1개, pytest PASS 유지 |

모든 Command는 **슬래시명만**으로 동작 — 추가 질문 금지.

---

## 턴 선언 (매 응답 필수)

```
Phase: red | green | refactor
Layer: entity | control | boundary
Track: Logic (D-*) | UI (U-*)
```

(선택) `Mode: Golden Master | smell-analysis | safe-apply`

---

## Logic Track vs UI Track

| | **Logic Track (B)** | **UI Track (A)** |
|---|---------------------|------------------|
| **Layer** | entity, control | boundary |
| **테스트 ID** | `D-*` | `U-*` |
| **파일** | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` | `tests/boundary/test_u_*.py` |
| **Mock** | **Domain Mock 금지** | I/O·control **Mock 허용** |
| **순서** | entity → control 먼저 | Logic GREEN 후 |
| **ECB import** | control→entity만 | boundary→control만 |

---

## ECB · Mock · 오류 코드

| 규칙 | entity | control | boundary |
|------|--------|---------|----------|
| import 방향 | **→ \* 금지** | entity만 | control만 |
| `E001`~`E005` | **처리 금지** | 변환·위임만 | 정의·발생·매핑 |
| `E006`~`E007` | — | — | boundary 전담 |
| Domain Mock | **금지** | **금지** | — |
| I/O Mock | — | — | **허용** |
| MagicConstant | `entity/constants.py` SSOT | SSOT import | SSOT import |

**Boundary API (`.cursorrules`):**

```python
validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": [...]}
```

- 10선: R1~R4, C1~C4, D1, D2 — 마법상수 **34**
- Mom Test: 대각선 누락·원인 확인 비용 — D1/D2 케이스 우선

---

## Phase: RED (ARRR Ask + Respond)

### Ask — `/red-test-plan`

- C2C Rule1~3, FR 인용, Track B/A 설계표, 테스트 플랜, ECB 점검
- `tests/`·`src/` **생성 금지**

### Respond — `/red-skeleton`

1. Test ID·파일·픽스처 확정
2. AAA + `pytest.fail("RED: …")` 한 줄
3. pytest **FAIL** 확인
4. `src/` 도메인 구현 **금지** (constants SSOT만 예외)

---

## Phase: GREEN (ARRR Refine)

### `/green-minimal`

1. RED FAIL 재확인
2. assert만 통과하는 **최소** `src/` 구현
3. `pytest.fail` → 실제 assert
4. 대상·파일 pytest **PASS**
5. (선택) REPL 스모크

### `/golden-master` (PASS 후)

1. `_approval.py` + `tests/golden/*.approved.txt`
2. `UPDATE_GOLDEN=1`로 기준 생성 → 일반 실행 matched
3. int[6] 1-index, ERROR 포맷 고정

---

## Phase: REFACTOR (ARRR Review)

### `/refactor-smell`

- 코드 읽기만, 우선순위 내림차순 스멜 표
- 수정 **금지**

### `/refactor-safe`

- 상위 스멜 **1건**, 기법 **1개**
- REFACTOR 전·후 pytest **전부 PASS**

---

## Test / Review Loop

| 시점 | 명령 | 기대 |
|------|------|------|
| RED ④ 후 | `pytest <파일>::<함수> -v` | **FAIL** |
| GREEN 후 | 동일 | **PASS** |
| Golden 검증 | `pytest …` (UPDATE_GOLDEN 없음) | matched |
| REFACTOR 후 | `python -m pytest tests/ -v` | **전부 PASS** |
| Logic 완료 | `pytest tests/entity/ tests/control/ -v` | 전부 PASS |
| 세션 종료 | `python -m pytest` | 전체 PASS |

**금지:** skip, xfail, assert 완화, `-x`로 실패 숨기기.

---

## 완료 보고 항목

- [ ] **Phase / Layer / Track / Test ID**
- [ ] **변경 파일** (`src/…`, `tests/…`)
- [ ] **pytest** 명령 + passed/failed
- [ ] **ECB** — entity→\* 없음, E001~E005 entity 미사용
- [ ] **Mock** — Logic Track Domain Mock 없음
- [ ] **MagicConstant** — 리터럴 34/16/4/0 산재 없음
- [ ] **다음 Command** — ARRR 체인 다음 단계

---

## 추가 참고

- D-*/U-* ID: [reference.md](reference.md)
- 세션 문서: `.cursor/skills/magic-square-docs/SKILL.md`
- git commit: **사용자 요청 시에만**
