# refactor-smell — ARRR R단계 (Review = 스멜 분석)

코드베이스 **코드 스멜**을 읽기 전용으로 분석하고, **우선순위 내림차순 표**로 보고한다.
**코드 수정 금지** — 분석·표 출력만.

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-smell` 만 입력했다. 분석 범위·Layer는 **`src/`·`tests/`·`.cursorrules`·`docs/PRD.md`·채팅**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (읽기 전용)

| 출처 | 용도 |
|------|------|
| `.cursorrules` | ECB, MagicConstant, 10선, Mom Test |
| `docs/PRD.md` | FR, 계층 책임 |
| `.cursor/skills/magic-square-tdd/SKILL.md` | Track·Mock·오류 코드 |
| `src/`, `tests/` | 실제 코드 스캔 |

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: refactor | Mode: smell-analysis | Scope: {자동 추출 범위}
```

---

## 자동 추출 (사용자에게 묻지 말 것)

1. **Scope** — `src/entity`, `src/control`, `src/boundary`, `tests/`, `tests/conftest.py`, `tests/golden/`
2. **현재 pytest 상태** — (있으면) 전체 passed/failed 수 1줄
3. **최근 작업 Track** — 채팅의 Layer/Track 또는 Logic 우선

---

## 절차

1. Scope 내 Python·테스트 파일을 **읽기만** 한다.
2. 아래 **스멜 카테고리**로 후보를 수집한다.
3. **우선순위**를 정한다: 유지보수 비용 · 도메인 오류 위험 · ECB/SSOT 위반 · 확장 시 비용.
4. [결과 표](#결과-표-필수)를 **우선순위 내림차순**으로 작성한다.
5. 상위 3~5개에 **리팩터링 기법 이름**(Fowler 등)을 1줄씩 제안한다.

---

## 스멜 카테고리 (MagicSquare_xx)

| 카테고리 | 예시 |
|----------|------|
| 아키텍처 | `tests/entity` ↔ `src/entity` 패키지 충돌, ECB import 위반 |
| 도메인 | 10선 무시, `solve` 이름과 행 합만 계산, 대각선 누락 위험 |
| SSOT | 리터럴 `34`/`16`/`4`/`0`, golden·assert 이중·비연동 |
| 중복 | `conftest` `_load_*` 반복, assert 이중 검증 |
| 테스트 | Domain Mock on Logic, skip/xfail, 죽은 golden JSON |
| 타입 | Primitive Obsession (`list[list[int]]`, int[6] 의미 불명) |
| 미완성 | 빈 `control`/`boundary`, Dead constant |

---

## 결과 표 (필수)

| 우선순위 | 코드 스멜 | 유형 | 위치 | 설명 | 리팩토링 방향 |
|:---:|:---|:---|:---|:---|:---|
| **1** | … | … | `path:line` | … | (기법명) … |
| **2** | … | … | … | … | … |

- 최소 **5행**, 최대 **17행** (과잉 나열 금지)
- Mom Test 무관 기능 제안 **금지**

### 우선 처리 요약 (3~5 bullet)

1. …
2. …

마지막 줄:

```
/refactor-safe 로 상위 1건 적용 가능
```

---

## 금지 (refactor-smell)

| 금지 | 이유 |
|------|------|
| `src/`·`tests/` **수정** | 분석만 |
| pytest 실행 후 코드 변경 | Review 단계 |
| GREEN/RED 테스트 추가 | Phase 혼입 |
| 사용자 추가 질문 | 단독 실행 |

---

## refactor-smell 체크리스트

- [ ] 응답 첫 줄: `Phase: refactor | Mode: smell-analysis`
- [ ] 우선순위 **내림차순** 표
- [ ] ECB·SSOT·Mom Test 관점 포함
- [ ] 코드 변경 **없음**
- [ ] 마지막 줄: `/refactor-safe` 안내
