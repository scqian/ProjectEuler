import math

def main():
    flag = True
    curr = 1
    target = 4
    fValue = -1
    while flag:
        flag = False
        for i in range(target):
            if not numPrimesFactors(curr + i) == target:
                flag = True
                break
                
        if not flag:
            fValue = curr
        curr += 1
    print fValue


def numPrimesFactors(n):
    count = 0
    limit = int(math.sqrt(n))
    for factor in range(1, limit + 1):
        if n%factor == 0:
            if isPrime(factor):
                count += 1
            if isPrime(n/factor):
                count += 1
    return count

def isPrime(n):
    if n < 2: return False
    limit = int(math.sqrt(n))
    for factor in range(2, limit + 1):
        if n%factor == 0: return False
    return True

if __name__ == '__main__':
    main()