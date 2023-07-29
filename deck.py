import random


class Card:
    def __init__(self, suit, value, points, location="DECK"):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param value: The value of the card, e.g 3 or King
        """
        self._suit = suit.capitalize()
        self._value = value
        self._points = points
        self._location = location

    # TEST FUNCTION
    # remove?
    def __repr__(self): 
        return "Card suit:% s value:% s points:% s location:% s" % (self._suit, self._value, self._points, self._location) 

    def get_suit(self):
        return self._suit
    
    def get_value(self):
        return self._value
    
    def get_location(self):
        return self._location
    

class Deck:
    def __init__(self):
        # create deck full of Card objects
        self.card_values = {
            'Ace': 11,  # ace default value is 11, change to 1 when needed
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10
        }
        self._suits = ["\u2660", "\u2665", "\u2666", "\u2663"]  # unicode symbols for spades, hearts, diamonds, clubs
        self._deck = []

        for suit in self._suits:
            for key in self.card_values:
                self._deck.append(Card(suit, key, self.card_values[key]))

    def shuffleDeck(self):
        for i in range(random.randint(1,3)):
            random.shuffle(self._deck)  # shuffle the deck a random amount of times, between 1-3 (inclusive)

    # TEST FUNCTION
    def showDeck(self):
        count = 0
        for card in self._deck:
            print([card])
            count += 1
        print("There are", count, "cards")

    def getACard(self):
        return self._deck.pop()
