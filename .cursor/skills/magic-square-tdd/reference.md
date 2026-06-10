# MagicSquare_xx — 테스트 ID 레퍼런스

> SSOT: `docs/PRD.md`, `.cursorrules`. PRD 미등재 FR은 «도출 스펙»으로 표기.

---

## Track B — Logic (`D-*`)

| Test ID | Layer | 대상 함수 | FR/AC | Given→Then 요약 |
|---------|-------|-----------|-------|-----------------|
| D-LOC-01 | entity | `find_blank_coords` | FR-LOC-01 | G1(0×2) → `[(2,2),(3,3)]` row-major 1-index |
| D-SOL-01 | entity | `solve_step_a` | FR-SOL-01 | G1 → `int[6]` 1-index |
| D-VAL-01 | control | `validate_lines` | FR-VAL / `.cursorrules` | 행·열 OK, D1만 ≠34 → `fail`, `["D1"]` |
| D-VAL-02 | control | `validate_lines` | AC pass | 완성 마방진 → `pass`, `[]` |
| D-VAL-03 | control | `validate_lines` | AC incomplete | 빈칸 2개 → `incomplete` 정책 |
| D-001 | entity | `sum_line` | FR-2 | 한 줄 합 계산 |
| D-002 | entity | `validate` (legacy) | AC-1 | 합 ≠34 → False |
| D-003 | entity | `validate` (legacy) | AC-2 | 완성 → True |
| D-004 | entity | `validate` (legacy) | AC-3 | 부분 격자 정책 |
| D-005 | entity | 격자 검증 | F3 | 크기·값 범위 위반 |
| D-006 | control | validate 오케스트레이션 | FR-1 | entity 조합 |
| D-007 | entity | MagicConstant SSOT | `.cursorrules` | 리터럴 34/16 미사용 |

**파일 패턴:** `tests/entity/test_d_<topic>.py`, `tests/control/test_d_<topic>.py`

---

## Track A — UI (`U-*`)

| Test ID | Layer | Given | Then | Expected RED |
|---------|-------|-------|------|--------------|
| U-IN-01 | boundary | `grid=None` | `E003 INVALID_NULL` | ModuleNotFoundError |
| U-IN-02 | boundary | `grid=3×4` | `E001 INVALID_SIZE` | AssertionError |
| U-IN-03 | boundary | 빈칸 0개 | `E002 INVALID_BLANK` | AssertionError |
| U-OUT-01 | boundary | 유효 G1 | `len(result)==6` | pytest.fail RED |
| U-FLOW-02 | boundary | `grid=None` | `execute()` 0회 | pytest.fail RED |

**파일 패턴:** `tests/boundary/test_u_<topic>.py`

---

## 오류 코드 (boundary 전담)

| 코드 | 의미 | Test ID |
|------|------|---------|
| E001 | INVALID_SIZE | U-IN-02 |
| E002 | INVALID_BLANK | U-IN-03 |
| E003 | INVALID_NULL | U-IN-01, U-FLOW-02 |
| E004 | (PRD 정의) | — |
| E005 | (PRD 정의) | — |
| E006 | (PRD 정의) | boundary |
| E007 | (PRD 정의) | boundary |

entity/control 테스트에서 E001~E005 **emit 금지**.

---

## 픽스처 · G1

| 이름 | 설명 |
|------|------|
| `grid_g1` | 4×4, `0` 정확히 2개, (2,2)·(3,3) 1-index — `tests/conftest.py` |

---

## 진행 순서

```
Track B: D-LOC → D-SOL → D-VAL → …  (RED→GREEN→Golden→REFACTOR)
    ↓ Logic GREEN 누적 후
Track A: U-IN → U-OUT → U-FLOW
```

Command 체인: `/red-test-plan` → `/red-skeleton` → `/green-minimal` → `/golden-master` → `/refactor-smell` → `/refactor-safe`
