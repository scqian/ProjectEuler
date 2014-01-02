import math
import sys

def main():
    total = 0
    checked = []
    for i in range(2, 10000):
        factorSum = fSum(i)
        match = fSum(factorSum)
        if match == i and factorSum != i:
            print i
            total += i
    print total

def fSum(n):
    total = 0
    factor = 1
    while factor * factor <= n:
        if n%factor == 0:
            total += factor
            corresponding = n/factor
            if factor * factor != n and corresponding < n:
                total += corresponding
        factor += 1
    return total

if __name__ == '__main__':
    main()

