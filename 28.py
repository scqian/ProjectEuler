import math
import sys
x = 500
y = 500
value = 1
toSort = []

def main():
    global x
    global y
    global toSort
    grid = [[0 for a in range(1001)] for b in range(1001)]
    grid[x][y] = 1 #start at center
    fillGrid(grid)
    toReturn = sumGrid(grid)
    '''print grid[1000][1000]
    print grid[0][0]
    print grid[0][1000]'''
    #print grid[1000][0]
    #print toReturn
    '''print grid'''
    newSorted = sorted(toSort)
    print newSorted
    
def fillGrid(grid):
    global x
    global y
    toMove = 1
    while toMove < 1002:
        moveRight(toMove, grid)
        if toMove == 1001: break
        moveDown(toMove, grid)
        toMove += 1
        moveLeft(toMove, grid)
        moveUp(toMove, grid)
        toMove += 1

def moveRight(steps, grid):
    global x
    global y
    global value
    count = 0
    while count < steps and y < 1000:
        y += 1
        value += 1
        grid[x][y] = value
        count += 1

        toSort.append(value)


def moveDown(steps, grid):
    global x
    global y
    global value
    count = 0
    while count < steps and x < 1000:
        x += 1
        value += 1
        grid[x][y] = value
        count += 1

        toSort.append(value)

def moveLeft(steps, grid):
    global x
    global y
    global value
    count = 0
    while count < steps and y > 0:
        y -= 1
        value += 1
        grid[x][y] = value
        count += 1

        toSort.append(value)

def moveUp(steps, grid):
    #print steps
    global x
    global y
    global value
    count = 0
    while count < steps and x > 0:
        x -= 1
        value += 1
        grid[x][y] = value
        count += 1

        toSort.append(value)

def sumGrid(grid):
    total = 0
    for i in range(1001):
        #print grid[i][i]
        total += grid[i][i]
    for i in range(1001):
        print grid[i][1000-i]
        total += grid[i][1000-i]
        #print i, 1000-i
    return total

if __name__ == '__main__':
    main()