class Card:
    """Card class for representing and manipulating one playing card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

    def get_value(self):
        """ A reader method that returns the blackjack value of the card"""
        return self.value

    def assign_value(self, rank):
        """A helper function to determine the blackjack value of a rank"""
        print("The assignValue method needs to be completed")
        values = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        return values[rank]