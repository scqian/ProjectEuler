import math
import sys

def main():
    total = 1000
    for a in range(total):
        for b in range(total - a):
            c = total - a - b
            if a < b and b < c and pow(a,2) + pow(b,2) == pow(c,2):
                print a*b*c
if __name__ == '__main__':
    main()