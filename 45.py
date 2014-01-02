import math

def main():
    flag = True
    i = 285
    toReturn = 0
    while flag:
        i += 1
        triNum = i*(i+1)/2
        if isPentagonal(triNum) and isHexagonal(triNum):
            flag = False
            toReturn = triNum
    print toReturn


def isPentagonal(n):
    return (quadPent(n)).is_integer()

def quadPent(n):
    numer = 1 + math.sqrt(1+24*n)
    denom = 6
    return numer/float(denom)

def isHexagonal(n):
    return (quadHex(n)).is_integer()

def quadHex(n):
    numer = 1 + math.sqrt(1+8*n)
    denom = 4
    return numer/float(denom)




if __name__ == '__main__':
    main()