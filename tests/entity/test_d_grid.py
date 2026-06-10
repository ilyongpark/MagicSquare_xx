"""D-005 — 격자 도메인 규칙 검증 (entity)."""

import pytest


def test_d_005_rejects_invalid_grid_size():
    # Given: 크기가 4×4가 아닌 격자 (예: 3×4)
    # When: 격자 도메인 규칙 검증
    # Then: F3 도메인 규칙 위반 감지
    pytest.fail("RED: D-005 — 격자 크기 검증 미구현")


def test_d_005_rejects_out_of_range_cell_values():
    # Given: 셀 값이 0~16 범위를 벗어난 격자
    # When: 격자 도메인 규칙 검증
    # Then: F3 도메인 규칙 위반 감지
    pytest.fail("RED: D-005 — 셀 값 범위 검증 미구현")
