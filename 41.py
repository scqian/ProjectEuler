def main():
    toReturn = 0
    for i in range(10000001,1000000000,2):
        if isPrime(i) and isPandigital(i):
            toReturn = i
    print toReturn


def isPrime(n):
    if n < 2: return False
    factor = 2
    while factor * factor < n:
        if n%factor == 0: return False
        factor += 1
    return True

def isPandigital(n):
    toSort = []
    strVer = str(n)
    for i in range(len(strVer)):
        toSort.append(int(strVer[i]))
    finalList = sorted(toSort)
    if finalList[0] != 1: 
        return False
    for i in range(len(finalList) - 1):
        if finalList[i] != finalList[i+1] - 1: 
            return False
    return True

if __name__ == '__main__':
    main()