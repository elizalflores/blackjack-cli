class Card:
    def __init__(self, suit, value, num_value, location):
        """
        Creates a card with a suit, value, and its current location.
        """
        self._suit = suit
        self._value = value
        self._num_value = num_value
        self._location = location

    def __repr__(self): 
        return "Card suit:% s value:% s num_value:% s location:% s" % (self._suit, self._value, self._num_value, self._location) 

    def get_suit(self):
        return self._suit
    
    def get_value(self):
        return self._value
    
    def get_location(self):
        return self._location
    

class Deck:

    def __init__(self):
        # create deck full of Card objects
        self._values = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
        self._suits = ["\u2663", "\u2665", "\u2666", "\u2660"]  # unicode symbols for clubs, hearts, diamonds, spades
        self._deck = []

        for suit in self._suits:
            for key in self._values:
                self._deck.append(Card(suit, key, self._values[key], "DECK"))

    def showDeck(self):
        count = 0
        for card in self._deck:
            print([card])
            count += 1
        print("There are", count, "cards")
