import numpy as np

# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: Wacky Packages
# Kruize Christensen      
# Last Modified: November 20, 2019               
# ---------------------------------------------
# Gave discriptions of each written program above each individual one.
# ---------------------------------------------

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many
                                , dtype=WackyPackageCard)


#gives the information on each card

    def read_series_information(self,file):
        count = 0
        data = open(file, "r")

        for line in data:
            info = line.strip("\n").split(",")
            self.cards[count] = WackyPackageCard(int(info[0]), info[1], float(info[2]))
            count += 1
        data.close()

# calculates what you have

    def read_collection_information(self,file):
        data = open(file, "r")

        i = 0

        for line in data:
            info = line.split(",")
            a = 0
            for cards in self.cards:
                if (info[0].lower().strip().replace(" ", "") == self.cards[a].get_description().lower().replace(" ", "")):
                    self.cards[a].set_cards_owned(self.cards[a].get_cards_owned()+1)
                a += 1
            i += 1
# calculats the price of how much you own  

    def collection_value(self):
        a = 0
        value = 0
        for cards in self.cards:
            if self.cards[a].get_cards_owned() > 0:
                value += (self.cards[a].get_value()*self.cards[a].get_cards_owned())     
            a+=1
        return value
                
#gets how many you don't have and calculates the cost it will to buy all of them            
    
    def determine_missing_information(self):
        a = 0
        value = 0
        num = 0
        for cards in self.cards:
            if self.cards[a].get_cards_owned() == 0:
                value += self.cards[a].get_value()
                num += 1
            a+=1
        return num, value

# Aranges the output of the information in the terminal
 
    def __str__(self):
        x = " "
        answer = ("My " + str(self.year) + " collection of " + self.manufacturer + "Wacky Packages\n")
        answer += ("Number" + 4*x + "Description" + 19*x + "Value" + 5*x + "Owned\n")
        answer += ("------" + 4*x + "-----------" + 19*x + "------" + 5*x + "------\n")
        for card in self.cards:
            answer += str(card) + "\n"
        return answer

    

# Place the missing methods here.  Do not modify the code below or above.

# ---------------------------------------------

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_cards_owned(self):
        return self.cards_owned

    def set_cards_owned(self, number):
        self.cards_owned = number

# ---------------------------------------------

def main():
    my_collection = WackyPackageSeries("Topps", 1973, 30)
    my_collection.read_series_information("series1.csv")
    print(my_collection)
    my_collection.read_collection_information("mycards.csv")
    print(my_collection)
    print("Value of collection = ${:.2f}".format(my_collection.collection_value()))
    number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    print("Number of missing cards =", number_of_missing_cards)
    print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))
    
# ---------------------------------------------

main()
