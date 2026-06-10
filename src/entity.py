"""Entity — 격자·줄·마법상수 등 도메인 데이터."""

MAGIC = 34

LINE_IDS = (
    "R1", "R2", "R3", "R4",
    "C1", "C2", "C3", "C4",
    "D1", "D2",
)


def get_line_cells(grid, line_id: str):
    ...


def sum_line(cells):
    ...
