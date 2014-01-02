def main():
    count = 0
    for i in range(10000):
        if not possible(i): count += 1
    print count

def possible(n):
    for i in range(50):
        n += reverse(n)
        if isPalindrome(n):
            return True
    return False

def isPalindrome(n):
    strVer = str(n)
    return strVer == strVer[::-1]

def reverse(n):
    strVer = str(n)
    reverse = int(strVer[::-1])
    return reverse

if __name__ == '__main__':
    main()