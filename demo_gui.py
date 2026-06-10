"""MagicSquare_xx — PyQt 최소 GUI 데모.

실행: python demo_gui.py
의존성: pip install PyQt6  (또는 pip install -e \".[gui]\")
"""

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from boundary.flow import run
from constants import GRID_SIZE
from validate_lines import validate_lines

# tests/conftest.py grid_g1 와 동일
GRID_G1 = [
    [16, 3, 2, 13],
    [5, 0, 11, 12],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

_STATUS_LABEL = {
    "pass": "pass - 10선 모두 합 34",
    "fail": "fail - 틀린 줄",
    "incomplete": "incomplete - 빈칸이 있어 판정 보류",
}


class MagicSquareDemo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("MagicSquare_xx - 10선 검증 데모")
        self.setMinimumWidth(320)
        self._cells: list[list[QLineEdit]] = []
        self._result = QLabel("결과: -")
        self._result.setWordWrap(True)
        self._build_ui()
        self._load_g1()

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        title = QLabel("4x4 격자 (0=빈칸, 1~16)")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        grid_layout = QGridLayout()
        for row in range(GRID_SIZE):
            row_cells: list[QLineEdit] = []
            for col in range(GRID_SIZE):
                cell = QLineEdit()
                cell.setMaxLength(2)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setFixedSize(52, 36)
                grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self._cells.append(row_cells)
        layout.addLayout(grid_layout)

        btn_row = QHBoxLayout()
        load_btn = QPushButton("G1 불러오기")
        load_btn.clicked.connect(self._load_g1)
        validate_btn = QPushButton("10선 검증")
        validate_btn.clicked.connect(self._validate)
        solve_btn = QPushButton("Step A")
        solve_btn.clicked.connect(self._solve)
        btn_row.addWidget(load_btn)
        btn_row.addWidget(validate_btn)
        btn_row.addWidget(solve_btn)
        layout.addLayout(btn_row)
        layout.addWidget(self._result)

    def _read_grid(self) -> list[list[int]] | None:
        grid: list[list[int]] = []
        for row in range(GRID_SIZE):
            values: list[int] = []
            for col in range(GRID_SIZE):
                text = self._cells[row][col].text().strip()
                if text in ("", "0"):
                    values.append(0)
                    continue
                try:
                    value = int(text)
                except ValueError:
                    return None
                if not 1 <= value <= 16:
                    return None
                values.append(value)
            grid.append(values)
        return grid

    def _set_grid(self, grid: list[list[int]]) -> None:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = grid[row][col]
                self._cells[row][col].setText("" if value == 0 else str(value))

    def _load_g1(self) -> None:
        self._set_grid(GRID_G1)
        self._result.setText("G1 샘플 격자를 불러왔습니다.")

    def _validate(self) -> None:
        grid = self._read_grid()
        if grid is None:
            self._result.setText("입력 오류: 각 칸은 0(빈칸) 또는 1~16이어야 합니다.")
            return

        result = validate_lines(grid)
        status = result["status"]
        failed = result["failed_lines"]
        message = _STATUS_LABEL[status]
        if status == "fail" and failed:
            message = f"{message}: {', '.join(failed)}"
        self._result.setText(message)

    def _solve(self) -> None:
        grid = self._read_grid()
        if grid is None:
            self._result.setText("입력 오류: 각 칸은 0(빈칸) 또는 1~16이어야 합니다.")
            return

        result = run(grid)
        if isinstance(result, str):
            self._result.setText(result)
        else:
            self._result.setText(f"Step A int[6]: {result}")


def main() -> None:
    app = QApplication(sys.argv)
    window = MagicSquareDemo()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
