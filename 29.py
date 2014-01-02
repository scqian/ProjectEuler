import math
import sys

def main():
    toCount = []
    for i in range(2,101):
        for j in range(2,101):
            toAdd = pow(i,j)
            toCount.append(toAdd)
    sortList = sorted(toCount)
    distinctLen = 1
    for i in range(1, len(sortList)):
        if sortList[i] != sortList[i - 1]:
            distinctLen += 1
    print distinctLen

if __name__ == '__main__':
    main()