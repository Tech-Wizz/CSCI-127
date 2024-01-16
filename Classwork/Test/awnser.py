##def grocery_bill(file_name):
##    file = open(file_name, "r")
##    for line in file:
##        total += float(line)
##    print ("The total bill = ${:.2f}".format(total))
##    file.close()
##
##grocery_bill("town-and-country.in")


'''
def general_flush(cards):
    for card in cards:
        if card[1] != cards[0][1]:
            return False
    return True
'''

def general_flush(cards):
    suits = []
    for card in cards:
        suits.append(card[1])
    return suits.count(suits[0]) == len(cards)
    

print(general_flush([[3,"hearts"]]))
print(general_flush([[3,"hearts"],[9,"hearts"],[14, "hearts"]]))
print(general_flush([[13, "clubs"],[14, "clubs"],[2, "diamonds"]]))
