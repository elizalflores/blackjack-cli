from deck import *

def main():
    file = open('header.txt', 'r', encoding='utf-8')
    header = file.read()
    print(header)

    current_deck = Deck()  # test 
    current_deck.showDeck()


if __name__ == "__main__":
    main()