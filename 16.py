import math
import sys

def main():
    total = 0
    num = pow(2, 1000)
    strNum = str(num)
    numLen = len(strNum)
    for i in range(numLen):
        total += int(strNum[i])
    print total

if __name__ == '__main__':
    main()