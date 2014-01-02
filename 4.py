import math
import sys

def main():
    greatest = 0
    for i in range(1000):
        for j in range(1000):
            if isPalindrome(i*j) and i*j > greatest:
                greatest = i * j
    print greatest

def isPalindrome(n):
    strNum = str(n)
    return strNum == strNum[::-1]

if __name__ == '__main__':
    main()
     