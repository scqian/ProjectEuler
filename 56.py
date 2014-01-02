
def main():
    largest = 0
    for a in range(100):
        for b in range(100):
            test = digits(pow(a,b))
            if test > largest:
                largest = test
    print largest

def digits(n):
    total = 0
    strVer = str(n)
    for i in range(len(strVer)):
        total += int(strVer[i])
    return total


if __name__ == '__main__':
    main()