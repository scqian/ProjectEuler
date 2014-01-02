def main():
    count = 0
    total = 0
    current = 10
    while count != 11:
        if loopNum(current): 
            print current
            count += 1
            total += current
        current += 1
    print total


def isPrime(n):
    if n == 1: return False
    factor = 2
    while factor * factor <= n:
        if n % factor == 0: return False
        factor += 1
    return True

def loopNum(n):
    strVer = str(n)
    for i in range(len(strVer)):
        if not isPrime(int(strVer[i:])): return False
    for i in range(1, len(strVer)):
        if not isPrime(int(strVer[:i*(-1)])): return False
    return True

if __name__ == '__main__':
    main()