from deck import *
from playGame import *
from cardRenders import *
from leaderboard import *
from InquirerPy import inquirer

leaderboard = Leaderboard()

def main():
    file = open('./assets/header.txt', 'r', encoding='utf-8')
    header = file.read()
    print(header)

    final_confirm = "No"
    choice = mainMenu()

    while final_confirm != "Yes":
        if choice == 'Start Game':
            play_again, navigation = playGame()  # returns a tuple based on gameOver() or choice in playGame()

            while play_again == True and navigation == "Play Again":
                play_again, navigation = playGame()  # jump right back into another game without having to start over at the main menu

            if play_again == False and navigation == "Exit":
                break  # exit program
        elif choice == 'Leaderboard':
            leaderboard.leaderboardMenu()
        else:
            final_confirm = inquirer.select(
                message="Are you sure you want to quit?",
                choices=["Yes", "No"]
            ).execute()
            if final_confirm == "Yes":
                break
        if choice == "Start Game" or choice == "Leaderboard":
            print(header)  # print header again when returning from a game or leaderboard
        choice = mainMenu()

    exitGame()


def mainMenu():
    selection = inquirer.select(
        message="Welcome to Blackjack! Select:",
        choices=["Start Game", "Leaderboard", "Exit"],
    ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()

    while not confirm:
        selection = inquirer.select(
            message="Welcome to Blackjack! Select:",
            choices=["Start Game", "Leaderboard", "Exit"],
        ).execute()
        confirm = inquirer.confirm(message="Confirm?").execute()

    return selection

def playGame():
    selection = inquirer.select(
        message="Select the deck size:",
        choices=["1 Deck (52 cards)", "2 Decks (104 cards)", "3 Decks (156 cards)"],
    ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()

    while not confirm:
        selection = inquirer.select(
            message="Select the deck size:",
            choices=["1 Deck (52 cards)", "2 Decks (104 cards)", "3 Decks (156 cards)"],
        ).execute()
        confirm = inquirer.confirm(message="Confirm?").execute()
        
        if selection == "3 Decks (156 cards)":
            deck_size = 3
        elif selection == "2 Decks (104 cards)":
            deck_size = 2
        elif selection == "1 Deck (52 cards)":
            deck_size = 1

    if selection == "3 Decks (156 cards)":
        deck_size = 3
    elif selection == "2 Decks (104 cards)":
        deck_size = 2
    elif selection == "1 Deck (52 cards)":
        deck_size = 1

    game = Game(deck_size)
    game.dealersHand()
    game.playersHand()
    game.calculateHandTotal(game.get_person("Player"))
    if game.get_person("Player").get_total() == 21:
        game.lucky21()
    else:
        game.gameStatus()

    choice = gameOptions()
    while game.get_person("Dealer").get_wins() <= 3:
        # if game.get_person("Player").get_total() == 21:  # lucky first blackjack
        #     game.lucky21()

        if choice == "Hit":
            game.hit(game.get_person("Player"))
            game.calculateHandTotal(game.get_person("Player"))
        elif choice == "Stay":
            game.dealersTurn()
        else:
            final_confirm = inquirer.select(
                message="Are you sure you want to quit playing the game? You \n will be brought back to the Main Menu.",
                choices=["Yes", "No"]
            ).execute()
            if final_confirm == "Yes":
                return (False, "Main Menu")

        if choice == "Stay" or game.get_person("Player").get_total() > 21:
            game.roundOver()  # end the round if the player chooses to stay or busts

        if game.get_person("Player").get_total() == 21:
            game.lucky21()

        if game.get_person("Dealer").get_wins() >= 3:
            break  # end game if dealer gets 3 wins
        
        game.dealersHand()
        game.playersHand()
        game.gameStatus()
        choice = gameOptions()

    print("Game over! Here's your total wins:", game.get_person("Player").get_wins())
    return gameOver(game.get_person("Player").get_wins())  # return T/F choice to play again

def gameOptions():
    option = inquirer.select(
        message="Your turn! Choose an option:",
        choices=["Hit", "Stay", "Quit"]
    ).execute()

    return option

def gameOver(score):
    leaderboard.newHighScore(score)  # update leaderboard if new high score is found
   
    selection = inquirer.select(
        message="Would you like to play again?",
        choices=["Yes", "No"],
    ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()

    while not confirm:
        selection = inquirer.select(
            message="Would you like to play again?",
            choices=["Yes", "No"],
        ).execute()
        confirm = inquirer.confirm(message="Confirm?").execute()
    
    if selection == "Yes":
        return (True, "Play Again")
    else:
        selection = inquirer.select(
            message="Would you like to go back to the Main Menu or exit the game?",
            choices=["Main Menu", "Exit"],
        ).execute()
        confirm = inquirer.confirm(message="Confirm?").execute()

        while not confirm:
            selection = inquirer.select(
                message="Would you like to go back to the Main Menu or exit the game?",
                choices=["Main Menu", "Exit"],
            ).execute()
            confirm = inquirer.confirm(message="Confirm?").execute()

        if selection == "Main Menu":
            return (False, "Main Menu")
        else:
            return (False, "Exit")

def exitGame():
    file = open('./assets/closingMessages.txt', 'r', encoding='utf-8')
    exitMsg = file.read()
    print(exitMsg)



if __name__ == "__main__":
    main()