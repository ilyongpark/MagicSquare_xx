"""D-VAL — validate_lines (control)."""

import pytest


def test_d_val_01_fail_when_only_d1_not_magic(grid_d1_only_fail):
    # Given: 행·열 합 34, D1(주대각선)만 ≠ 34인 4×4 격자
    # When: validate_lines(grid) 호출
    # Then: status "fail", failed_lines ["D1"]
    pytest.fail("RED: D-VAL-01 — validate_lines 미구현")


def test_d_val_02_pass_for_complete_magic_square(grid_complete_magic):
    # Given: 1~16 중복 없는 완성 마방진
    # When: validate_lines(grid) 호출
    # Then: status "pass", failed_lines []
    pytest.fail("RED: D-VAL-02 — validate_lines 미구현")


def test_d_val_03_incomplete_for_partial_grid_two_blanks(grid_g1):
    # Given: 빈칸 0 정확히 2개인 부분 격자 (G1)
    # When: validate_lines(grid) 호출
    # Then: status "incomplete" (R6 정책 일관)
    pytest.fail("RED: D-VAL-03 — validate_lines 미구현")
