import math
import sys

def main():
    current = 0
    toAdd = 1
    while numDivisors(current) < 500:
        current += toAdd
        toAdd += 1
    print current

def numDivisors(n):
    if (n < 1): return 0
    count = 0
    limit = int(math.sqrt(n))
    for i in range(1,limit):
        if n%i == 0: count += 2
    if n%limit == 0: count += 1
    return count

if __name__ == '__main__':
    main()

