from time import sleep

from sudoku_solver.algorithms.matrix_elimination import matrix_sweep
from sudoku_solver.algorithms.single_possible import single_possible_sweep
from sudoku_solver.utils.print_board import print_board


def solve(_board: [[int]]) -> None:
    """Solves the sudoku."""

    board = _board

    remaining_cells = sum([len([c for c in row if c is None]) for row in board])

    while remaining_cells > 0:
        filled = 0

        board, _filled = matrix_sweep(board)

        filled += _filled

        board, _filled = single_possible_sweep(board)
        filled += _filled

        remaining_cells -= filled

        print_board(board)

        # Add a small delay for display purposes
        if remaining_cells > 0:
            sleep(0.3)

        if filled == 0 and remaining_cells > 0:
            print("Unsolvable puzzle!")
            break

    if remaining_cells == 0:
        print("Done!")
