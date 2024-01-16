# -----------------------------------------+
# Kruize Christensen                       |
# CSCI 127, Program 2                      |
# Last Updated: 30, 2019                   |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

def royal_flush(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) ==1:
        for h in hand:
            if h[0]==10:
                return True
            else:
                return False
    else:
        return False

def straight_flush(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) ==1:
        return True
    else:
        return False

def straight(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) ==2:
        return True
    else:
        return False

def four_of_a_kind(ranks):
    count = ranks.count(2)
    if len(set(ranks)) ==2:
        for item in ranks:
            if count == 4:
                return True
            else:
                return False
    else:
        return False

    
def full_house(ranks):
    count = ranks.count(8)
    if len(set(ranks)) ==2:
        for item in ranks:
            if count == 3:
                return True
            else:
                return False
    else:
        return False

def three_of_a_kind(ranks):
    count = ranks.count(7)
    if len(set(ranks)) ==3:
        for item in ranks:
            if count == 3:
                return True
            else:
                return False
    else:
        return False
    
def two_pair(ranks):
    if len(set(ranks)) ==3:
        return True
        
    else:
        return False

def one_pair(ranks):
    if len(set(ranks)) ==4:
        return True
    else:
        return False

# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+

main()
