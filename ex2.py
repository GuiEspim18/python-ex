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
    diagonalSum(0)

def diagonalSum(diagonal):
    total = 0
    if diagonal == 0:
        for a in range(0, len(nestedList), 1):
            # returnDiagonal(nestedList[i], (len(nestedList[i])-(i+1)) - 1, 0)
            for b in range(0, len(nestedList[a]), 1):
                if (a >= b):
                    print(b)
    else: 
        for i in range(0, len(nestedList), 1):
            d = (len(nestedList[i]) + 1) - i
            # print(d)
            returnDiagonal(nestedList[i], d, 1)

def returnDiagonal(l, length, type):
    # total = 0
    total = ""
    if (type == 0):
        for index in range(0, length, 1):
            total += f"{l[index]} "
    else:
        if length > 0 and length <= 5:
            for index in range(0, length, 1):
                # total += f"{l[length-index]} "
                print(index)
    print(total)
    # return total

main(5, 5)