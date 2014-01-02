def main():
    toReturn = 0
    for i in range(1000000):
        if isPalindrome(i) and isPalindrome(toBinary(i)):
            toReturn += i
    print toReturn

def toBinary(n):
    strVer = ''
    '''binary = str(bin(n))[2:]
    return int(binary)'''
    while n > 0:
        strVer += str(n%2)
        n /= 2
    print strVer
    return strVer
    


def isPalindrome(n):
    strVer = str(n)
    return strVer == strVer[::-1]



if __name__ == '__main__':
    main()