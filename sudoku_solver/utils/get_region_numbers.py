def get_region_numbers(board: [[int]], i: int, j: int) -> set[int]:
    """Gets the existing numbers in the specified region.

    In our definition, a region is a 3x3 set of numbers which form a square on the board.
    A standard sudoku has 9 of these regions.
    """
    i = i // 3 * 3
    j = j // 3 * 3

    nums = [board[bi][bj] for bj in range(j, j + 3) for bi in range(i, i + 3)]
    return set(filter(None, nums))
