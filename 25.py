import math
import sys

def main():
    flag = True
    i = 1
    prev = 1
    count = 2
    while flag:
        next = i + prev
        if len(str(next)) == 1000:
            count += 1
            break
        prev = i
        i = next
        count += 1
    print count

if __name__=='__main__':
    main()