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
│   └── test_validate_lines.py
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

## 성공 기준 (AC)

| ID | 기준 | Mom Test |
|----|------|----------|
| AC-1 | 대각선 1개만 틀림 → `fail`, `failed_lines`에 D1/D2 | ① 대각선 누락 |
| AC-2 | 완성 마방진 → `pass` | 판정 기준선 |
| AC-3 | 빈칸 2개 부분 격자 → `incomplete` 정책 | ② 빈칸 2개 |
| AC-4 | `pytest` 1회, **수 초** 이내 | ② 20분 확인 |

상세: [docs/PRD.md §9](docs/PRD.md)

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
