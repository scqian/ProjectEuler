import math
import sys

def main():
    nameFile = open('names.txt', 'rU')
    strNames = ''
    total = 0
    for line in nameFile:
        strNames += line
    nameList = strNames.split(',')
    for i in range(len(nameList)):
        nameList[i] = (nameList[i])[1:-1]
    sortedNames = sorted(nameList)
    for i in range(len(sortedNames)):
        total = total + nameValue(sortedNames[i]) * (i+1)
    print total

def nameValue(name):
    value = 0
    for i in range(len(name)):
        value += ord(name[i]) - ord('A') + 1
    return value



if __name__ == '__main__':
    main()