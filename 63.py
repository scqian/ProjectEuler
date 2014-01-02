import math
from fractions import Fraction

def main():
    count = 0
    for i in range(1000000000):
        count += 1
    print count
    #print isNPower(5)

def isNPower(num):
    n = len(str(num))
    testVal = pow(num, 1.0/n)
    return str(round(testVal)) == str(testVal)

if __name__=='__main__':
    main()