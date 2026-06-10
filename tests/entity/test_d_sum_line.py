"""D-001 — sum_line (entity)."""

from constants import MAGIC_SUM
from entity import sum_line


def test_d_001_sum_line_returns_expected_sum():
    # Given: 한 줄(4셀) 정수 리스트
    cells = [16, 3, 2, 13]
    # When: sum_line(cells) 호출
    # Then: sum(cells) == 기대 합
    assert sum_line(cells) == MAGIC_SUM
