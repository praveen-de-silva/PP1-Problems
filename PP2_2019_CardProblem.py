def addCard(cards_dic, card_name):
    '''add cards to the dictinary'''
    if card_name[0] in cards_dic:
        cards_dic[card_name[0]] += (card_name[1], )
    else:
        cards_dic[card_name[0]] = (card_name[1], )

def isSameSuit(dic):
    '''check all elements of the dict are same suit'''
    values = list(dic.values())
    first_val = values[0][0] # comparing card
    
    for val in values:
        if val[0] != first_val: # if compair fail; then gives false
            return False
    return True

def checkRank(player_cards):
    '''check the rank of the player'''
    player_vals = sorted(player_cards.keys()) # all values of the card pack
    
    for x in player_vals:
        if len(player_cards[x])==3 and len(player_vals)==2: # check : Rank 04
            return 4
        if len(player_cards[x])>=3: # check : Rank 02
            return 2
        
        
    if isSameSuit(player_cards):
        royal_fam = ['T', 'J', 'Q', 'K', 'A']
        if set(royal_fam)<=set(player_vals): # check : Rank 06
            return 6
        if ord(max(player_vals))-ord(min(player_vals))==4 and len(player_vals)==5: # check : Rank 05
            return 5
        return 3
    return 1


if __name__=='__main__':
    player1_cards = dict()
    player2_cards = dict()

    # == Input ==
    inp_str = input().strip() 
    cards = inp_str.strip().split()

    try:
        for i in range(len(cards)):
            if i<5:
                addCard(player1_cards, cards[i])
            else:
                addCard(player2_cards, cards[i])

        player1_rank = checkRank(player1_cards)
        player2_rank = checkRank(player2_cards)

        out_str = f'{player1_rank} {player2_rank}'
        
    except Exception:
        print('Data error!')
    
    else:
        # == Output ==
        file_out = open('Output.txt', 'w')
        file_out.write(out_str)
        print(out_str)
        file_out.close()
