import math

rounds = []
suitValue = {}
cardValues = {}
cardsPerHand = 5

def main():
    global rounds
    inputCards()
    inputSuits()
    count = 0  #keeps track of number of wins from player 1
    f = open('poker.txt','U')
    for line in f:
        rounds.append(line[:-1])
    #print rounds
    for hand in rounds:
        if playRound(hand): 
            print hand
            count += 1
            #print hand

    print count
    #print playRound('6D 7C 5D 5H 3S 5C JC 2H 5S 3D')

def inputSuits():
    global suitValue
    suitValue['D'] = 1
    suitValue['C'] = 2
    suitValue['H'] = 3
    suitValue['S'] = 4

def playRound(hand):    #returns true if player 1 wins and False if otherwise
    p1 = sorted((hand[:len(hand)/2]).split(' '), key=sortHand)  #a list of player 1's hand sorted
    p2 = sorted((hand[len(hand)/2 + 1:]).split(' '), key=sortHand)  #a list of player 2's hand sorted
    winList = []
    winList.append(rFlush(p1,p2))
    winList.append(sFlush(p1,p2))
    winList.append(fKind(p1,p2))
    winList.append(fHouse(p1,p2))
    winList.append(flush(p1,p2))
    winList.append(straight(p1,p2))
    winList.append(tKind(p1,p2))
    winList.append(tPair(p1,p2))
    winList.append(pair(p1,p2))
    winList.append(hCard(p1,p2))
    winner = -2
    #print winList
    for i in range(len(winList)):
        temp = winList[i]
        #print temp
        if temp != 2:
            winner = temp
            #print winner
            break
    if winner == 0:
        test = hCard(p1,p2)
        #print test
        if test == 1: return True
        elif test == -1: return False
        else: print 'error'
    if winner == 1: return True
    if winner == -1: return False
    print 'error2'
    return False


    #return False

def inputCards():
    global cardValues
    cardValues['2'] = 2
    cardValues['3'] = 3
    cardValues['4'] = 4
    cardValues['5'] = 5
    cardValues['6'] = 6
    cardValues['7'] = 7
    cardValues['8'] = 8
    cardValues['9'] = 9
    cardValues['T'] = 10
    cardValues['J'] = 11
    cardValues['Q'] = 12
    cardValues['K'] = 13
    cardValues['A'] = 14


#Royal Flush Test
def rFlush(p1,p2):
    flag1 = True
    flag2 = True
    if (p1[0])[0] != 'T': flag1 = False  #Check if it is royal
    if (p2[0])[0] != 'T': flag2 = False  #Check if it is royal
    sameSuit = True
    for card in range(cardsPerHand - 1):
        #Hand1 Check
        if cardValues[(p1[card])[0]] != cardValues[(p1[card + 1])[0]] - 1:  #compare number value
            flag1 = False
        if (p1[card])[1] != (p1[card + 1])[1]:  #compare suit value
            flag1 = False

        #Hand 2 Check
        if cardValues[(p2[card])[0]] != cardValues[(p2[card + 1])[0]] - 1:  #compare number value
            flag2 = False
        if (p2[card])[1] != (p2[card + 1])[1]:  #compare suit value
            flag2 = False
    #Check Winner
    #print flag1,flag2
    if flag1 and flag2: 
        #Uknown test?
        return 0  #in case of tie
    if flag1: 
        return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Straight Flush Test
def sFlush(p1,p2):
    flag1 = True
    flag2 = True
    sameSuit = True
    for card in range(cardsPerHand - 1):
        #Hand1 Check
        if cardValues[(p1[card])[0]] != cardValues[(p1[card + 1])[0]] - 1:  #compare number value
            flag1 = False
        if (p1[card])[1] != (p1[card + 1])[1]:  #compare suit value
            flag1 = False

        #Hand 2 Check
        if cardValues[(p2[card])[0]] != cardValues[(p2[card + 1])[0]] - 1:  #compare number value
            flag2 = False
        if (p2[card])[1] != (p2[card + 1])[1]:  #compare suit value
            flag2 = False
    #Check Winner
    if flag1 and flag2: 
        if cardValues[(p1[0])[0]] > cardValues[(p2[0])[0]]: return 1
        elif cardValues[(p2[0])[0]] > cardValues[(p1[0])[0]]: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Four of a Kind Test
def fKind(p1,p2):
    flag1 = False
    flag2 = False
    for card in range(2):
        #Check hand1
        if (p1[card])[0] == (p1[card+1])[0]:
            if (p1[card])[0] == (p1[card+2])[0]:
                if (p1[card])[0] == (p1[card+3])[0]:
                    flag1 = True

        #Check hand2
        if (p2[card])[0] == (p2[card+1])[0]:
            if (p2[card])[0] == (p2[card+2])[0]:
                if (p2[card])[0] == (p2[card+3])[0]:
                    flag2 = True
    #Check Winner
    if flag1 and flag2: 
        if cardValues[(p1[2])[0]] > cardValues[(p2[2])[0]]: return 1
        elif cardValues[(p2[2])[0]] > cardValues[(p1[2])[0]]: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Full House
def fHouse(p1,p2):
    flag1 = False
    flag2 = False
    tNum1 = 0
    tNum2 = 0
    #Check Hand 1
    if isDouble(p1[0],p1[1]):
        flag1 = isTriple(p1[2],p1[3],p1[4])
        if flag1: tNum1 = cardValues[(p1[2])[0]]
    elif isDouble(p1[3],p1[4]):
        flag1 = isTriple(p1[0],p1[1],p1[2])
        if flag1: tNum1 = cardValues[(p1[2])[0]]

    #Check Hand 2
    if isDouble(p2[0],p2[1]):
        flag2 = isTriple(p2[2],p2[3],p2[4])
        if flag2: tNum2 = cardValues[(p2[2])[0]]
    elif isDouble(p2[3],p2[4]):
        if flag2: tNum2 = cardValues[(p2[2])[0]]
        flag2 = isTriple(p2[0],p2[1],p2[2])
        

    #Check Winner
    if flag1 and flag2: 
        if tNum1 > tNum2: return 1
        if tNum2 > tNum1: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Check Flush
def flush(p1,p2):
    flag1 = True
    flag2 = True
    sameSuit = True
    for card in range(cardsPerHand - 1):
        #Hand1 Check
        if (p1[card])[1] != (p1[card + 1])[1]:  #compare suit value
            flag1 = False

        #Hand 2 Check
        if (p2[card])[1] != (p2[card + 1])[1]:  #compare suit value
            flag2 = False
    #Check Winner
    if flag1 and flag2: 
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Check Straight
def straight(p1,p2):
    flag1 = True
    flag2 = True
    sameSuit = True
    for card in range(cardsPerHand - 1):
        #Hand1 Check
        if cardValues[(p1[card])[0]] != cardValues[(p1[card + 1])[0]] - 1:  #compare number value
            flag1 = False

        #Hand 2 Check
        if cardValues[(p2[card])[0]] != cardValues[(p2[card + 1])[0]] - 1:  #compare number value
            flag2 = False
    #Check Winner
    if flag1 and flag2: 
        if cardValues[(p1[0])[0]] > cardValues[(p2[0])[0]]: return 1
        elif cardValues[(p2[0])[0]] > cardValues[(p1[0])[0]]: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Check Three of a Kind
def tKind(p1,p2):
    flag1 = False
    flag2 = False
    tNum1 = 0
    tNum2 = 0
    sameSuit = True
    for card in range(3):
        #Hand1 Check
        if isTriple(p1[card],p1[card+1],p1[card+2]): 
            flag1 = True
            tNum1 = cardValues[(p1[card])[0]]

        #Hand 2 Check
        if isTriple(p2[card],p2[card+1],p2[card+2]): 
            flag2 = True
            tNum2 = cardValues[(p2[card])[0]]
    #Check Winner
    if flag1 and flag2: 
        if tNum1 > tNum2: return 1
        if tNum2 > tNum1: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Check two Pair
def tPair(p1,p2):
    flag1 = False
    flag2 = False
    tNum1 = 0
    tNum2 = 0
    for card in range(2):
        #Check hand1
        if isDouble(p1[card],p1[card + 1]) and isDouble(p1[card+2],p1[card+3]):
            flag1 = True
            temp1 = cardValues[(p1[card])[0]]
            temp2 = cardValues[(p1[card+2])[0]]
            if temp1 > temp2: tNum1 = temp1
            else: tNum1 = temp2
        #Check hand2
        if isDouble(p2[card],p2[card+1]) and isDouble(p2[card+2], p2[card+3]):
            flag2 = True
            temp1 = cardValues[(p2[card])[0]]
            temp2 = cardValues[(p2[card+2])[0]]
            if temp1 > temp2: tNum1 = temp1
            else: tNum2 = temp2
    if isDouble(p1[0],p1[1]) and isDouble(p1[3],p1[4]): flag1 = True
    if isDouble(p2[0],p2[1]) and isDouble(p2[3],p2[4]): flag2 = True

    #Check Winner
    if flag1 and flag2: 
        if tNum1 > tNum2: return 1
        if tNum2 > tNum1: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

#Check pair
def pair(p1,p2):
    flag1 = False
    flag2 = False
    tNum1 = 0
    tNum2 = 0
    for i in range(4):
        if isDouble(p1[i],p1[i+1]): 
            flag1 = True
            tNum1 = cardValues[(p1[i])[0]]
        if isDouble(p2[i],p2[i+1]): 
            flag2 = True
            tNum2 = cardValues[(p2[i])[0]]

    if flag1 and flag2: 
        if tNum1 > tNum2: return 1
        if tNum2 > tNum1: return -1
        return 0  #in case of tie
    if flag1: return 1  #if 1 wins
    if flag2: return -1  #if 2 wins
    return 2  #Returns 2 for neither

def hCard(p1,p2):
    flag1 = False
    flag2 = False
    for i in range(cardsPerHand - 1, -1, -1):
        p1C = cardValues[(p1[i])[0]]
        p2C = cardValues[(p2[i])[0]]
        if p1C > p2C: 
            flag1 = True
            flag2 = False
            break
        if p2C > p1C: 
            flag1 = False
            flag2 = True
            break
    if flag1 and flag2: 
        return 0
    if flag1: return 1
    if flag2: return -1
    return 2

def isDouble(c1,c2):
    return c1[0] == c2[0]

def isTriple(c1,c2,c3):
    return c1[0] == c2[0] == c3[0]

def sortHand(card):
    return cardValues[card[:-1]]





if __name__=='__main__':
    main()
