# green-minimal — ARRR R단계 (Refine = GREEN)

RED 스켈레톤을 **최소 구현**으로 통과시키는 GREEN 전용 커맨드.
이번 RED 묶음 **1~3개 Test ID만** 해결한다.

**추가 입력 없이 즉시 실행.** 사용자가 `/green-minimal` 만 입력했다. RED 대상·파일·함수는 **직전 `/red-skeleton`·채팅·`tests/`·`docs/PRD.md`** 에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (읽기 전용)

| 우선순위 | 출처 | 용도 |
|----------|------|------|
| 1 | `tests/entity/test_d_*.py` 등 RED 스켈레톤 | Test ID, Then 기대값 |
| 2 | `docs/PRD.md` | FR, invariant |
| 3 | `.cursorrules` | ECB, MagicConstant, API |
| 4 | `.cursor/skills/magic-square-tdd/SKILL.md` | GREEN 7단계 |

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: green | Layer: {entity|control|boundary} | Track: {Logic|UI}
```

---

## 자동 추출 (사용자에게 묻지 말 것)

1. **RED 대상 Test ID** — `pytest.fail("RED: …")`가 있는 테스트 또는 채팅 최근 ID
2. **테스트 파일·함수** — 해당 `test_d_*` / `test_u_*`
3. **대상 구현 파일** — Layer별 `src/entity/`, `src/control/`, `src/boundary/`
4. **Then 기대값** — RED 스켈레톤 주석·설계표

---

## 절차 (5단계)

### 1. RED 재확인

```bash
python -m pytest <파일>::<함수> -v
```

**기대:** `pytest.fail` 또는 ImportError → **FAIL** (의도적 RED 상태).

### 2. `src/` 최소 구현

| 규칙 | 내용 |
|------|------|
| 범위 | 이번 RED 묶음 assert만 통과하는 **가장 짧은** 코드 |
| MagicConstant | `34`/`16`/`4`/`0` 리터럴 금지 → `entity/constants.py` SSOT |
| E001~E005 | entity/control에서 **raise/return 금지** |
| ECB | entity → boundary/control import **금지**; control → entity만 |
| Domain Mock | Logic Track → **금지** |

### 3. 테스트 assert 교체

- `pytest.fail("RED: …")` **제거**
- 설계표 Then에 맞는 **실제 assert**로 교체
- assert 완화·skip·xfail **금지**

### 4. PASS 확인

```bash
python -m pytest <파일>::<함수> -v
python -m pytest <파일> -v
```

**기대:** 대상 테스트 **PASS**. 회귀 실패 시 즉시 수정.

### 5. (선택) REPL 스모크

G1(또는 설계표 Given) 입력 vs Then — 1줄로 일치 여부 보고.

---

## 완료 보고 형식

```
Phase: green | Layer: … | Track: …

| 항목 | 내용 |
|------|------|
| PASS Test ID | D-xxx-01 |
| 변경 파일 | src/…, tests/… |

## pytest 결과
| 명령 | 결과 |
|------|------|
| …::test_… | passed |
| … (파일 전체) | N passed |

## ECB 점검
- entity → boundary/control import 없음
- E001~E005 entity 미사용
- Domain Mock 없음 (Logic)

## 다음 단계
- /golden-master (승인 기준선) 또는 다음 RED
```

마지막 줄:

```
/golden-master 또는 다음 /red-test-plan 으로 넘길 준비됐다
```

---

## 금지 (green-minimal)

| 금지 | 이유 |
|------|------|
| 이번 RED 묶음 외 ID 동시 해결 | TDD 한 사이클 |
| REFACTOR (구조 정리·이름 변경) | `/refactor-safe` |
| assert 완화 | 요구사항 훼손 |
| `@pytest.mark.skip`, `xfail` | GREEN 회피 |
| git commit | 사용자 요청 시에만 |
| 사용자 추가 질문 | 단독 실행 |

---

## green-minimal 체크리스트

- [ ] RED FAIL 재확인
- [ ] 최소 구현만 `src/` 추가
- [ ] `pytest.fail` → assert 교체
- [ ] 대상·파일 단위 pytest **PASS**
- [ ] 이번 묶음 외 ID 미해결
