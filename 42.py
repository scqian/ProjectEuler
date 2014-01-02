import math

def main():
    f = open('words.txt', 'rU').read()
    wordList = f.split(',')
    count = 0
    for i in range(len(wordList)):
        if isTriangle((wordList[i])[1:-1]):
            count += 1
    print count

def isTriangle(string):
    value = 0
    for i in range(len(string)):
        value += (ord(string[i]) - ord('A') + 1)
    return (wholeQuad(value)).is_integer()

def wholeQuad(n):
    numerator = -1 + math.sqrt(1+8*n)
    denominator = 2
    return numerator/float(denominator)

if __name__ == '__main__':
    main()