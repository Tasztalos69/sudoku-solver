from sudoku import solve, pb


def main():
    accepted = [str(x) for x in range(1, 10)]
    with open("input.txt", "r") as file:
        board = [[int(c) if c.strip() in accepted else None for c in row.split(" ")] for row in file.readlines() if row != "\n"]
    
    pb(board)
    input("Press enter to solve")
    
    solve(board)


if __name__ == "__main__":
    main()
        