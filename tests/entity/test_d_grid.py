"""D-005 — 격자 도메인 규칙 검증 (entity)."""

from entity import validate_grid


def test_d_005_rejects_invalid_grid_size():
    # Given: 크기가 4×4가 아닌 격자 (예: 3×4)
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # When: 격자 도메인 규칙 검증
    # Then: F3 도메인 규칙 위반 감지
    assert validate_grid(grid) is False


def test_d_005_rejects_out_of_range_cell_values():
    # Given: 셀 값이 0~16 범위를 벗어난 격자
    grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 17]]
    # When: 격자 도메인 규칙 검증
    # Then: F3 도메인 규칙 위반 감지
    assert validate_grid(grid) is False
