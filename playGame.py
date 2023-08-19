import requests
import json
import os
from deck import Deck
from cardRenders import *

url = f'http://localhost:5000/api/'

class Player():
    def __init__(self, name):
        self._name = name
        self._hand = []
        self._hits = []  # store hits separately
        self._total = 0
        self._wins = 0
        self._turn = False  # dealers turn flag

    def get_name(self):
        return self._name()
    
    def get_hand(self):
        return self._hand
    
    def get_hits(self):
        return self._hits
    
    def get_total(self):
        return self._total
    
    def get_wins(self):
        return self._wins
    
    def get_turn(self):
        return self._turn
    
    def set_hand(self, card):
        self._hand.append(card)

    def set_total(self, total):
        self._total = total

    def set_wins(self, win):
        self._wins += win

    def set_turn(self, toggle):
        self._turn = toggle

    def discard_hand(self):
        self._hand = []
        self._hits = []
        self._total = 0
    

class Game():
    def __init__(self, deck_size):
        """
        Creates the initial game state with a deck, discard pile, dealer, and player.
        """
        self._playing_deck = Deck(self.createDeck(deck_size))
        self._discard_pile = []
        self._dealer = Player("Dealer")
        self._player = Player("Player")        
        self.deal()

    def createDeck(self, deck_amount):
        try:
            response = requests.get(f'{url}shuffle?numDecks={deck_amount}').json()
            return response['cards']  # extract array
        except requests.exceptions.RequestException as error:
            print(f'Test: Invalid Request (numDecks = {deck_amount})', error.response.json())

    def deal(self):
        # deal starting cards to player and dealer, alternating between the two
        if self._playing_deck.getDeckSize() <= 5:
            self.reshuffleDeck((self._playing_deck.convertToArray() + self._discard_pile))
        for i in range(4):
            if i % 2 == 0:
                self._player.set_hand(self._playing_deck.getACard())
            else:
                self._dealer.set_hand(self._playing_deck.getACard())

    def get_playing_deck(self):
        return self._playing_deck
    
    def get_discard_pile(self):
        return self._discard_pile
    
    def get_person(self, player):
        if player == "Dealer":
            return self._dealer
        else:
            return self._player
        
    def gameStatus(self):
        dealersHand = self._dealer.get_total()
        if dealersHand == 0 and self._dealer.get_turn() == False:
            dealersHand = "?"  # use default ? when dealer's card is hidden

        print("Dealer's Hand:", dealersHand, "VS", "Player's Hand:", self._player.get_total())
        print("Wins:", self._player.get_wins())
    
    def hit(self, player):
        """
        Wrapper function for getting a card.
        """
        # combine discard pile and deck to reshuffle
        if self._playing_deck.getDeckSize() <= 5:
            self.reshuffleDeck((self._playing_deck.convertToArray() + self._discard_pile))
        card = self._playing_deck.getACard()  # adds card to players hit array
        player._hits.append(card)
    
    def calculateHandTotal(self, player):
        temp_total = 0
        total_cards = player.get_hand() + player.get_hits()

        aces = [total_cards.pop(index) for index, card in enumerate(total_cards) if "Ace" in card.get_value()]

        for card in total_cards:  # add non ace cards first
            temp_total += card.get_points()

        for card in aces:  # add ace card(s), changing its points to 1 if 11 leads to a bust
            if (temp_total + card.get_points()) > 21:
                card.set_points(1)
            temp_total += card.get_points()

        player.set_total(temp_total)

    def dealersHand(self):
        if self._dealer.get_turn() == False:
            print(dealerCards(self._dealer.get_hand()))
        else:
            if(len(self._dealer._hits) > 0):
                print(halfFaceUpCards(self._dealer._hits))
            print()
            print(faceUpCards(self._dealer.get_hand()))

    def dealersTurn(self):
        """
        Algorithm for dealer's turn. 
        """
        if self.calculateHandTotal(self._dealer) == 21:  # if dealer has 21 from the start
            self._dealer.set_turn(True)
            return

        while self._dealer.get_total() < 17 and self._dealer.get_total() < 22:
            if self._playing_deck.getDeckSize() <= 5:
                self.reshuffleDeck((self._playing_deck.convertToArray() + self._discard_pile))
            self.hit(self.get_person("Dealer"))
            self.calculateHandTotal(self.get_person("Dealer"))

        self._dealer.set_turn(True)

    def playersHand(self):
        print(faceUpCards(self._player.get_hand()))
        print()
        if(len(self._player._hits) > 0):
            print(halfFaceUpCards(self._player._hits))

    def roundOver(self):
        """
        Gather Dealer and Player's hands & hits and add to the discard pile.
        Deal new cards for both.
        """
        self.calculateHandTotal(self.get_person("Dealer"))
        self.calculateHandTotal(self.get_person("Player"))
        dealer_total = self._dealer.get_total()
        player_total = self._player.get_total()
        if self._dealer.get_turn() == False:
            self.dealersTurn()
      
        self.dealersHand()  # print results
        self.playersHand()
        self.gameStatus()

        if dealer_total > 21:
            print("Dealer bust! You win! Onto the next round...")
            self._player.set_wins(1)
        elif player_total > 21:
            print("It's a bust! You lose! Onto the next round...")
            self._dealer.set_wins(1)
        elif dealer_total == 21 and player_total != 21:
            print("21! Dealer wins! Onto the next round...")
            self._dealer.set_wins(1)
        elif player_total == 21 and dealer_total != 21:
            print("21! You win!  Onto the next round...")
            self._player.set_wins(1)
        elif dealer_total > player_total and dealer_total <= 21:  # dealer wins
            print("Dealer wins! Onto the next round...")
            self._dealer.set_wins(1)
        elif dealer_total < player_total and player_total <= 21:  # player wins
            print("You win! Onto the next round...")
            self._player.set_wins(1)

        # if dealer_total == player_total there is a tie, no wins are recorded
        if dealer_total == player_total:
            print("Tie! Nobody wins. Onto the next round...")        

        self.discard("Dealer")  # add Dealer & Player's hands to discard pile
        self.discard("Player")
        self._dealer.discard_hand()  # reset Dealer & Player's hand[], hits[], and total=0
        self._player.discard_hand()

        if self._playing_deck.getDeckSize() <= 5:
            self.reshuffleDeck((self._playing_deck.convertToArray() + self._discard_pile))
        
        self.deal()  # deal new cards for new round and recalculate player's hand
        self._dealer.set_turn(False)
        self.calculateHandTotal(self._player)

    def lucky21(self):
        """
        Function to handle the player immediately having 21 in their starting hand.
        """
        self.dealersTurn()  # do dealer's turn incase of tie
        self.roundOver()

        while self._player.get_total() == 21:
            self.dealersTurn()
            self.roundOver()

        return

    def discard(self, person):
        current_person = self.get_person(person)
        pile = current_person.get_hand() + current_person.get_hits()

        for card in pile:
            self._discard_pile.append(card)

        current_person.discard_hand()

    def reshuffleDeck(self, deck):
        try:
            headers = {'Content-Type': 'application/json'} 
            request_body = json.dumps({"cards": deck})
            response = requests.put(f'{url}reshuffle', data=request_body, headers=headers).json()
            self._playing_deck = Deck(response['cards']) # recreate a Deck object using the response array
        except requests.exceptions.RequestException as error:
            print(f'Test: Invalid Request (cards = ${deck})', error.response.json())
