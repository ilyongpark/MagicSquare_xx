"""Control + Boundary — 10선 판정 흐름, {status, failed_lines} 계약."""

from typing import Literal, TypedDict


class ValidateResult(TypedDict):
    status: Literal["pass", "fail", "incomplete"]
    failed_lines: list[str]


def validate_lines(grid) -> ValidateResult:
    ...
