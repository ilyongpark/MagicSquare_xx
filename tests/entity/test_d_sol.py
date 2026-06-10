"""D-SOL — solve_step_a (entity)."""

from _approval import assert_matches_golden
from entity import solve_step_a


def test_d_sol_01_step_a_int6_golden(grid_g1):
    # Given: G1 격자
    # When: solve_step_a(grid_g1) 호출
    # Then: int[6] Golden 일치 (1-index)
    result = solve_step_a(grid_g1)
    assert_matches_golden(result, "golden/d_sol_01_g1_step_a.approved.txt")
