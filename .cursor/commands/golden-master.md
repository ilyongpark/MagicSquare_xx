# golden-master — GREEN PASS 후 승인 기준선

pytest **PASS** 상태에서 **Golden Master** 기준선만 구축한다.
회귀·REFACTOR 시 입·출력 SSOT로 사용한다.

**추가 입력 없이 즉시 실행.** 사용자가 `/golden-master` 만 입력했다. 대상 Test ID·출력 형식은 **채팅·최근 GREEN·`tests/`·`docs/PRD.md`** 에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (읽기 전용)

| 우선순위 | 출처 | 용도 |
|----------|------|------|
| 1 | 최근 PASS 테스트 | Test ID, fixture, 기대값 |
| 2 | `docs/PRD.md` | `int[6]` 1-index, E001~E007 포맷 |
| 3 | `.cursor/skills/magic-square-tdd/SKILL.md` | Golden 규칙 |

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: green | Layer: {entity|control|boundary} | Track: {Logic|UI} | Mode: Golden Master
```

---

## 자동 추출 (사용자에게 묻지 말 것)

| 항목 | 추출 |
|------|------|
| 대상 Test ID | 최근 GREEN PASS (예: `D-SOL-01`, `U-OUT-01`) |
| 테스트 파일·함수 | `test_d_*` / `test_u_*` |
| 출력 형식 | `int[6]` → `INT6: r1,c1,n1,r2,c2,n2` 또는 좌표 리스트·JSON |
| golden 경로 | `tests/golden/<id>_<fixture>_<topic>.approved.txt` |

대상이 없으면: Logic Track에서 **int[6] 또는 구조화 출력**이 있는 최근 PASS 테스트 1건을 선정한다.

---

## 선행 조건

- 대상 테스트 **이미 PASS** — FAIL이면 `/green-minimal` 먼저.
- 전체 회귀 의심 시: `python -m pytest tests/<layer>/ -v` 로 PASS 확인 후 진행.

---

## 절차

### 1. PASS 재확인

```bash
python -m pytest <대상 파일>::<함수> -v
```

### 2. 승인 헬퍼 (`tests/_approval.py`)

없으면 생성:

```python
def assert_matches_golden(actual, relative_path: str) -> None: ...
def format_for_golden(actual) -> str: ...
```

- `UPDATE_GOLDEN=1` 환경변수 시 기준 파일 **갱신**
- 없으면 golden과 **비교** → mismatch 시 FAIL

### 3. 테스트에 golden 경로 연결

```python
from tests._approval import assert_matches_golden

def test_d_sol_01_step_a_success(grid_g1, solve_step_a):
    result = solve_step_a(grid_g1)
    assert_matches_golden(result, "golden/d_sol_01_g1_step_a.approved.txt")
```

### 4. 기준 파일 생성

```bash
# PowerShell
$env:UPDATE_GOLDEN=1; python -m pytest <파일>::<함수> -v

# bash
UPDATE_GOLDEN=1 python -m pytest <파일>::<함수> -v
```

### 5. 검증 (UPDATE_GOLDEN 없음)

```bash
python -m pytest <파일>::<함수> -v
```

**기대:** `matched` 또는 PASS. diff 있으면 내용 요약.

---

## Golden 포맷 규칙

| 유형 | 포맷 | 예 |
|------|------|-----|
| int[6] | `INT6: r1,c1,n1,r2,c2,n2` (1-index) | `INT6: 2,2,6,3,3,7` |
| 좌표 리스트 | JSON baseline | `d_loc_01_g1_baseline.json` |
| 에러 코드 | `ERROR: E00x MESSAGE` | `ERROR: E003 INVALID_NULL` |

- golden **수동 편집으로 통과 우회 금지** — `UPDATE_GOLDEN=1`로만 갱신
- pytest assert SSOT는 테스트 파일; golden은 **승인 스냅샷** 보조

---

## 완료 보고 형식

```
Phase: green | … | Mode: Golden Master

| 항목 | 내용 |
|------|------|
| Test ID | D-xxx-01 |
| golden 파일 | tests/golden/… |
| matched | yes / no |

## diff 요약
(있을 때만)

## pytest
- UPDATE_GOLDEN=1: …
- 검증: … passed

## 다음 단계
- /refactor-smell 또는 다음 /red-test-plan
```

마지막 줄:

```
/refactor-smell 또는 다음 RED 로 넘길 준비됐다
```

---

## 금지 (golden-master)

| 금지 | 이유 |
|------|------|
| PASS 전 golden 생성 | 기준선 오염 |
| golden 수동 편집 후 “matched” 보고 | 우회 |
| assert 완화로 golden 맞추기 | SSOT 훼손 |
| 도메인 로직 변경 (GREEN 범위) | Golden은 스냅샷만 |
| git commit | 사용자 요청 시에만 |
| 사용자 추가 질문 | 단독 실행 |

---

## golden-master 체크리스트

- [ ] 대상 테스트 PASS 확인
- [ ] `_approval.py` 또는 동등 헬퍼
- [ ] `UPDATE_GOLDEN=1`로 기준 생성
- [ ] 일반 실행 matched/PASS
- [ ] 수동 편집 없음
