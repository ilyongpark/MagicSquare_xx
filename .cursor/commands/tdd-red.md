# TDD RED — validate_lines

`validate_lines(grid)` 판정 로직에 대한 **RED 단계 전용** 커맨드.
이 단계에서는 `tests/`만 수정한다.

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 선언:

```
Phase: RED
```

---

## 대상

| 항목 | 내용 |
|------|------|
| API | `validate_lines(grid) -> {"status": "pass"\|"fail"\|"incomplete", "failed_lines": [...]}` |
| 테스트 파일 | `tests/test_validate_lines.py` |
| 도메인 | 4×4, `0`/`1~16`, 마법상수 34, 10선 R1~R4·C1~C4·D1·D2 |

---

## AAA 절차

각 테스트는 **Arrange → Act → Assert** 순서로 작성한다.

1. **Arrange** — 4×4 `grid` 준비 (Mom Test 케이스: 대각선만 틀림, 완성 마방진, 빈칸 2개 등)
2. **Act** — `result = validate_lines(grid)` 호출
3. **Assert** — `result["status"]`, `result["failed_lines"]`를 **엄격하게** 검증

한 RED 사이클 = **실패하는 테스트 1개**(또는 동일 행동 1건) 추가.

---

## pytest 예시

```python
from entity import MAGIC
from validate_lines import validate_lines


def test_fail_when_only_d1_diagonal_sum_not_magic():
    # Arrange — 행·열은 34, D1(주대각선)만 틀림
    grid = [
        [16,  2,  3, 13],
        [ 5, 11, 10,  8],
        [ 9,  7,  6, 12],
        [ 4, 14, 15,  1],
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "D1" in result["failed_lines"]
    assert result["failed_lines"] == ["D1"]
```

실행:

```bash
pytest tests/test_validate_lines.py -v
```

**기대 결과:** 새 테스트 **FAIL** (구현이 `...`이거나 요구사항 미충족).

---

## RED 완료 보고 형식

작업 후 아래 형식으로 보고:

```
Phase: RED

## 추가한 테스트
- test_xxx: (한 줄 설명)

## Arrange 요약
- grid 특성 (예: 행·열 OK, D1만 ≠34)

## Assert 기대
- status: fail
- failed_lines: ["D1"]

## pytest 결과
- 명령: pytest tests/test_validate_lines.py::test_xxx -v
- 결과: FAILED (예상대로 RED 확인)

## 다음 단계
- GREEN: src/validate_lines.py 최소 구현
```

---

## 금지 (RED)

| 금지 | 이유 |
|------|------|
| `src/` 수정 (`entity.py`, `validate_lines.py` 등) | RED는 테스트만 |
| assert 완화 (`==` → `in`, 기대값 축소) | 요구사항 훼손 |
| `@pytest.mark.skip`, `xfail` | 실패 회피 |
| 테스트 삭제·기존 assert 약화 | RED 회피 |
| GREEN/REFACTOR 코드 동시 작성 | 한 Phase씩 |

---

## RED 검증 체크리스트

- [ ] 응답 첫 줄: `Phase: RED`
- [ ] 수정 파일: `tests/`만
- [ ] AAA 주석 또는 구조 명확
- [ ] `pytest` 실행 시 **새 테스트 FAIL**
- [ ] Mom Test 연계 케이스 우선 (대각선 누락·원인 확인)
