"""U-IN — boundary 입력 검증 (FR-BND-IN)."""

import pytest


def test_u_in_01_invalid_null_grid():
    # Given: grid=None
    # When: boundary 입력 검증 호출
    # Then: E003 INVALID_NULL — "ERROR: E003 INVALID_NULL"
    pytest.fail("RED: U-IN-01 — boundary 입력 검증 미구현")


def test_u_in_02_invalid_size_not_4x4():
    # Given: 3×4 등 크기 불일치 격자
    # When: boundary 입력 검증 호출
    # Then: E001 INVALID_SIZE — "ERROR: E001 INVALID_SIZE"
    pytest.fail("RED: U-IN-02 — boundary 크기 검증 미구현")


def test_u_in_03_invalid_blank_count():
    # Given: 빈칸 0개 (또는 2개 아님) 격자
    # When: boundary 입력 검증 호출
    # Then: E002 INVALID_BLANK — "ERROR: E002 INVALID_BLANK"
    pytest.fail("RED: U-IN-03 — boundary 빈칸 개수 검증 미구현")
