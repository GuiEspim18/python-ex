# GUILHERME MONTEIRO ESPIM RM99499

import random

nestedList = []

def main(line, col):
    print("-"*13 + "Matriz" + "-"*14)
    for a in range(0, line, 1):
        addList = []
        for b in range(0, col, 1):
            sort = random.randint(10, 30)
            addList.insert(b, sort)
        nestedList.insert(a, addList)
    print("|  l  | c1 | c2 | c3 | c4 | c5 |")
    for a in range(0, len(nestedList), 1):
        l = f"| ({a}) | "
        for b in range(0, len(nestedList[a]), 1):
            l += f"{nestedList[a][b]} | "
        print("-"*33)
        print(l)
    print("-"*33)
    sumLineRes = sumLine(3)
    sumColRes = columnSum(1)
    pDiagonalSum  = diagonalSum(0)
    sDiagonalSum  = diagonalSum(1)
    totalSumRes = totalSum()
    print("="*32)
    print(f"Soma da linha 4: {sumLineRes}")
    print(f"Soma da coluna 2: {sumColRes}")
    print(f"Soma da diagonal principal: {pDiagonalSum}")
    print(f"Soma da diagonal secundária: {sDiagonalSum}")
    print(f"Soma de todos os valores: {totalSumRes}")

def sumLine(line):
    selectedLine = nestedList[line]
    total = 0
    for i in range(0, len(selectedLine), 1):
        total += selectedLine[i]
    return total

def columnSum(column):
    total = 0
    for i in range(0, len(nestedList), 1):
        total += nestedList[i][column]
    return total

def diagonalSum(diagonal):
    total = 0
    if diagonal == 0:
        for i in range(0, len(nestedList), 1):
            total += nestedList[i][i]
    else: 
        for i in range(0, len(nestedList), 1):
            d = (len(nestedList) - 1)- i
            total += nestedList[i][d]

    return total

def totalSum():
    total = 0
    for a in range(0, len(nestedList), 1):
        for b in range(0, len(nestedList[a]), 1):
            total += nestedList[a][b]
    return total


main(5, 5)
