import os
from time import sleep


def pb(board: [[int]]):
    os.system("cls")
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            val = "·" if c is None else c
            print(val, end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end = " ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("---------------------")


def get_cell_numbers(board: [[int]], i: int, j: int):
    i = i // 3 * 3
    j = j // 3 * 3
    nums = []
    for bi in range(i, i + 3):
        for bj in range(j, j + 3):
            nums.append(board[bi][bj])
    return set(filter(None, nums))


def get_possibles(board: [[int]], i: int, j: int):
    rownums = set(filter(None, board[i]))
    colnums = set([row[j] for row in board if row[j]])
    cellnums = get_cell_numbers(board, i, j)
    
    reserved = rownums | colnums | cellnums
    available = [x for x in range(1, 10) if x not in reserved]
    
    return available


def sweep(board: [[int]]):
    removed = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] is None:
                possibles = get_possibles(board, i, j)
                if len(possibles) == 1:
                    board[i][j] = possibles[0]
                    removed += 1
    return removed
                

def solve(board):
    remaining_cells = sum([len([c for c in row if c is None]) for row in board])
    while remaining_cells > 0:
        removed = sweep(board)
        remaining_cells -= removed
        
        pb(board)
        
        if remaining_cells > 0:
            sleep(0.3)
            
        if removed == 0 and remaining_cells > 0:
            print("Unsolvable puzzle!")
            break
            
    if remaining_cells == 0:
        print("Done!")
    