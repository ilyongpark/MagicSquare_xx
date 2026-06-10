"""U-IN — boundary 입력 검증 (FR-BND-IN)."""

from _approval import assert_matches_golden
from boundary.input import validate_input


def test_u_in_01_invalid_null_grid():
    # Given: grid=None
    # When: boundary 입력 검증 호출
    # Then: E003 INVALID_NULL
    assert_matches_golden(validate_input(None), "golden/u_in_01_null.approved.txt")


def test_u_in_02_invalid_size_not_4x4():
    # Given: 3×4 등 크기 불일치 격자
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # When: boundary 입력 검증 호출
    # Then: E001 INVALID_SIZE
    assert_matches_golden(validate_input(grid), "golden/u_in_02_invalid_size.approved.txt")


def test_u_in_03_invalid_blank_count():
    # Given: 빈칸 0개 (완성 마방진)
    grid = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    # When: boundary 입력 검증 호출
    # Then: E002 INVALID_BLANK
    assert_matches_golden(validate_input(grid), "golden/u_in_03_invalid_blank.approved.txt")
