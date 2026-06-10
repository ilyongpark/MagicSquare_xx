# red-test-plan — ARRR A단계 (Ask = RED ③)

**C2C 설계표·테스트 플랜만 작성**하는 RED 전용 커맨드.
이 단계에서는 **문서(표) 출력만** 한다. `tests/`·`src/` **파일 생성·수정 금지**.

**추가 입력 없이 즉시 실행.** 사용자가 `/red-test-plan` 만 입력했다. 세션 주제·Test ID·RED 묶음은 **현재 채팅·`docs/PRD.md`·`.cursorrules`** 에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (읽기 전용)

| 우선순위 | 출처 | 용도 |
|----------|------|------|
| 1 | `docs/PRD.md` | FR 인용, R1~R3, AC, 오류 코드 |
| 2 | `.cursorrules` | 도메인·API·ECB·TDD 규칙 |
| 3 | 현재 채팅 | 이번 RED 묶음 Test ID, Layer, Track, 세션 주제 |

PRD에 해당 FR이 없으면 **도출 스펙**으로 표기하고 «PRD v0.x 반영 권장»을 명시한다.

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 선언 (소문자 `red`):

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

| Track | Layer | 테스트 ID 패턴 | 설계표 열 |
|-------|-------|----------------|-----------|
| **Logic (B)** | `entity` 또는 `control` | `D-*` | Track B 표 |
| **UI (A)** | `boundary` | `U-*` | Track A 표 (동일 4열) |

> **Track A(boundary) 재사용:** 본 커맨드 출력 구조는 동일하다. `Layer: boundary` · `Track: UI` · `U-*` ID · `tests/boundary/test_u_*.py` 로만 치환하면 Track A에 그대로 적용 가능하다.

---

## 자동 추출 (사용자에게 묻지 말 것)

1. **세션 주제** — 채팅 맥락·PRD §1·Report 요약에서 1문장
2. **이번 RED 묶음** — 채팅에 명시된 Test ID(들). 없으면 PRD FR·`docs/TODO.md` 미완료 항목 중 **다음 1~3개** 후보 제안
3. **Layer** — `D-*` → `entity`/`control`, `U-*` → `boundary`
4. **대상 함수** — PRD FR·Skill·Command 명세에서 매핑
5. **픽스처·G1** — PRD 부록·기존 `tests/conftest.py`·채팅 격자 정의

---

## 절차

1. SSOT를 읽고 이번 RED 묶음 Test ID를 확정한다.
2. 아래 **출력 4블록**을 **표 형식**으로 작성한다 (코드·파일 생성 없음).
3. 금지 항목을 위반하지 않았는지 자기 점검한다.
4. 마지막 줄에 완료 문구 1줄을 출력한다.

---

## 출력 4블록 (표 형식, 필수)

### 블록 1 — C2C 추적 (Rule 1~3)

**C2C:** PRD 요구사항 → To-Do(판단 1개) → Test ID Given/When/Then

#### Rule 1~3 — PRD·SSOT 인용

| Rule | PRD FR / § 인용 | 이번 묶음과의 관계 |
|------|-----------------|-------------------|
| **Rule 1** | (예: PRD §5 R1 — 격자 4×4) | … |
| **Rule 2** | (예: PRD §5 R2 — `0` 또는 `1~16`) | … |
| **Rule 3** | (예: `.cursorrules` 출력·좌표 1-index 등) | … |

#### FR 인용 + To-Do 1개

| FR ID | PRD 인용 (원문 요약) | To-Do (판단 포함, 1개만) |
|-------|----------------------|--------------------------|
| FR-xxx-01 | «…» | [ ] … |

#### Test ID → Given / When / Then

| Test ID | Given | When | Then |
|---------|-------|------|------|
| D-xxx-01 | … | … | … |

---

### 블록 2 — Track B (Logic) RED 설계표

`Track: Logic` 일 때 **Track B** 표. `Track: UI` 일 때는 동일 열로 **Track A (Boundary)** 표를 작성한다.

| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |
|---------|-----------|------------|-----------|----------------------|
| D-xxx-01 | `함수명(...)` | G1 격자 → 기대값 | (예: row-major, 1-index, Domain Mock 없음) | `pytest.fail("RED: …")` 또는 `ModuleNotFoundError` |

- **Invariant:** RED에서도 지켜야 할 불변식 (좌표 규칙, 10선 ID, 출력 길이 등)
- **Expected RED Failure:** 구현 전 pytest가 **반드시 FAIL** 나는 이유·메시지

---

### 블록 3 — 테스트 플랜

| 항목 | 내용 |
|------|------|
| **파일 경로** | (예: `tests/entity/test_d_loc_01.py` / `tests/boundary/test_u_in_01.py`) |
| **test 함수명 후보** | (예: `test_d_loc_01_blank_coords_row_major`) |
| **conftest 픽스처** | (예: `grid_g1` — 4×4, `0` 2개, **데이터만**, 로직 없음) |
| **pytest 명령** | `python -m pytest <파일>::<함수> -v` |
| **RED 묶음 범위** | 이번 사이클에 포함할 Test ID (1~3개, 명시) |

---

### 블록 4 — ECB·Mock 점검

| 점검 항목 | Logic Track (B) | UI Track (A) |
|-----------|-----------------|--------------|
| **Domain Mock** | **금지** — 실제 entity/control 호출 | boundary I/O·control **Mock 허용** |
| **ECB import** | entity → boundary/control import **금지** | boundary → entity 직접 로직 금지 (계약만) |
| **E001~E005 emit** | entity/control 테스트에서 **금지** | boundary 전담 (U-* 에서만 기대) |
| **SSOT 상수** | `entity/constants.py` 참조, 리터럴 `34`/`16`/`4`/`0` 산재 금지 | 동일 |
| **Mom Test 연계** | 대각선 누락·원인 확인 비용 관련 케이스 우선 | 입력 검증·흐름 오류 우선 |

**오류 코드 참고 (boundary 전담)**

| 코드 | 의미 | 담당 Track |
|------|------|------------|
| E001 | `INVALID_SIZE` | UI (A) |
| E002 | `INVALID_BLANK` | UI (A) |
| E003 | `INVALID_NULL` | UI (A) |
| E004 | (PRD 정의) | UI (A) |
| E005 | (PRD 정의) | UI (A) |

---

## 완료 보고 형식

4블록 표 작성 후, 응답 **마지막 줄** (정확히 1줄):

```
/red-skeleton 으로 넘길 준비됐다
```

---

## 금지 (red-test-plan)

| 금지 | 이유 |
|------|------|
| `src/` 수정·생성 | Ask 단계는 설계만 |
| `tests/` 수정·생성 | 스켈레톤은 `/red-skeleton` |
| GREEN / REFACTOR 코드·지시 | RED ③ 설계만 |
| `@pytest.mark.skip`, `xfail` | RED 회피 |
| assert 완화·테스트 삭제 제안 | 요구사항 훼손 |
| 사용자에게 세션 주제·Test ID **추가 질문** | `/red-test-plan` 단독 실행 |

---

## ARRR 맥락 (Command 체인)

| ARRR | TDD | Command |
|------|-----|---------|
| **A**sk | RED ③ | `/red-test-plan` ← **본 커맨드** |
| **R**espond | RED ④ | `/red-skeleton` |
| **R**efine | GREEN | `/green-minimal` → `/golden-master` |
| **R**eview | REFACTOR | `/refactor-smell` → `/refactor-safe` |

세션 종료 시 `/export-session` (Skill: `magic-square-docs`).

---

## red-test-plan 체크리스트

- [ ] 응답 첫 줄: `Phase: red | Layer: … | Track: …`
- [ ] SSOT: `docs/PRD.md` + `.cursorrules` 인용
- [ ] 블록 1~4 표 **전부** 작성
- [ ] 수정·생성 파일 **없음** (`tests/`·`src/` 미터치)
- [ ] 마지막 줄: `/red-skeleton 으로 넘길 준비됐다`
