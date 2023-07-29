from deck import *
from playGame import *
from cardRenders import *
from InquirerPy import inquirer


def main():

    file = open('./assets/header.txt', 'r', encoding='utf-8')
    header = file.read()
    print(header)

    final_confirm = "No"
    choice = mainMenu()

    while final_confirm != "Yes":
        if choice == 'Start Game':
            playGame()
        elif choice == 'Leaderboard':
            print("LEADERBOARD UNDER CONSTRUCTION")
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
            message="",
            choices=["Start Game", "Leaderboard", "Exit"],
        ).execute()
        confirm = inquirer.confirm(message="Confirm?").execute()

    return selection

def playGame():
    playing = True

    game = Game()
    game.dealersHand()
    game.playersHand()

    choice = gameOptions()
    while playing:
        if choice == "Hit":
            print("HIT UNDER CONSTRUCTION")
        elif choice == "Bet":
            game.bet()
            
        elif choice == "Stay":
            print("STAY UNDER CONSTRUCTION")
            # dealer's turn algorithm
        else:
            final_confirm = inquirer.select(
                message="Are you sure you want to quit playing the game? You \n will be brought back to the Main Menu.",
                choices=["Yes", "No"]
            ).execute()
            if final_confirm == "Yes":
                break

        print("Gameplay here...")
        showCards()
        choice = gameOptions()
    
def showCards():
    pass

def gameOptions():
    option = inquirer.select(
        message="Your turn! Choose an option:",
        choices=["Hit", "Stay", "Bet", "Quit"]
    ).execute()

    return option
    
def viewLeaderboard():
    pass

def exitGame():
    file = open('./assets/closingMessages.txt', 'r', encoding='utf-8')
    exitMsg = file.read()
    print(exitMsg)



if __name__ == "__main__":
    main()