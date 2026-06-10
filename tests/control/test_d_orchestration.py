"""D-006 — validate_lines 오케스트레이션 (control)."""

import pytest


def test_d_006_validate_lines_orchestrates_entity_functions(grid_complete_magic):
    # Given: sum_line 등 entity 함수가 조합 가능한 격자
    # When: validate_lines(grid) 호출
    # Then: entity 조합을 통한 10선 판정 흐름 정상 조율
    pytest.fail("RED: D-006 — validate_lines 오케스트레이션 미구현")
