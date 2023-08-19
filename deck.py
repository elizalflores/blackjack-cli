import random


class Card:
    def __init__(self, suit, value, points, location="DECK"):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param value: The value of the card, e.g 3 or King
        """
        self._suit = suit
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
    
    def get_points(self):
        return self._points
    
    def get_location(self):
        return self._location
    
    def set_points(self, points):
        self._points = points  # USE CASE: Converting Ace from 11 to 1 when needed
    

class Deck:
    def __init__(self, deck):
        self._deck = []

        for card in deck:
            suit, rank = card.split(" ")
            if rank == "Ace":
                self._deck.append(Card(suit, rank, 11))
            elif rank == "Jack" or rank == "Queen" or rank == "King":
                self._deck.append(Card(suit, rank, 10))
            else:
                self._deck.append(Card(suit, rank, int(rank)))

    # TEST FUNCTION
    def showDeck(self):
        count = 0
        for card in self._deck:
            print([card])
            count += 1
        print("There are", count, "cards")

    def getACard(self):
        return self._deck.pop()
    
    def getDeckSize(self):
        return len(self._deck)

    def convertToArray(self):
        deck_array = []
        for card in self._deck:
            deck_array.append(str(card.get_suit()) + " " + str(card.get_value()))
        deck_array.sort()
        return deck_array