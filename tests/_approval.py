"""Golden Master 승인 헬퍼 — UPDATE_GOLDEN=1 로만 기준 갱신."""

import os
from pathlib import Path

_TESTS_DIR = Path(__file__).resolve().parent


def format_for_golden(actual) -> str:
    if isinstance(actual, list) and len(actual) == 6 and all(isinstance(x, int) for x in actual):
        return "INT6: " + ",".join(str(x) for x in actual)
    if isinstance(actual, str):
        return actual
    return str(actual)


def assert_matches_golden(actual, relative_path: str) -> None:
    golden_path = _TESTS_DIR / relative_path
    formatted = format_for_golden(actual)

    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(formatted + "\n", encoding="utf-8")
        return

    if not golden_path.is_file():
        raise AssertionError(f"golden file missing: {golden_path} (run with UPDATE_GOLDEN=1)")

    expected = golden_path.read_text(encoding="utf-8").strip()
    assert formatted == expected, (
        f"golden mismatch ({relative_path}):\n"
        f"  expected: {expected!r}\n"
        f"  actual:   {formatted!r}"
    )
