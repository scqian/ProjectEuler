import math

def main():
    flag = True
    curr = 1
    value = 0
    while flag:
        cur2 = curr * 2
        cur3 = curr * 3
        cur4 = curr * 4
        cur5 = curr * 5
        cur6 = curr * 6
        if isPerm(curr,cur2) and isPerm(curr,cur3) and isPerm(curr,cur4) and isPerm(curr,cur5) and isPerm(curr,cur6):
            value = curr
            flag = False
        curr += 1
    print value


def isPerm(i,j):
    str1 = str(i)
    str2 = str(j)
    if sorted(str1) == sorted(str2):
        return True
    return False

if __name__ == '__main__':
    main()