"""Boundary 입력 검증 — E001~E003."""

from constants import BLANK_CELL, EXPECTED_BLANK_COUNT, GRID_SIZE

ERROR_E001 = "ERROR: E001 INVALID_SIZE"
ERROR_E002 = "ERROR: E002 INVALID_BLANK"
ERROR_E003 = "ERROR: E003 INVALID_NULL"


def _is_valid_size(grid) -> bool:
    if not grid or len(grid) != GRID_SIZE:
        return False
    return all(len(row) == GRID_SIZE for row in grid)


def validate_input(grid) -> str | None:
    if grid is None:
        return ERROR_E003
    if not _is_valid_size(grid):
        return ERROR_E001
    blank_count = sum(row.count(BLANK_CELL) for row in grid)
    if blank_count != EXPECTED_BLANK_COUNT:
        return ERROR_E002
    return None
