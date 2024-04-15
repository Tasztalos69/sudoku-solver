"""Matrix elimination algorithm.

This is a rather dumb algorithm, as it works like this:

- Get all numbers from the corresponding row, column and region
- Subtract these numbers from the available 1-9 range
- If only one possibility remains, fill that in.
"""
from sudoku_solver.utils.get_region_numbers import get_region_numbers


def get_possibles(board: [[int]], i: int, j: int) -> [int]:
    """Gets the possible numbers that can be inserted into a given cell."""

    row_nums = set(filter(None, board[i]))
    col_nums = {row[j] for row in board if row[j]}
    region_nums = get_region_numbers(board, i, j)

    reserved = row_nums | col_nums | region_nums
    return [x for x in range(1, 10) if x not in reserved]


def matrix_sweep(board: [[int]]) -> ([[int]], int):
    """Sweeps the board with the matrix elimination strategy.

    :returns: the board, and the number of filled cells.
    """
    filled = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] is None:
                possibles = get_possibles(board, i, j)
                if len(possibles) == 1:
                    board[i][j] = possibles[0]
                    filled += 1
    return board, filled
