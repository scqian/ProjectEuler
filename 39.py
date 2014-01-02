def main():
    limit = 1001
    maxSol = 0
    toReturn = 0
    for i in range(limit):
        temp = numSolutions(i)
        if temp > maxSol:
            maxSol = temp
            toReturn = i
    print toReturn

def numSolutions(n):
    count = 0
    for a in range(1,n):
        for b in range(1, n-a):
            c = n - a - b
            if pow(a,2)+pow(b,2)==pow(c,2):
                count += 1
    return count/2 #every set is duplicated

if __name__ == '__main__':
    main()