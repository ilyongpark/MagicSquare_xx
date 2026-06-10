"""Control — 10선 판정 흐름, {status, failed_lines} 계약."""

from typing import Literal, TypedDict

from constants import BLANK_CELL, MAGIC_SUM
from entity import LINE_IDS, get_line_cells, line_sum_if_no_blank, sum_line


class ValidateResult(TypedDict):
    status: Literal["pass", "fail", "incomplete"]
    failed_lines: list[str]


def _has_blank(grid) -> bool:
    return any(BLANK_CELL in row for row in grid)


def validate_lines(grid) -> ValidateResult:
    if _has_blank(grid):
        return {"status": "incomplete", "failed_lines": []}

    failed_lines: list[str] = []
    for line_id in LINE_IDS:
        cells = get_line_cells(grid, line_id)
        if sum_line(cells) != MAGIC_SUM:
            failed_lines.append(line_id)

    if failed_lines:
        return {"status": "fail", "failed_lines": failed_lines}
    return {"status": "pass", "failed_lines": []}
