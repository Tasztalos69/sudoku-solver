import os


def print_board(board: [[int]]) -> None:
    """Prints the board to the console."""

    clear_cmd: str = "cls" if os.name == "nt" else "clear"
    os.system(clear_cmd)  # noqa: S605

    for i, r in enumerate(board):
        for j, c in enumerate(r):
            val = "·" if c is None else c
            print(val, end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("---------------------")
