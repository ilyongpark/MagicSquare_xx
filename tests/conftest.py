"""공유 pytest 픽스처 — 테스트 데이터만 (도메인 로직 없음)."""

import sys
from pathlib import Path

import pytest

_tests_root = Path(__file__).resolve().parent
if str(_tests_root) not in sys.path:
    sys.path.insert(0, str(_tests_root))


@pytest.fixture
def grid_g1():
    """G1 — 4×4 부분 격자, 빈칸 0 정확히 2개 (1-index (2,2), (3,3))."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 12],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_complete_magic():
    """완성 4×4 마방진 — 1~16 중복 없음, 10선 합 34."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_d1_only_fail():
    """행·열 합 34, 대각선(D1·D2) ≠ 34 — AC-1 (D1+D2=68 불변)."""
    return [
        [16, 3, 2, 13],
        [5, 11, 11, 7],
        [9, 5, 7, 13],
        [4, 15, 14, 1],
    ]
