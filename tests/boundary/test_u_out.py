"""U-OUT — boundary 출력 검증 (FR-BND-OUT)."""

import pytest


def test_u_out_01_valid_input_returns_int6(grid_g1):
    # Given: 유효 입력 G1 격자
    # When: boundary execute / 출력 호출
    # Then: len(result) == 6 (int[6])
    pytest.fail("RED: U-OUT-01 — boundary 출력 미구현")
