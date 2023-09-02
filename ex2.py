# GUILHERME MONTEIRO ESPIM RM99499

import random

nestedList = []

def main(line, col):
    print("-"*18 + "Matriz" + "-"*19)
    for a in range(0, line, 1):
        addList = []
        for b in range(0, col, 1):
            sort = random.randint(10, 20)
            addList.insert(b, float(sort))
        nestedList.insert(a, addList)
    print("|  l  |  c1  |  c2  |  c3  |  c4  |  c5  |")
    for a in range(0, len(nestedList), 1):
        l = f"| ({a}) | "
        for b in range(0, len(nestedList[a]), 1):
            l += f"{nestedList[a][b]} | "
        print("-"*43)
        print(l)
    print("-"*43)
    print(f"Soma da diagonal 1: {diagonalSum(0)}")
    print(f"Soma da diagonal 2: {diagonalSum(1)}")

def diagonalSum(diagonal):
    total = 0
    if diagonal == 0:
        for a in range(0, len(nestedList), 1):
            if a > 0:
                for b in range(0, a, 1):
                    total += nestedList[a][b]
    else: 
        for a in range(0, len(nestedList), 1):
            if a < 4:
                for b in range(len(nestedList[a])-1, a, -1):
                    total += nestedList[a][b]
    return total

main(5, 5)