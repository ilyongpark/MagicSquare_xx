"""D-004 — 부분 격자 합산·판정 정책 (entity)."""

import pytest


def test_d_004_partial_grid_zero_line_policy(grid_g1):
    # Given: 빈칸(0) 포함 줄이 있는 부분 격자 (G1)
    # When: 부분 격자 합산·판정 정책 적용
    # Then: R6 정책에 따라 합산·판정 일관 (legacy validate 대응)
    pytest.fail("RED: D-004 — 부분 격자 정책 미구현")
