from deck import Deck
from cardRenders import *

class Player():
    def __init__(self, name):
        self._name = name
        self._hand = []
        self._hits = []  # store hits separately
        self._total = 0
        self._pot = 500  # start with $500?

    def get_name(self):
        return self._name()
    
    def get_hand(self):
        return self._hand
    
    def get_hits(self):
        return self._hits
    
    def get_total(self):
        return self._total
    
    def get_pot(self):
        return self._pot
    
    def set_hand(self, card):
        self._hand.append(card)

    def discard_hand(self):
        self._hand = []
        self._hits = []
        self._total = 0
    

class Game():
    def __init__(self):
        """
        Creates the initial game state with a deck, discard pile, dealer, and player.
        """
        self._playing_deck = Deck()
        self._discard_pile = []
        self._dealer = Player("Dealer")
        self._player = Player("Player")

        self._playing_deck.shuffleDeck()
        self.deal()

        # # deal starting cards to player and dealer, alternating between the two
        # for i in range(4):
        #     if i % 2 == 0:
        #         self._player.set_hand(self._playing_deck.getACard())
        #     else:
        #         self._dealer.set_hand(self._playing_deck.getACard())

    def get_playing_deck(self):
        return self._playing_deck
    
    def get_discard_pile(self):
        return self._discard_pile
    
    def get_person(self, player):
        if player == "Dealer":
            return self._dealer
        else:
            return self._player
    
    def get_player(self):
        return self._player
    
    def deal(self):
        # deal starting cards to player and dealer, alternating between the two
        for i in range(4):
            if i % 2 == 0:
                self._player.set_hand(self._playing_deck.getACard())
            else:
                self._dealer.set_hand(self._playing_deck.getACard())
    
    def hit(self):
        """
        Wrapper function for getting a card.
        """
        card = self._playing_deck.getACard()  # adds card to players hit array
        self._player._hits.append(card)
        # calculateHandTotal(self._player._hits)
        return card
    
    def calculateHandTotal(self, hand):
        # temp_total = 0
        pass


    
    def bet(self):
        """
        Betting process for the player.
        """
        bet = int(input("Enter your bet (whole numbers only): $"))
        print("You bet $" + str(bet))

    def dealersHand(self, turn=False):
        if turn is False:
            print(dealerCards(self._dealer.get_hand()))
        else:
            print(faceUpCards(self._dealer.get_hand()))

    def dealersTurn(self):
        """
        Algorithm for dealer's turn. 
        """
        pass

    def playersHand(self):
        print(faceUpCards(self._player.get_hand()))
        if(len(self._player._hits) > 0):
            print(halfFaceUpCards(self._player._hits))

    def discard(self, person):
        current_person = self.get_person(person)
        pile = current_person.get_hand() + current_person.get_hits()

        for card in pile:
            self._discard_pile.append(card)

        current_person.discard_hand()

    def reshuffleDeck(self):
        pass
        # put discard pile back into deck
        # ...but you can't since the Deck is inaccessible???
