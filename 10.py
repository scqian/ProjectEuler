import math

primes = []
pSums = []

def main():
    global primes
    global sums
    most = 0
    longest = 0
    target = 0
    insertPrimes()
    insertSums()
    for i in primes:
        index = primes.index(i)
        for j in range(index):
            
    '''for i in range(10):
        curVal = checkConsec(primes[i]) #checkConsec returns length of chain
        if curVal > longest:
            longest = curVal
            target = primes[i]
    print target'''
    print pSums

def insertSums():
    global pSums
    global primes
    currAdd = 0
    for i in range(len(primes)):
        currAdd += primes[i]
        pSums.append(currAdd)
def insertPrimes():
    global primes
    for i in range(1000000):
        if isPrime(i):
            primes.append(i)

def isPrime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def checkConsec(n):
    global primes
    gCount = 0 # count that will be returned
    curSum = 0 # variable to keep track of sum
    flag = False
    for i in range(len(primes)): #iterate through primes
        index = i
        count = 0
        if primes[index] > n: return 0
        while curSum < n + 1:
            #print curSum
            curSum += primes[index]
            count += 1
            if curSum == n:
                gCount = count
                flag = True
                break
            index += 1
        if flag: break
        count = 0
        curSum = 0
    return gCount




if __name__ == '__main__':
    main()