import math
import sys

def main():
    num = 100
    fact = factorial(100)
    strFact = str(fact)
    total = 0
    for i in range(len(strFact)):
        total += int(strFact[i])
    print total

def factorial(n):
    if n == 1: return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    main()