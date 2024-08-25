# ====================
# PROGRAM : Black Jack
# ====================

def detScore(cards):
    '''determine the score'''
    points = [0]

    for card in cards:
        if card[1:]=='A':
            tempAdd1 = []
            tempAdd2 = []
            for i in range(0,len(points)):
                tempAdd1.append(points[i]+1)
                tempAdd2.append(points[i]+11)
            points = list(set(tempAdd1).union(tempAdd2)) # all the posible points for 'Aces'
            
        elif card[1:].isalpha():
            for i in range(0,len(points)):
                points[i] += 10 # for 'J', 'Q', 'K'
        else:
            for i in range(0,len(points)):
                points[i] += int(card[1:]) # for '1', '2', ..., '10'

    points.sort()
    return points


try:
    # Input :
    dealCards = input().strip().split()
    plyrCards = input().strip().split()


    dealPoints = detScore(dealCards)
    plyrPoints = detScore(plyrCards)
except:
    print('Invalid Input!')
else:
    if (21 in plyrPoints) and (21 not in dealPoints):
        stts = 'Won'
    else:
        for point in plyrPoints:
            if max(dealPoints)<point<21:
                stts = 'Won'
            elif point in dealPoints:
                stts = 'Hit'
            else:
                stts = 'Lost'

    # Output :
    print(stts)
