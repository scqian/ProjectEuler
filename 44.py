import math

def main():
    '''mini = 100000
    for i in range(1000):
        for j in range(1000):
            if isPentagonal(i) and isPentagonal(j):
                diff = abs(i-j)
                summation = i + j
                if isPentagonal(diff) and isPentagonal(summation):
                     print i,j
                    if diff < mini:
                    mini = diff
    print mini'''
    notFound = True
    value = 0 
    i = 0
    while (notFound):
        i += 1
        n = i*(3*i-1)/2
        for j in range(1,i):
            m = j*(3*j-1)/2
            diff = n-m
            summation = n+m
            if isPentagonal(diff) and isPentagonal(summation):
                value = diff
                notFound = False
                break
    print value



def isPentagonal(n):
    return (quad(n)).is_integer()

def quad(n):
    numer = 1 + math.sqrt(1+24*n)
    denom = 6
    return numer/float(denom)

if __name__ == '__main__':
    main()