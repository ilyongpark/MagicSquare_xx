# red-skeleton — ARRR R단계 (Respond = RED ④)

`/red-test-plan`에서 확정한 설계표 기준으로 **RED 스켈레톤**만 작성한다.
이 단계에서는 `tests/`만 수정한다. `src/` 도메인 구현 **금지**.

**추가 입력 없이 즉시 실행.** 사용자가 `/red-skeleton` 만 입력했다. Test ID·파일 경로·픽스처·Given/When/Then은 **직전 `/red-test-plan` 출력·현재 채팅·`docs/PRD.md`** 에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (읽기 전용)

| 우선순위 | 출처 | 용도 |
|----------|------|------|
| 1 | 직전 `/red-test-plan` 4블록 | Test ID, 파일, 픽스처, Expected RED Failure |
| 2 | `docs/PRD.md` | FR, G1 격자, invariant |
| 3 | `.cursorrules` | 도메인·ECB·TDD |

`/red-test-plan` 없이 단독 호출 시: `docs/TODO.md`·`.cursor/skills/magic-square-tdd/reference.md`에서 **다음 미완료 D-*/U-*** 1건을 자동 선정한다.

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: red | Layer: {entity|control|boundary} | Track: {Logic|UI}
```

---

## 자동 추출 (사용자에게 묻지 말 것)

| 항목 | 추출 원천 |
|------|-----------|
| Test ID | 채팅·설계표 (예: `D-LOC-01`) |
| 테스트 파일 | 설계표 블록 3 (예: `tests/entity/test_d_loc_01.py`) |
| test 함수명 | 설계표 블록 3 (예: `test_d_loc_01_blank_coords_row_major`) |
| 픽스처 | 설계표 블록 3 (예: `grid_g1`) |
| 대상 함수 | 설계표 블록 2 (예: `find_blank_coords`) |
| Then 기대값 | 설계표 Given→Then |

---

## 절차

1. SSOT에서 이번 RED 묶음 **Test ID 1~3개**를 확정한다.
2. `tests/conftest.py`에 픽스처가 없으면 **데이터만** 추가한다 (도메인 로직 없음).
3. 테스트 파일에 AAA 스켈레톤을 작성한다.
4. `pytest` 실행 → **FAIL** 확인 (의도적 RED).
5. [보고 형식](#완료-보고-형식)으로 출력한다.

---

## AAA 스켈레톤 규칙

| 규칙 | 내용 |
|------|------|
| 주석 | `# Given:` / `# When:` / `# Then:` (AAA) |
| Then | `pytest.fail("RED: <Test ID> — …")` **한 줄만** |
| assert | 본문·통과 더미 **금지** |
| skip/xfail | **금지** |
| 상수 | `34`/`16`/`4`/`0` 리터럴 금지 → `entity/constants.py` SSOT import (픽스처 검증용만) |
| Domain Mock | Logic Track → **금지** |

### 템플릿 (Logic Track · entity)

```python
def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패")
```

### 예외 — SSOT 상수만 `src/` 허용

`tests/entity` ↔ `src/entity` 패키지 충돌 시 `entity/constants.py`(GRID_SIZE, MAGIC_SUM, CELL_MAX, BLANK_CELL) **상수만** 존재해도 됨. **함수 구현은 GREEN까지 금지.**

---

## pytest 실행

```bash
python -m pytest <파일>::<함수> -v
```

**기대:** `Failed: RED: <Test ID> — …` 또는 `ModuleNotFoundError` / `ImportError` (구현 없음).

---

## 완료 보고 형식

```
Phase: red | Layer: … | Track: …

| 항목 | 내용 |
|------|------|
| Test ID | D-xxx-01 |
| FAIL | (pytest 메시지 한 줄) |
| 변경 파일 | tests/… 만 |

## pytest 결과
- 명령: python -m pytest … -v
- 결과: FAILED (RED 확인)

## 다음 단계
- /green-minimal
```

마지막 줄:

```
/green-minimal 으로 넘길 준비됐다
```

---

## 금지 (red-skeleton)

| 금지 | 이유 |
|------|------|
| `src/` 도메인 함수·로직 추가 | GREEN은 `/green-minimal` |
| assert 본문·통과 더미 | RED는 의도적 FAIL만 |
| `@pytest.mark.skip`, `xfail` | RED 회피 |
| GREEN/REFACTOR 동시 작성 | 한 Phase씩 |
| 이번 묶음 외 Test ID 추가 | RED 범위 초과 |
| 사용자 추가 질문 | 단독 실행 |

---

## red-skeleton 체크리스트

- [ ] 응답 첫 줄: `Phase: red | Layer: … | Track: …`
- [ ] 수정: `tests/`만 (상수 SSOT 예외)
- [ ] AAA + `pytest.fail` 한 줄
- [ ] pytest **FAIL** 확인
- [ ] 마지막 줄: `/green-minimal 으로 넘길 준비됐다`
