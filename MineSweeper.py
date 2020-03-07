from random import randint
from os import system
from time import sleep


def printgrid(grid):
    print()
    for row in grid:
        print(*row, sep='\t', end='\n\n')
    print()


def revealneighbours(mgrid, dgrid, lpos, donepos=[]):
    rlpos = []
    if len(lpos) != 0:
        for x, y in lpos:
            if mgrid[x][y] == '0':
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if i == x and j == y:
                            continue
                        try:
                            if i >= 0 and j >= 0:
                                if mgrid[i][j] == '0' and (i, j) not in donepos:
                                    rlpos.append((i, j))
                                    donepos.append((i, j))
                                    dgrid[i][j] = mgrid[i][j]
                                else:

                                    dgrid[i][j] = mgrid[i][j]
                        except:
                            pass
            else:
                dgrid[x][y] = mgrid[x][y]
        revealneighbours(mgrid, dgrid, rlpos, donepos)


if __name__ == '__main__':
    system('clear')
    [m, n] = list(map(int, input("Enter grid dimensions:\t").split()))

    while True:
        mineCount = int(input("Enter the number of mines:\t"))
        if mineCount >= m * n:
            print('Invalid number of mines!')
            continue
        break

    mineGrid = [['' for _ in range(n)] for _ in range(m)]
    displayGrid = [['-' for _ in range(n)] for _ in range(m)]

    i = 0
    mineLoc = list()
    while i < mineCount:
        x, y = randint(0, m - 1), randint(0, n - 1)
        if (x, y) not in mineLoc:
            mineGrid[x][y] = '*'
            mineLoc.append((x, y))
            i += 1

    for i in range(m):
        for j in range(n):
            neighbourMines = 0
            if mineGrid[i][j] != '*':
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        try:
                            if mineGrid[a][b] == '*' and a >= 0 and b >= 0:
                                neighbourMines += 1
                        except:
                            pass
                mineGrid[i][j] = str(neighbourMines)

    # printgrid(mineGrid)

    # print(mineLoc)
    while True:  # User input loop
        system('clear')
        dcount = 0
        for row in displayGrid:
            dcount += row.count('-')
        if dcount == len(mineLoc):
            printgrid(mineGrid)
            print('CONGRATULATIONS!\nYOU WON!')
            break

        printgrid(displayGrid)
        userInput = list(input("Enter the row and column numbers: \t").split())
        if userInput[0] == 'f' or userInput[0] == 'F':
            try:
                displayGrid[int(userInput[1]) - 1][int(userInput[2]) - 1] = 'F'
                continue
            except:
                print("Invalid Input!")
                sleep(2)
                continue

        elif userInput[0] == '?':
            try:
                displayGrid[int(userInput[1]) - 1][int(userInput[2]) - 1] = '?'
                continue
            except:
                print("Invalid Input!")
                sleep(2)
                continue

        else:
            try:
                x = int(userInput[0]) - 1
                y = int(userInput[1]) - 1
                if x >= m or y >= n:
                    print('Invalid Input!')
                    sleep(2)
                    continue
            except:
                print("Invalid Input!")
                sleep(2)
                continue

        if (x, y) in mineLoc:
            for a, b in mineLoc:
                displayGrid[a][b] = '*'
            printgrid(displayGrid)
            print("GAME OVER!\nYOU LOST!")
            break

        revealneighbours(mineGrid, displayGrid, [(x, y)])
