import math
import sys

def main():
    smallest = 20
    while True:
        if meetsReq(smallest): 
            break
        smallest += 2
    print smallest


def meetsReq(n):
    for i in range(11,21):
        if n % i:
            return False
    return True

if __name__ == '__main__':
    main()