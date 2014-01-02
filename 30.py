import math
import sys

def main():
    toReturn = 0
    current = 0
    for i in range(1000, 1000000):
        if powSum(i) == i:
            toReturn += i
            print toReturn

def powSum(n):
    strVer= str(n)
    total = 0
    for i in range(len(strVer)):
        total += pow(int(strVer[i]),5)
    return total

if __name__ == '__main__':
    main()