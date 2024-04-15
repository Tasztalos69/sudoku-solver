#!/usr/bin/env python
from sudoku_solver.solver import solve
from sudoku_solver.utils.parse_file import parse_file
from sudoku_solver.utils.print_board import print_board


def main() -> None:
    """Runs the app."""

    board = parse_file()

    print_board(board)
    input("Press enter to solve")

    solve(board)


if __name__ == "__main__":
    main()
