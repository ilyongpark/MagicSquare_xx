"""Boundary 흐름 — 입력 검증 후 execute."""

from boundary.input import validate_input
from entity import solve_step_a


def execute(grid) -> list[int]:
    return solve_step_a(grid)


def run(grid) -> str | list[int]:
    error = validate_input(grid)
    if error:
        return error
    return execute(grid)
