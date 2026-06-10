"""U-OUT — boundary 출력 검증 (FR-BND-OUT)."""

from _approval import assert_matches_golden
from boundary.flow import run


def test_u_out_01_valid_input_returns_int6(grid_g1):
    # Given: 유효 입력 G1 격자
    # When: boundary run(grid_g1) 호출
    result = run(grid_g1)
    # Then: int[6] Golden 일치
    assert isinstance(result, list)
    assert len(result) == 6
    assert_matches_golden(result, "golden/u_out_01_g1_int6.approved.txt")
