# MagicSquare_xx

4×4 **부분 마방진** 학습 프로젝트. Mom Test로 문제를 정의하고, **10선 합 34 판정**(`validate_lines`)부터 Dual-Track TDD·ARRR로 구현한다.

---

## 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 도메인 | 4×4 격자, 빈칸 2개(`0`), 값 `1~16`, **마법합 34** |
| 검증 대상 | **10선** — R1~R4(행) + C1~C4(열) + D1·D2(대각선) |
| 페르소나 | 4×4 부분 마방진을 손으로/코드로 다루는 **학습자** |
| PRD | [docs/PRD.md](docs/PRD.md) v0.2 |
| 현재 단계 | Logic Track RED/GREEN 진행 중 |

### 진짜 문제 (Mom Test)

> 4×4 부분 마방진에서 빈칸 2개를 채운 뒤 행·열·대각선 **10선** 합을 맞추는 과정에서 **검산 대상(대각선)을 빠뜨리거나** 틀린 원인을 바로 짚지 못해, 무엇이 문제인지 확인하는 데만 **20분 가까이 낭비**한다.

### Mom Test 증거

1. “**지난 주**에 빈칸 2개 넣고 … **대각선 하나를 빼먹어서 20분 날렸다**.”
2. “**20분 동안 무엇이 문제인지 확인**하다가 알았어.”
3. “4×4 부분 마방진을 손으로/코드로 다루는 **학습자**”

---

## 도메인 규칙

```
┌────┬────┬────┬────┐
│ 16 │  3 │  2 │ 13 │  ← R1 (행 합 34)
├────┼────┼────┼────┤
│  5 │  0 │ 11 │ 12 │  ← 빈칸 (0) 2개
├────┼────┼────┼────┤
│  9 │  6 │  0 │ 12 │
├────┼────┼────┼────┤
│  4 │ 15 │ 14 │  1 │
└────┴────┴────┴────┘
  ↑ C1~C4 · D1(주대각) · D2(부대각) 각각 합 34
```

| Rule | 설명 |
|------|------|
| R1 | 격자 **4×4** |
| R2 | 셀 값 `0`(빈칸) 또는 `1~16` |
| R3 | 마법합 **34** |
| R4 | **10선** 각각 합 34 — **대각선 누락 금지** |
| R5 | 완성 격자: 1~16 중복 없음 |
| R6 | `0` 포함 줄: 합산·판정 정책 일관 적용 |
| R7 | 좌표·출력 **1-index** |

---

## Boundary API

```python
validate_lines(grid) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": ["D1", ...]  # pass/incomplete 시 []
}
```

| status | 의미 |
|--------|------|
| `pass` | 10선 모두 합 34 |
| `fail` | 한 줄이라도 합 ≠ 34 |
| `incomplete` | 빈칸 등 미완 — 판정 보류 |

---

## 범위

### 하는 것 (v0.2)

| 항목 | 내용 |
|------|------|
| **판정** | `validate_lines` — 10선 합 34 + `failed_lines` |
| **Logic** | `find_blank_coords`, `solve_step_a` (FR-LOC/SOL) |
| **TDD** | Dual-Track — Logic(`D-*`) → UI(`U-*`) |
| **ARRR** | `/red-test-plan` → … → `/refactor-safe` |

### 하지 않는 것 (Non-Goals)

- Solver — 빈칸 자동 채우기
- MissingFinder — 빈칸 위치 탐색
- GridUI / GUI
- 힌트·자동 교정·KPI 약속

> **표면 문제:** “Solver·Validator 프로그램을 만들면 빈칸 2개를 빠르게 채울 수 있다.”  
> → 본 프로젝트는 **10선 판정·원인 확인 비용 절감**만 다룬다.

---

## 프로젝트 구조

```
MagicSquare_xx/
├── README.md
├── docs/
│   └── PRD.md                    # 제품 요구사항 SSOT (v0.2)
├── .cursorrules                  # 도메인·ECB·TDD 규칙
├── .cursor/
│   ├── commands/                 # ARRR Slash Commands
│   └── skills/
│       ├── magic-square-tdd/     # Dual-Track TDD Skill
│       └── magic-square-docs/    # Report·Transcript Skill
├── src/
│   ├── entity.py                 # MAGIC, LINE_IDS, sum_line
│   └── validate_lines.py         # validate_lines (Control+Boundary)
├── tests/
│   ├── conftest.py                 # grid_g1 등 공유 픽스처
│   ├── entity/
│   │   └── test_d_*.py            # D-001, D-004~007, D-LOC-01, D-SOL-01
│   ├── control/
│   │   └── test_d_*.py            # D-VAL-01~03, D-006
│   ├── boundary/
│   │   └── test_u_*.py            # U-IN, U-OUT, U-FLOW
│   ├── golden/
│   │   └── *.approved.txt         # int[6], ERROR Golden Master
│   └── test_validate_lines.py     # (레거시·통합, D-VAL로 이전 예정)
├── Report/                       # 세션 보고서 (01~04)
├── Prompting/                      # Transcript Export
└── pyproject.toml
```

---

## ECB · Dual-Track

```
boundary → control → entity
entity → * import 금지
```

| Track | Layer | Test ID | Mock |
|-------|-------|---------|------|
| **Logic (B)** | entity, control | `D-*` | Domain Mock **금지** |
| **UI (A)** | boundary | `U-*` | I/O Mock **허용** |

진행 순서: **Logic GREEN 누적** → UI Track

---

## TDD · ARRR 워크플로

| ARRR | Command | 산출 |
|------|---------|------|
| **A**sk | `/red-test-plan` | C2C 설계표 (파일 없음) |
| **R**espond | `/red-skeleton` | `tests/` pytest.fail |
| **R**efine | `/green-minimal` | `src/` 최소 구현 |
| **R**efine+ | `/golden-master` | Golden 기준선 |
| **R**eview | `/refactor-smell` → `/refactor-safe` | 스멜 분석·안전 리팩터 |

사이클: **RED → GREEN → REFACTOR** (한 Phase씩)  
금지: assert 완화, `skip`, `xfail`

---

## 테스트 플랜

PRD v0.2 [§8 FR](docs/PRD.md), [§9 AC](docs/PRD.md), [§10 오류 코드](docs/PRD.md), [§11 테스트 요구사항](docs/PRD.md) 기준.  
상세 Given→Then: [.cursor/skills/magic-square-tdd/reference.md](.cursor/skills/magic-square-tdd/reference.md)

### Test ID 체계

| 패턴 | Track | Layer | 테스트 파일 | Mock |
|------|-------|-------|-------------|------|
| `D-*` | Logic (B) | entity, control | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` | Domain Mock **금지** |
| `U-*` | UI (A) | boundary | `tests/boundary/test_u_*.py` | I/O·control Mock **허용** |

**진행 순서:** Logic Track GREEN 누적 → UI Track

```
Track B: D-LOC → D-SOL → D-VAL → (D-001, D-006 …)
    ↓
Track A: U-IN → U-OUT → U-FLOW
```

### Track B — Logic (`D-*`)

#### P0 — 핵심 판정·위치 (Mom Test 우선)

| Test ID | 계층 | 대상 | FR/AC | Given | Then (기대) | 파일 |
|---------|------|------|-------|-------|-------------|------|
| **D-VAL-01** | control | `validate_lines` | FR-VAL, AC-1 | 행·열 합 34, **D1만** ≠ 34인 4×4 격자 | `status: "fail"`, `failed_lines: ["D1"]` | `tests/control/test_d_val.py` |
| **D-VAL-02** | control | `validate_lines` | FR-VAL, AC-2 | 1~16 중복 없는 **완성 마방진** | `status: "pass"`, `failed_lines: []` | `tests/control/test_d_val.py` |
| **D-VAL-03** | control | `validate_lines` | FR-VAL, AC-3 | 빈칸 `0` **정확히 2개** 부분 격자 | `status: "incomplete"` (R6 정책 일관) | `tests/control/test_d_val.py` |
| **D-LOC-01** | entity | `find_blank_coords` | FR-LOC-01, AC-5 | `grid_g1` (G1 픽스처) | `[(2,2), (3,3)]` — row-major, **1-index** | `tests/entity/test_d_loc.py` |
| **D-SOL-01** | entity | `solve_step_a` | FR-SOL-01, AC-6 | `grid_g1` | `int[6]` `[r1,c1,n1,r2,c2,n2]` Golden 일치 | `tests/entity/test_d_sol.py` |
| **D-001** | entity | `sum_line` | FR-2 | 한 줄(4셀) 정수 리스트 | `sum(cells)` == 기대 합 | `tests/entity/test_d_sum_line.py` |

#### P1 — 오케스트레이션·확장

| Test ID | 계층 | 대상 | FR/AC | Given | Then (기대) | 파일 |
|---------|------|------|-------|-------|-------------|------|
| **D-006** | control | entity 조합 | FR-1 | `sum_line` 등 entity 함수 | `validate_lines` 흐름 정상 조율 | `tests/control/test_d_orchestration.py` |
| **D-004** | entity | 부분 격자 정책 | AC-3, R6 | 빈칸 포함 줄 | 합산·판정 정책 일관 (legacy `validate` 대응) | `tests/entity/test_d_partial.py` |

#### P2 — 레거시·도메인 검증 (선택·리팩터 시)

| Test ID | 계층 | 대상 | Given | Then (기대) |
|---------|------|------|-------|-------------|
| **D-002** | entity | `validate` (legacy) | 합 ≠ 34 | `False` |
| **D-003** | entity | `validate` (legacy) | 완성 마방진 | `True` |
| **D-005** | entity | 격자 검증 | 크기 ≠ 4×4 또는 값 범위 위반 (F3) | 도메인 규칙 위반 감지 |
| **D-007** | entity | MagicConstant SSOT | 소스 검사 | 리터럴 `34`/`16`/`4`/`0` 산재 없음 — `MAGIC_SUM` 등 상수 사용 |

### Track A — UI (`U-*`)

Logic Track GREEN 누적 **후** 진행. Boundary 전담 — entity/control에서 E001~E005 emit **금지**.

| Test ID | 계층 | FR | Given | Then (기대) | RED 단계 기대 |
|---------|------|-----|-------|-------------|---------------|
| **U-IN-01** | boundary | FR-BND-IN | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` 또는 assert fail |
| **U-IN-02** | boundary | FR-BND-IN | 3×4 등 크기 불일치 | `E001` `INVALID_SIZE` | `AssertionError` |
| **U-IN-03** | boundary | FR-BND-IN | 빈칸 0개 (또는 2개 아님) | `E002` `INVALID_BLANK` | `AssertionError` |
| **U-OUT-01** | boundary | FR-BND-OUT | 유효 입력 `grid_g1` | `len(result) == 6` (`int[6]`) | `pytest.fail` (RED) |
| **U-FLOW-02** | boundary | FR-BND-FLOW | `grid=None` | `execute()` **0회** 호출 | `pytest.fail` (RED) |

오류 출력 Golden 포맷: `ERROR: E00x MESSAGE`

### Acceptance Criteria ↔ Test ID

| AC | 기준 | Mom Test | Test ID |
|----|------|----------|---------|
| **AC-1** | 행·열 OK, 대각선 1개만 틀림 → `fail`, `failed_lines`에 D1 또는 D2 | ① 대각선 누락 | D-VAL-01 |
| **AC-2** | 완성 4×4 마방진 → `pass`, `failed_lines: []` | 판정 기준선 | D-VAL-02 |
| **AC-3** | 빈칸 2개 부분 격자 → `incomplete` 또는 R6 정책 | ② 빈칸 2개 | D-VAL-03, D-004 |
| **AC-4** | `pytest` 1회로 AC-1~3 검증, **수 초** 이내 | ② 20분 확인 | 전체 Logic P0 |
| **AC-5** | G1 → `find_blank_coords` = `[(2,2),(3,3)]` | FR-LOC-01 | D-LOC-01 |
| **AC-6** | G1 → `solve_step_a` = `int[6]` Golden 일치 | FR-SOL-01 | D-SOL-01 |

### 픽스처 G1 (`grid_g1`)

`tests/conftest.py`에 정의. D-LOC-01, D-SOL-01, U-OUT-01 공통 입력.

| 항목 | 값 |
|------|-----|
| 크기 | 4×4 |
| 빈칸 | `0` **2개** — 1-index **(2,2)**, **(3,3)** |
| 성격 | 부분 격자 (완성 마방진 아님, `12` 중복 등 의도적) |

```
grid_g1 (0-index):
[16,  3,  2, 13]
[ 5,  0, 11, 12]
[ 9,  6,  0, 12]
[ 4, 15, 14,  1]
```

### Golden Master

| 대상 | 경로 | 갱신 |
|------|------|------|
| `solve_step_a` `int[6]` | `tests/golden/*.approved.txt` | `UPDATE_GOLDEN=1` 환경변수로만 |
| Boundary ERROR 문자열 | `tests/golden/*.approved.txt` | 수동 편집 우회 **금지** |

### RED 우선 케이스 (Mom Test)

1. **D-VAL-01** — 행·열 OK, D1만 ≠ 34 → `fail`, `["D1"]`
2. **D-VAL-02** — 완성 마방진 → `pass`
3. **D-VAL-03** — 빈칸 2개 부분 격자 → `incomplete` 정책

### 테스트 실행 (Track별)

```powershell
# Logic — 판정 (P0)
python -m pytest tests/control/test_d_val.py -v

# Logic — 위치·채움
python -m pytest tests/entity/test_d_loc.py tests/entity/test_d_sol.py -v

# UI (Logic GREEN 후)
python -m pytest tests/boundary/ -v

# 전체
python -m pytest -v
```

---

## 성공 기준 (AC)

| ID | 기준 | Mom Test | Test ID |
|----|------|----------|---------|
| AC-1 | 대각선 1개만 틀림 → `fail`, `failed_lines`에 D1/D2 | ① 대각선 누락 | D-VAL-01 |
| AC-2 | 완성 마방진 → `pass` | 판정 기준선 | D-VAL-02 |
| AC-3 | 빈칸 2개 부분 격자 → `incomplete` 정책 | ② 빈칸 2개 | D-VAL-03, D-004 |
| AC-4 | `pytest` 1회, **수 초** 이내 | ② 20분 확인 | 전체 P0 |
| AC-5 | G1 → `[(2,2),(3,3)]` | FR-LOC-01 | D-LOC-01 |
| AC-6 | G1 → `int[6]` Golden | FR-SOL-01 | D-SOL-01 |

상세: [docs/PRD.md §9](docs/PRD.md) · 테스트 플랜은 위 [§ 테스트 플랜](#테스트-플랜) 참고

---

## 실행 방법

```powershell
cd c:\DEV\MagicSquare_xx
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
python -m pytest -v
```

RED 예시 (대각선만 틀린 케이스):

```powershell
python -m pytest tests/test_validate_lines.py -v
```

---

## 로드맵

| 단계 | 내용 | 상태 |
|------|------|------|
| STEP 1 | Mom Test · 문제 정의 | ✅ |
| STEP 2 | Harness · `.cursorrules` | ✅ |
| STEP 3 | Rule + Command + Test Loop 골격 | ✅ |
| ARRR | Command·Skill | ✅ |
| Logic | D-LOC, D-SOL, D-VAL | 🔲 |
| UI Track | U-IN, U-OUT, U-FLOW | 🔲 |
| Solver / GUI | — | Out of scope |

---

## 참고 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | FR/AC, 10선, 오류 코드, G1 픽스처 |
| [Report/01.REPORT.md](Report/01.REPORT.md) | Mom Test 인터뷰 |
| [Report/03.REPORT.md](Report/03.REPORT.md) | 세션 3 워크북 |
| [Report/04.REPORT.md](Report/04.REPORT.md) | Harness·ECB 골격 |
| [.cursor/skills/magic-square-tdd/reference.md](.cursor/skills/magic-square-tdd/reference.md) | D-*/U-* Test ID |

---

## Mom Test 원칙

- ✅ “마지막으로 ~했을 때”, “몇 분 걸렸어?”, “어떤 줄을 빼먹었어?”
- ❌ “만들면 좋겠어?”, “이 기능 필요해?”, Solver/ECB 이름 먼저 제시

---

학습용 프로젝트 — MagicSquare_xx (PRD v0.2)
