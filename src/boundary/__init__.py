"""Boundary — 입출력·오류 코드·execute 흐름."""

from boundary.flow import execute, run
from boundary.input import validate_input

__all__ = ["validate_input", "execute", "run"]
