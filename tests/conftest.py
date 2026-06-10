"""공유 pytest 픽스처 — 테스트 데이터만 (도메인 로직 없음)."""

import pytest


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
    """행·열 합 34, D1(주대각선)만 ≠ 34 — AC-1 / Mom Test."""
    return [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 15, 1],
    ]
