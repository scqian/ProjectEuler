import math

def main():
    curr = 3
    flag = True
    toReturn = -1
    while flag:
        if not isPrime(curr):
            found = False
            for sq in range(0, int(math.sqrt(curr/2.0)) + 1):
                p = curr-2*pow(sq,2)
                if isPrime(p): 
                    found = True
                    break
            if not found:
                toReturn = curr
                flag = False
        curr += 2
    print toReturn
    #print isPrime(51)

def isPrime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

if __name__ == '__main__':
    main()

