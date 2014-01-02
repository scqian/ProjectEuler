import math

def main():
    count = 0
    for n in range(1,101):
        for r in range(n+1):
            if comb(n,r) > 1e6:
                count += 1
    print count

def comb(n,r):
    num = fact(n)
    denom = fact(r)*fact(n-r)
    return num/denom

def fact(n):
    if n < 2: return 1
    return n*fact(n-1)

if __name__ == '__main__':
    main()