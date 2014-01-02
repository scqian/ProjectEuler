import math
import sys

count = 0
coins = [1,2,5,10,20,50,100,200]

def main():
    global count
    value = 0
    recurse(value)
    #print count

def recurse(n):
    global count
    global coins
    target = 5
    if n == target:
        count += 1
        print count
    elif n < target:
        #print n
        for i in coins:
            recurse(n+i)

if __name__ == '__main__':
    main()
