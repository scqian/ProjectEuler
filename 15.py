import math
import sys

def main():
    n = 20 * 2
    r = 20
    nFact = factorial(n)
    rFact = factorial(r)
    subFact = factorial(n - r)
    print nFact/(rFact*subFact)

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    main()


