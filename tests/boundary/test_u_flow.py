"""U-FLOW — boundary 흐름 검증 (FR-BND-FLOW)."""

from unittest.mock import patch

from boundary.input import ERROR_E003
from boundary.flow import run


def test_u_flow_02_execute_not_called_when_grid_null():
    # Given: grid=None
    # When: boundary 흐름 진입
    with patch("boundary.flow.execute") as mock_execute:
        result = run(None)
    # Then: execute() 0회 호출
    mock_execute.assert_not_called()
    assert result == ERROR_E003
