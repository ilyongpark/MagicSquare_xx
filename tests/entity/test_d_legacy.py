"""D-002, D-003 — validate legacy (entity)."""

import pytest


def test_d_002_validate_legacy_returns_false_when_sum_not_magic(grid_d1_only_fail):
    # Given: 10선 중 합 ≠ 34인 격자
    # When: validate(grid) 호출
    # Then: False
    pytest.fail("RED: D-002 — validate(legacy) 미구현")


def test_d_003_validate_legacy_returns_true_for_complete_magic(grid_complete_magic):
    # Given: 완성 4×4 마방진
    # When: validate(grid) 호출
    # Then: True
    pytest.fail("RED: D-003 — validate(legacy) 미구현")
