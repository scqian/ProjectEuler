import math

def main():
    count = 0
    for i in range(2,1000000):
        if checkRotation(i):
            #print i
            count += 1
    print count

def checkRotation(n):
    if str(n).find('0') >= 0: return False
    for i in range(len(str(n))):
        if not isPrime(n): return False
        n = rotate(n)
    return True

def rotate(n):
    toReturnString = ''
    strVer = str(n)
    for i in range(1, len(strVer)):
        toReturnString += strVer[i]
    toReturnString += strVer[0]
    return int(toReturnString)


def isPrime(n):
    limit = math.sqrt(n)
    for i in range(2, int(limit) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    main()