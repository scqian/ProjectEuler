import math
import sys

def main():
    numDict = {}
    numDict['1'] = 'one'
    numDict['2'] = 'two'
    numDict['3'] = 'three'
    numDict['4'] = 'four'
    numDict['5'] = 'five'
    numDict['6'] = 'six'
    numDict['7'] = 'seven'
    numDict['8'] = 'eight'
    numDict['9'] = 'nine'
    numDict['10'] = 'ten'
    numDict['11'] = 'eleven'
    numDict['12'] = 'twelve'
    numDict['13'] = 'thirteen'
    numDict['14'] = 'fourteen'
    numDict['15'] = 'fifteen'
    numDict['16'] = 'sixteen'
    numDict['17'] = 'seventeen'
    numDict['18'] = 'eighteen'
    numDict['19'] = 'nineteen'
    numDict['20'] = 'twenty'
    numDict['30'] = 'thirty'
    numDict['40'] = 'forty'
    numDict['50'] = 'fifty'
    numDict['60'] = 'sixty'
    numDict['70'] = 'seventy'
    numDict['80'] = 'eighty'
    numDict['90'] = 'ninety'
    total = 0
    for i in range(1,1000):
        total += strNum(i, numDict)
    total += 11
    print total

def strNum(n, numDict):
    strVer = str(n)
    strlen = len(strVer)
    toReturn = ''
    if strlen == 3:
        toReturn += (numDict[strVer[0]] + 'hundred')
        if strVer[1] == '0':
            if strVer[1:] != '00':
                toReturn += ('and' + numDict[strVer[2]])
        elif strVer[1] == '1':
            toReturn += ('and' + numDict[strVer[1:]])
        else:
            toReturn += ('and' + numDict[str(int(strVer[1])*10)])
            if strVer[2] != '0':
                    toReturn += numDict[strVer[2]]


    elif strlen == 2:
        if strVer[0] == '1':
            toReturn += numDict[strVer]
        else:
            toReturn += numDict[str(int(strVer[0])*10)] 
            if strVer[1] != '0':
                toReturn += numDict[strVer[1]]
    

    else:
        toReturn += numDict[strVer]
    print toReturn
    return len(toReturn)

if __name__ == '__main__':
    main()

