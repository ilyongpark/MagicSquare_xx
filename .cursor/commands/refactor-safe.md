# refactor-safe — ARRR R단계 (Review = 안전 리팩터 1건)

`/refactor-smell` 상위 **1건**에 대해 **동작 보존** 리팩터를 1기법만 적용한다.
pytest **전부 PASS**를 유지한다.

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-safe` 만 입력했다. 대상 스멜·기법은 **직전 `/refactor-smell` 표·채팅·코드 스캔**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (읽기 전용)

| 우선순위 | 출처 | 용도 |
|----------|------|------|
| 1 | 직전 `/refactor-smell` 우선순위 1행 | 대상 스멜·기법 |
| 2 | `.cursorrules` | ECB, SSOT |
| 3 | `.cursor/skills/magic-square-tdd/SKILL.md` | REFACTOR 7단계 |

`/refactor-smell` 없이 단독 호출 시: 코드 스캔 후 **가장 위험한 스멜 1건**을 자동 선정한다.

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: refactor | Mode: safe-apply | Target: {스멜 한 줄 요약}
```

---

## 자동 추출 (사용자에게 묻지 말 것)

| 항목 | 추출 |
|------|------|
| 대상 스멜 | smell 표 **우선순위 1** (없으면 자동 스캔) |
| 리팩터 기법 | 표의 «리팩토링 방향» 1개 (Extract Function, Rename Package 등) |
| 영향 파일 | «위치» 열 |
| 검증 범위 | 변경 Layer의 `tests/<layer>/` + golden 연동 테스트 |

---

## 절차 (REFACTOR 1사이클)

### 1. GREEN 스냅샷

```bash
python -m pytest tests/ -v --tb=short
```

**기대:** REFACTOR 전 **전부 PASS**. FAIL이면 GREEN 먼저.

### 2. 범위 한정 — 기법 1개만

| 허용 | 금지 |
|------|------|
| Rename Package/Method | 새 Test ID·새 assert |
| Extract Function/Method | 동작·출력 변경 |
| Move Fixture / SSOT 통일 | assert 완화 |
| Remove Duplication (loader) | 이번 사이클 2개 이상 스멜 동시 해결 |

### 3. ECB·Golden 준수

- import 방향 유지
- golden 있으면 `UPDATE_GOLDEN` **없이** matched 유지 (포맷 변경 시에만 갱신)
- Logic Track Domain Mock 추가 **금지**

### 4. REFACTOR 후 검증

```bash
python -m pytest tests/ -v --tb=short
```

**기대:** **전부 PASS**. FAIL 시 즉시 롤백·수정.

### 5. 보고

[완료 보고 형식](#완료-보고-형식) 출력.

---

## 권장 기법 매핑 (MagicSquare_xx)

| 스멜 | 기법 |
|------|------|
| 패키지 이름 충돌 | Rename Package (`tests/entity` → `tests/logic`) |
| `_load_*` 삼중복 | Extract Function |
| solve 도메인 오해 | Rename Method + Extract Method |
| golden·assert 이중 | Introduce Assertion Helper / SSOT |
| G1 리터럴 산재 | Move Fixture + Externalize Data |

---

## 완료 보고 형식

```
Phase: refactor | Mode: safe-apply | Target: …

| 항목 | 내용 |
|------|------|
| 적용 기법 | Extract Function (예) |
| 대상 스멜 | (우선순위 1 한 줄) |
| 변경 파일 | … |

## pytest (REFACTOR 후)
- 명령: python -m pytest tests/ -v
- 결과: N passed (회귀 없음)

## ECB
- import 위반 없음 / (있으면 Violation 표)

## 다음 단계
- /refactor-smell (재분석) 또는 /red-test-plan
```

마지막 줄:

```
다음 /refactor-smell 또는 RED 로 넘길 준비됐다
```

---

## 금지 (refactor-safe)

| 금지 | 이유 |
|------|------|
| 한 턴에 스멜 2건 이상 | REFACTOR 범위 |
| assert·기대값 변경 | 동작 변경 = 새 RED |
| 새 기능·새 ID | GREEN/RED 혼입 |
| PASS 깨진 채 보고 | REFACTOR 실패 |
| git commit | 사용자 요청 시에만 |
| 사용자 추가 질문 | 단독 실행 |

---

## refactor-safe 체크리스트

- [ ] REFACTOR 전 pytest 전부 PASS
- [ ] 기법 **1개**만 적용
- [ ] REFACTOR 후 pytest 전부 PASS
- [ ] golden matched 유지 (해당 시)
- [ ] ECB import 위반 없음
