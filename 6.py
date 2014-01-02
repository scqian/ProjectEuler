import math
import sys

def main():
    result = 0
    first100 = math.pow(sumHundred(),2)
    for i in range(1, 101):
        result += math.pow(i, 2)
    print first100 - result

def sumHundred():
    total = 0
    for i in range(1, 101):
        total += i
    return total

if __name__ == '__main__':
    main()