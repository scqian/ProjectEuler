def main():
    toReturn = 1
    strNum = ''
    limit = 1000000
    for i in range(1,limit):
        strNum += str(i)
    subscripts = [1,10,100,1000,10000,100000,1000000]
    print strNum
    for i in subscripts:
        print strNum[i-1]
        toReturn *= int(strNum[i-1])
    print toReturn

if __name__ == '__main__':
    main()