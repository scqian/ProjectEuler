def main():
    for i in range(3, 10000000):
        if sFact(i) == i:
            print i

def sFact(n):
    toReturn = 0
    strVer = str(n)
    for i in range(len(strVer)):
        toReturn += fact(int(strVer[i]))
    return toReturn

def fact(n):
    if n <= 1: return 1
    return n*fact(n-1)

if __name__ == '__main__':
    main()