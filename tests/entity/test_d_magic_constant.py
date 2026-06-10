"""D-007 — MagicConstant SSOT (entity)."""

import re
from pathlib import Path

from constants import BLANK_CELL, CELL_MAX, GRID_SIZE, MAGIC_SUM


def test_d_007_no_scattered_magic_literals_in_src():
    # Given: src/ entity·control 소스 트리
    src_dir = Path(__file__).resolve().parents[2] / "src"
    skip_files = {"constants.py"}
    forbidden = re.compile(r"(?<![.\w])(?:34|16)\b")

    # When: 리터럴 34/16 산재 여부 검사
    violations: list[str] = []
    for path in src_dir.rglob("*.py"):
        if path.name in skip_files:
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if forbidden.search(line):
                violations.append(f"{path.name}:{lineno}")

    # Then: MAGIC_SUM 등 상수 SSOT 사용, 산재 리터럴 없음
    assert violations == []
    assert MAGIC_SUM == 34
    assert GRID_SIZE == 4
    assert CELL_MAX == 16
    assert BLANK_CELL == 0
