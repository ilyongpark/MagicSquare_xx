# MagicSquare_xx — PRD (Product Requirements Document)

## 1. 문서 개요

| 항목 | 내용 |
|------|------|
| 제품 | MagicSquare_xx |
| 버전 | **0.2** (ARRR·Dual-Track TDD 반영) |
| 기준 | Mom Test STEP 1 + 세션 3 워크북 + `.cursorrules` |
| SSOT 우선순위 | 본 문서 → `.cursorrules` → `.cursor/skills/magic-square-tdd/reference.md` |
| 목적 | 진짜 문제(10선 합 34 판정·원인 확인 비용) 해결을 위한 **최소 검증·판정 기능** 정의 |

### 변경 이력

| 버전 | 날짜 | 요약 |
|------|------|------|
| 0.1 | STEP 1~3 | `validate(grid) -> bool`, 세션 3 최소 범위 |
| 0.2 | ARRR 실습 | `validate_lines` API, ECB·Dual-Track, FR-LOC/SOL/VAL, D-*/U-* |

---

## 2. 배경 및 문제

### 페르소나

4×4 부분 마방진(빈칸 2개·`0`, 값 `1~16`, 마법합 34)을 손으로/코드로 다루는 **학습자**

### 진짜 문제 (한 문장)

4×4 부분 마방진에서 빈칸 2개를 채운 뒤 행·열·대각선 **10선** 합을 맞추는 과정에서 **검산 대상(대각선)을 빠뜨리거나** 틀린 원인을 바로 짚지 못해, 무엇이 문제인지 확인하는 데만 **20분 가까이 낭비**한다.

### Mom Test 증거

| # | 인용 | 유형 |
|---|------|------|
| 1 | “**지난 주**에 빈칸 2개 넣고 … **대각선 하나를 빼먹어서 20분 날렸다**.” | 과거 행동 + 비용 + 판정 누락 ✓ |
| 2 | “**20분 동안 무엇이 문제인지 확인**하다가 알았어.” | 판정·원인 추적 비용 ✓ |
| 3 | “4×4 부분 마방진을 손으로/코드로 다루는 **학습자**” | 페르소나 △ |

### 표면 문제 (Non-Goal)

> “4×4 부분 마방진을 Solver·Validator 프로그램으로 만들면, 빈 칸 2개를 빠르게 채우고 행·열·대각선 합 34를 맞출 수 있다.”

— **본 PRD의 목표가 아님** (솔루션 언어 혼입)

---

## 3. 제품 목표

### Goal

학습자가 빈칸 2개를 채운 4×4 격자에 대해, **10선(행 4 + 열 4 + 대각선 2) 합 34** 여부를 즉시 판정하고, 틀리면 **어느 줄**인지 짚을 수 있게 한다.

### Non-Goals (v0.2)

| 제외 | 이유 |
|------|------|
| Solver — 빈칸 자동 채우기 | 표면 문제 |
| MissingFinder — 빈칸 위치 탐색 | 증거와 무관 |
| GridUI / InputHandler / ResultDisplay | UI Track 이전 Logic 우선 |
| 힌트·자동 교정·“20분→1분” KPI | Mom Test 위반 |
| 완전한 ECB Boundary GUI | v0.2는 계약·로직 우선 |

---

## 4. R-G-I-O

| | 설명 |
|---|------|
| **Role** | 4×4 부분 마방진을 풀며 “행·열·대각선까지 다 34 맞나?”를 확인해야 하는 **학습자** |
| **Goal** | 10선 각각 합 34 충족 여부를 빠르게 알고, 틀리면 **어느 줄(R1~R4·C1~C4·D1·D2)** 인지 짚기 |
| **Input** | `grid: list[list[int]]` — 4×4, 값 `0`(빈칸) 또는 `1~16`, 빈칸 **정확히 2개** (boundary 유효 입력) |
| **Output (Boundary)** | `validate_lines(grid) -> {"status", "failed_lines"}` |
| **Output (확장)** | `int[6]` → `[r1, c1, n1, r2, c2, n2]` — 빈칸 2곳 **1-index** 좌표와 채울 값 (Solver 단계, v0.3+) |

---

## 5. 도메인 규칙 (Rule)

| ID | 규칙 | C2C Rule |
|----|------|----------|
| **R1** | 격자 크기는 **4×4** | Rule 1 |
| **R2** | 셀 값은 `0`(빈칸) 또는 `1~16` | Rule 2 |
| **R3** | **마법합 = 34** | Rule 3 (MagicConstant SSOT) |
| **R4** | **10선** — R1~R4(행), C1~C4(열), D1·D2(대각선) — 각각 합 34. **대각선 누락 금지** | Mom Test ① |
| **R5** | 완성 격자: 1~16 각각 1회 (중복 없음) | 완성 마방진 |
| **R6** | `0`이 포함된 줄: 합산·판정 정책을 테스트와 구현에서 **일관** 적용 | 부분 격자 |
| **R7** | 좌표·출력은 **1-index** `(row, col)` | boundary `int[6]` |

### 10선 ID 및 좌표 (0-index 내부, 1-index 출력)

| ID | 설명 | 셀 (0-index) |
|----|------|----------------|
| R1~R4 | 행 1~4 | `grid[r][0..3]` |
| C1~C4 | 열 1~4 | `grid[0..3][c]` |
| D1 | 주대각선 | `(0,0)(1,1)(2,2)(3,3)` |
| D2 | 부대각선 | `(0,3)(1,2)(2,1)(3,0)` |

### 실패 조건 (문제 인식점)

| ID | 조건 |
|----|------|
| F1 | 10선 중 하나라도 합 ≠ 34 |
| F2 | 완성 격자에서 1~16 중복 또는 누락 |
| F3 | 격자 크기 ≠ 4×4 또는 값 범위 위반 |

### MagicConstant SSOT

- `GRID_SIZE = 4`, `MAGIC_SUM = 34`, `CELL_MAX = 16`, `BLANK_CELL = 0`
- 정의 위치: `src/entity/constants.py` (또는 `src/entity.py`의 `MAGIC`)
- **리터럴 `34`/`16`/`4`/`0` 코드 산재 금지**

---

## 6. 아키텍처 (ECB)

| 계층 | 역할 | 예시 |
|------|------|------|
| **Entity** | 격자·줄·마법상수·좌표·채움값 계산 | `sum_line`, `find_blank_coords`, `solve_step_a` |
| **Control** | 10선 순회·판정 흐름·결과 조합 | `validate_lines` |
| **Boundary** | 입출력·오류 코드·`execute()` | grid 파싱, `E001`~`E007`, `int[6]` 직렬화 |

### 의존 방향

```
boundary → control → entity
entity → * import 금지
```

### Dual-Track TDD

| Track | Layer | 테스트 ID | Mock |
|-------|-------|-----------|------|
| **Logic (B)** | entity, control | `D-*` | Domain Mock **금지** |
| **UI (A)** | boundary | `U-*` | I/O·control Mock **허용** |

**진행 순서:** Logic Track GREEN 누적 후 → UI Track

---

## 7. Boundary API (필수)

```python
validate_lines(grid) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": list[str]  # 예: ["D1"]
}
```

| 필드 | 의미 |
|------|------|
| `status: pass` | 10선 모두 합 34 (빈칸 정책 충족) |
| `status: fail` | 한 줄이라도 합 ≠ 34 |
| `status: incomplete` | 빈칸 등 미완 — 판정 보류 |
| `failed_lines` | 합 ≠ 34인 줄 ID. `pass`/`incomplete` 시 `[]` |

---

## 8. 기능 요구사항 (FR)

### 핵심 — 10선 판정

| ID | 계층 | 설명 | 우선순위 | Test ID |
|----|------|------|----------|---------|
| **FR-VAL** | control | `validate_lines` — 10선 합 34 판정, `failed_lines` 반환 | P0 | D-VAL-01~03 |
| **FR-2** | entity | `sum_line(cells)` — 한 줄 합 계산 | P0 | D-001 |
| **FR-1** | control | entity 함수 오케스트레이션 | P1 | D-006 |

### 위치·채움 (Logic 확장)

| ID | 계층 | 설명 | 우선순위 | Test ID |
|----|------|------|----------|---------|
| **FR-LOC-01** | entity | 유효 4×4 부분 격자(빈칸 `0` **정확히 2개**)에서 빈칸 좌표를 **row-major** 스캔, **1-index** `(row,col)` 2개 반환 | P0 | D-LOC-01 |
| **FR-SOL-01** | entity | G1 등 유효 입력에서 행 합 기준 1스텝 채움값 → `int[6]` `[r1,c1,n1,r2,c2,n2]` 1-index | P1 | D-SOL-01 |

### Boundary 입출력

| ID | 계층 | 설명 | 우선순위 | Test ID |
|----|------|------|----------|---------|
| **FR-BND-IN** | boundary | 입력 검증 — null, 크기, 빈칸 개수 | P1 | U-IN-01~03 |
| **FR-BND-OUT** | boundary | 유효 입력 시 `int[6]` 길이 6 출력 | P1 | U-OUT-01 |
| **FR-BND-FLOW** | boundary | 무효 입력 시 `execute()` 미호출 | P2 | U-FLOW-02 |

### 레거시 (세션 3 초기)

| ID | 설명 | 비고 |
|----|------|------|
| FR-1 (legacy) | `validate(grid) -> bool` | → `validate_lines`로 대체 |
| FR-3 | 실패 선 식별 | `failed_lines`에 흡수 |

---

## 9. 성공 기준 (Acceptance Criteria)

| ID | 기준 | Mom Test | Test ID |
|----|------|----------|---------|
| **AC-1** | 행·열 OK, **대각선 1개만** 틀린 격자 → `status: fail`, `failed_lines`에 D1 또는 D2 | ① 대각선 누락 | D-VAL-01 |
| **AC-2** | 올바른 4×4 완성 마방진 → `status: pass`, `failed_lines: []` | 판정 기준선 | D-VAL-02 |
| **AC-3** | 빈칸 2개 부분 격자 → `incomplete` 또는 정책에 따른 검사 | ② “빈칸 2개 넣고” | D-VAL-03, D-004 |
| **AC-4** | `pytest` 1회로 AC-1~3 검증, **수 초 이내** | ② “20분 확인” | 전체 |
| **AC-5** | G1 → `find_blank_coords` = `[(2,2),(3,3)]` row-major 1-index | FR-LOC-01 | D-LOC-01 |
| **AC-6** | G1 → `solve_step_a` = `int[6]` golden 일치 | FR-SOL-01 | D-SOL-01 |

---

## 10. 오류 코드 (Boundary 전담)

| 코드 | 의미 | 조건 | Test ID |
|------|------|------|---------|
| **E001** | `INVALID_SIZE` | 4×4 아님 | U-IN-02 |
| **E002** | `INVALID_BLANK` | 빈칸 0개 또는 2개 아님 | U-IN-03 |
| **E003** | `INVALID_NULL` | `grid=None` | U-IN-01, U-FLOW-02 |
| **E004** | `INVALID_VALUE` | 셀 값이 `0`~`16` 범위 밖 | (예약) |
| **E005** | `INVALID_DUPLICATE` | 완성 격자 1~16 중복 | (예약) |
| **E006** | (boundary 전담) | 흐름·상태 오류 | (예약) |
| **E007** | (boundary 전담) | 출력 직렬화 오류 | (예약) |

- **entity/control에서 E001~E005 raise·return 금지**
- Golden 포맷: `ERROR: E00x MESSAGE`

---

## 11. 테스트 요구사항

### Test ID 체계

| 패턴 | Track | 파일 |
|------|-------|------|
| `D-*` | Logic | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` |
| `U-*` | UI | `tests/boundary/test_u_*.py` |

상세: `.cursor/skills/magic-square-tdd/reference.md`

### ARRR · TDD 사이클

| ARRR | Phase | Command |
|------|-------|---------|
| **A**sk | RED ③ | `/red-test-plan` |
| **R**espond | RED ④ | `/red-skeleton` |
| **R**efine | GREEN | `/green-minimal` → `/golden-master` |
| **R**eview | REFACTOR | `/refactor-smell` → `/refactor-safe` |

- RED: `tests/`만, pytest **FAIL**
- GREEN: 최소 `src/`, pytest **PASS**
- 금지: assert 완화, `skip`, `xfail`

### RED 우선 케이스 (Mom Test)

1. 행·열 OK, **D1만** ≠ 34 → `fail`, `["D1"]`
2. 완성 마방진 → `pass`
3. 빈칸 2개 부분 격자 → `incomplete` 정책

### Golden Master

- `tests/golden/*.approved.txt` — `int[6]`, ERROR 문자열
- `UPDATE_GOLDEN=1`로만 기준 갱신
- 수동 편집 우회 금지

---

## 12. 부록 — 픽스처 G1

**이름:** `grid_g1` (`tests/conftest.py`)

| 항목 | 값 |
|------|-----|
| 크기 | 4×4 |
| 빈칸 | `0` **2개** — 1-index **(2,2)**, **(3,3)** |
| 용도 | D-LOC-01, D-SOL-01, U-OUT-01 기준 입력 |

```
grid_g1 (0-index):
[16,  3,  2, 13]
[ 5,  0, 11, 12]
[ 9,  6,  0, 12]
[ 4, 15, 14,  1]
```

> 부분 격자(완성 마방진 아님). `12` 중복 등은 **의도적** 테스트 데이터.

---

## 13. 8계층 매핑 (세션 3+)

| 계층 | PRD 대응 |
|------|----------|
| Rule | §5 |
| Command | FR-VAL, FR-2, `validate_lines` |
| (Skill) | 10선 추출, `failed_lines` |
| Test Loop | §11 |
| ARRR Command | `.cursor/commands/` |
| Skill | `.cursor/skills/magic-square-tdd/` |

---

## 14. 범위 및 로드맵

| 단계 | 범위 | 상태 |
|------|------|------|
| STEP 1 | Mom Test · 문제 정의 | ✅ 완료 |
| STEP 2 | Harness · `.cursorrules` | ✅ 완료 |
| STEP 3 | Rule + Command + Test Loop 골격 | ✅ 진행 |
| ARRR | Command·Skill 산출물 | ✅ |
| Logic RED/GREEN | D-LOC, D-SOL, D-VAL | 🔲 진행 |
| UI Track | U-IN, U-OUT, U-FLOW | 🔲 Logic 후 |
| Solver/MissingFinder/GUI | — | Out of scope |

---

## 15. 참고 문서

| 문서 | 설명 |
|------|------|
| `.cursorrules` | 도메인·API·ECB·TDD AI 규칙 |
| `Report/01.REPORT.md` | Mom Test 인터뷰 원본 |
| `Report/03.REPORT.md` | 세션 3 워크북 |
| `Report/04.REPORT.md` | Harness·ECB 골격 |
| `.cursor/skills/magic-square-tdd/reference.md` | D-*/U-* Test ID |
| `.cursor/skills/magic-square-tdd/SKILL.md` | Dual-Track TDD 절차 |

---

*본 문서는 `docs/PRD.md` — MagicSquare_xx 제품 요구사항 v0.2입니다.*
