import random

def showCard(d):
    for i in d.keys():
        for j in d[i]:
            print("\t",j," of ",i)

def addCards(s, card):
     if card == 'KING' or card == 'QUEEN' or card == 'JACK':
        return (s+10)
     elif card == 'ACE':
        if s + 11 == 21:
            return (s+11)
        else:
            return (s+1)
     else:
        return (s+card)

choice = 'yes'
while choice == 'yes' or 'y':
    dealer_card = {'spades':[],'clubs':[],'hearts':[],'diamonds':[]}
    player_card = {'spades':[],'clubs':[],'hearts':[],'diamonds':[]}
    sum_dealer = 0
    sum_player = 0

    suit = ['spades','clubs','hearts','diamonds']
    card = [2,3,4,5,6,7,8,9,10,'KING','JACK','QUEEN','ACE']

    #dealer's card
    for i in range(1,3):
        suit_dealt = random.choice(suit)
        card_dealt = random.choice(card)
        dealer_card[suit_dealt].append(card_dealt)
        sum_dealer = addCards(sum_dealer, card_dealt)
        if i == 2:
            print("Dealer has \t..... &\t ",card_dealt," of ",suit_dealt)

    #palyer's card
    for i in range(1,3):
        suit_dealt = random.choice(suit)
        card_dealt = random.choice(card)
        player_card[suit_dealt].append(card_dealt)
        sum_player = addCards(sum_player, card_dealt)

    print("\tYou have : ")
    showCard(player_card)

    if sum_dealer == 21:
        print("----- Dealer wins with BlackJack! 21 -----\nDealer's cards : ",showCard(dealer_card))
    elif sum_player == 21:
        print("----- You win with BlackJack! 21 -----")

    while True:
        if sum_dealer > 21:
            print("Dealer is BUSTED!\n ----- You win! -----")
            break
        elif sum_player > 21:
            print("You are BUSTED!\n ----- Dealer wins! -----")
            break
        else:
            action = input("Do you want to stay or hit ? (stay/hit) : ")
            if action == 'hit':
                #Dealing one card to player
                suit_dealt = random.choice(suit)
                card_dealt = random.choice(card)
                player_card[suit_dealt].append(card_dealt)
                sum_player = addCards(sum_player, card_dealt)
                print("\tNow you have : ")
                showCard(player_card)
                if sum_player == 21:
                    print("----- You Win ! with total of 21 -----")
                    break
            elif action == 'stay':
                while sum_dealer < 17:
                    suit_dealt = random.choice(suit)
                    card_dealt = random.choice(card)
                    dealer_card[suit_dealt].append(card_dealt)
                    sum_dealer = addCards(sum_dealer, card_dealt)
                if sum_dealer > sum_player and sum_dealer < 21:
                    print("\n----- Dealer wins with total of ",sum_dealer," from cards : -----")
                    showCard(dealer_card)
                    print("\n----- Your total is ",sum_player," with cards : -----")
                    showCard(player_card)
                    break
                elif sum_dealer < sum_player and sum_player < 21:
                    print("\n----- You win with total of ",sum_player," from cards : -----")
                    showCard(player_card)
                    print("\n----- Dealer's total is ",sum_dealer," with cards : -----")
                    showCard(dealer_card)
                    break
                elif sum_player == sum_dealer:
                    print("\n----- Game tied! -----")
                    print("\nTotal of dealer is ",sum_dealer," with cards :")
                    showCard(dealer_card)
                    print("\nYour total is ",sum_player," with cards :")
                    showCard(player_card)
                    break
            else:
                print("Invalid Action!")
    dealer_card.clear()
    player_card.clear()
    choice = input("Do you want to continue? (yes(y)/no(n)) ? ")
    if choice == 'y' or choice == 'yes':
        continue
    else:
        break


