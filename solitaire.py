import random
BREAK_STRING = "-----------------------------------------------------"

class Card():
    card_to_name = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",
                    8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}

    def __init__(self, value, suit): 
        self.name = self.card_to_name[value]
        self.suit = suit
        self.title = "%s%s" % (self.name, self.suit)
        self.value = value
    
    def isBelow(self, card):
        return self.value == (card.value - 1)

    def isOppositeSuite(self, card):
        if self.suit == "club" or self.suit == "spade":
            return card.suit == "heart" or card.suit == "diam"
        else: 
            return card.suit == "spade" or card.suit == "club"
