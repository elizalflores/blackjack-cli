class Card:
    def __init__(self, suit, value, points):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param value: The value of the card, e.g 3 or King
        """
        self._suit = suit
        self._value = value
        self._points = points

    def get_suit(self):
        return self._suit
    
    def get_value(self):
        return self._value
    
    def get_points(self):
        return self._points
    
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