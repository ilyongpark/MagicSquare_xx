"""Entity — 격자·줄·마법상수 등 도메인 데이터."""

from constants import BLANK_CELL, CELL_MAX, GRID_SIZE, MAGIC_SUM

MAGIC = MAGIC_SUM

LINE_IDS = (
    "R1", "R2", "R3", "R4",
    "C1", "C2", "C3", "C4",
    "D1", "D2",
)


def get_line_cells(grid, line_id: str) -> list[int]:
    if line_id.startswith("R"):
        row = int(line_id[1]) - 1
        return list(grid[row])
    if line_id.startswith("C"):
        col = int(line_id[1]) - 1
        return [grid[r][col] for r in range(GRID_SIZE)]
    if line_id == "D1":
        return [grid[i][i] for i in range(GRID_SIZE)]
    if line_id == "D2":
        return [grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)]
    raise ValueError(f"unknown line_id: {line_id}")


def sum_line(cells: list[int]) -> int:
    return sum(cells)


def line_sum_if_no_blank(cells: list[int]) -> int | None:
    """R6 — 빈칸 포함 줄은 합산·판정 생략."""
    if BLANK_CELL in cells:
        return None
    return sum_line(cells)


def find_blank_coords(grid) -> list[tuple[int, int]]:
    """row-major 스캔, 1-index (row, col)."""
    coords: list[tuple[int, int]] = []
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == BLANK_CELL:
                coords.append((r + 1, c + 1))
    return coords


def solve_step_a(grid) -> list[int]:
    """행 합 기준 1스텝 채움값 → [r1, c1, n1, r2, c2, n2] 1-index."""
    result: list[int] = []
    for r, c in find_blank_coords(grid):
        row = grid[r - 1]
        known_sum = sum(v for v in row if v != BLANK_CELL)
        result.extend([r, c, MAGIC_SUM - known_sum])
    return result


def validate_grid(grid) -> bool:
    """F3 — 크기·값 범위 검증."""
    if not grid or len(grid) != GRID_SIZE:
        return False
    for row in grid:
        if len(row) != GRID_SIZE:
            return False
        for cell in row:
            if not (BLANK_CELL <= cell <= CELL_MAX):
                return False
    return True


def validate(grid) -> bool:
    """legacy — 10선 모두 합 34이면 True."""
    if not validate_grid(grid):
        return False
    for line_id in LINE_IDS:
        cells = get_line_cells(grid, line_id)
        if line_sum_if_no_blank(cells) is None:
            return False
        if sum_line(cells) != MAGIC_SUM:
            return False
    return True
