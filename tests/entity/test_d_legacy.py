"""D-002, D-003 — validate legacy (entity)."""

from entity import validate


def test_d_002_validate_legacy_returns_false_when_sum_not_magic(grid_d1_only_fail):
    # Given: 10선 중 합 ≠ 34인 격자
    # When: validate(grid) 호출
    # Then: False
    assert validate(grid_d1_only_fail) is False


def test_d_003_validate_legacy_returns_true_for_complete_magic(grid_complete_magic):
    # Given: 완성 4×4 마방진
    # When: validate(grid) 호출
    # Then: True
    assert validate(grid_complete_magic) is True
