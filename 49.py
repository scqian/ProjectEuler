import math

def main():
    incr = 3330
    sValue = 0
    end = 9999 - incr * 2
    for i in range(1489,end,2):
        if isPrime(i):
            if isPrime(i + incr) and isPerm(i,i+incr):
                if isPrime(i + 2*incr) and isPerm(i,i+2*incr):
                    sValue = i
                    break
    print str(sValue) + str(sValue + incr) + str(sValue + 2*incr)

def isPerm(n1, n2):
    str1 = str(n1)
    str2 = str(n2)
    l1 = []
    l2 = []
    for i in range(len(str1)):
        l1 += str1[i]
        l2 += str2[i]
    l1s = sorted(l1)
    l2s = sorted(l2)
    return l1s == l2s


def isPrime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

if __name__== '__main__':
    main()

