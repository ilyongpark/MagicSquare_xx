"""U-FLOW — boundary 흐름 검증 (FR-BND-FLOW)."""

import pytest


def test_u_flow_02_execute_not_called_when_grid_null():
    # Given: grid=None
    # When: boundary 흐름 진입
    # Then: execute() 0회 호출 (I/O Mock 허용)
    pytest.fail("RED: U-FLOW-02 — boundary 흐름 미구현")
