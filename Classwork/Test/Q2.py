def general_flush(cards):
    suits = [h[1] for h in cards]
    if len(set(suits)) ==1:
        print ("True")
    else:
        print ("False")

general_flush([[10, "hearts"], [14, "spades"], [12, "spades"]])

