"""D-007 — MagicConstant SSOT (entity)."""

import pytest


def test_d_007_no_scattered_magic_literals_in_src():
    # Given: src/ entity·control 소스 트리
    # When: 리터럴 34/16/4/0 산재 여부 검사
    # Then: MAGIC_SUM 등 상수 SSOT 사용, 산재 리터럴 없음
    pytest.fail("RED: D-007 — MagicConstant SSOT 검사 미구현")
