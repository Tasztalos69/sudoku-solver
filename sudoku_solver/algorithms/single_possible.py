"""Single possible algorithm.

This algorithm is a rather expensive one.
It iterates through the cells, and iterates through every possible number for a cell.
If the selected number cannot fit into the give row / column / region anywhere else, we have our solution.
"""
from typing import Literal

from sudoku_solver.utils.flatten import flatten
from sudoku_solver.utils.get_region_numbers import get_region_numbers


def can_fit_by_row(board: [[int]], i: int, num: int) -> bool:
    """Checks if a number can fit into a row."""
    row_nums = set(filter(None, board[i]))
    return num not in row_nums


def can_fit_by_column(board: [[int]], j: int, num: int) -> bool:
    """Checks if a number can fit into a column."""
    col_nums = {row[j] for row in board if row[j]}
    return num not in col_nums


def can_fit_by_region(board: [[int]], i: int, j: int, num: int) -> bool:
    """Checks if a number can fit into a region."""
    region_nums = get_region_numbers(board, i, j)
    return num not in region_nums


def region_free_cords(board: [[int]], i: int, j: int) -> list[(int, int)]:
    """Gives back free coordinates in a given region."""
    i = i // 3 * 3
    j = j // 3 * 3

    coords = [[(bi, bj) for bj in range(j, j + 3) if board[bi][bj] is None] for bi in range(i, i + 3)]
    return flatten(coords)


def check(board: [[int]], i: int, j: int, mode: Literal["row", "col", "region"]) -> int | None:
    """The check function, which finds a solution for the cell.

    We can run this in three modes: row, column, and region, and it will check availability for the corresponding mode.
    """
    row_nums = set(filter(None, board[i]))
    col_nums = {row[j] for row in board if row[j]}
    region_nums = get_region_numbers(board, i, j)

    available = []
    free_coords: list[int] | list[(int, int)] = []

    match mode:
        case "row":
            available = [x for x in range(1, 10) if x not in row_nums]
            free_coords = [index for (index, x) in enumerate(board[i]) if x is None]
            free_coords.remove(j)
        case "col":
            available = [x for x in range(1, 10) if x not in col_nums]
            free_coords = [index for (index, y) in enumerate(row[j] for row in board) if y is None]
            free_coords.remove(i)
        case "region":
            available = [x for x in range(1, 10) if x not in region_nums]
            free_coords = region_free_cords(board, i, j)
            free_coords.remove((i, j))

    solution = None

    # Iterate through every possible number for the cell
    for num in available:
        good = True

        # Check all other free cells in the row / col / region (specified by mode).
        # If the number cannot fit in anywhere else, we have the solution.
        # Note: We don't need to check for e.g. row availability in row mode, as we already know
        # that it can fit in the row.
        for coord in free_coords:
            a: bool
            b: bool
            match mode:
                case "row":
                    a = can_fit_by_column(board, coord, num)
                    b = can_fit_by_region(board, i, coord, num)
                case "col":
                    a = can_fit_by_row(board, coord, num)
                    b = can_fit_by_region(board, coord, j, num)
                case "region":
                    a = can_fit_by_row(board, coord[0], num)
                    b = can_fit_by_column(board, coord[1], num)

            if a and b:
                good = False
                break

        if good:
            solution = num
            break

    return solution


def single_possible_sweep(board: [[int]]) -> ([[int]], int):
    """Sweeps the board with the "single possible" strategy, by rows, columns and regions.

    :returns: the board, and the number of filled cells.
    """
    filled = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] is not None:
                continue

            for mode in "row", "col", "region":
                sol = check(board, i, j, mode)

                if sol:
                    board[i][j] = sol
                    filled += 1
                    break

    return board, filled
