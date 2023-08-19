from InquirerPy import inquirer

class Leaderboard:

    def __init__(self):
        self._leaderboard = [
            {"BLK" : 10},
            {"JCK" : 9},
            {"CHR" : 8},
            {"KEV" : 7},
            {"EVA" : 6},
            {"ELI" : 5},
            {"RCH" : 4},
            {"JSN" : 3},
            {"VIC" : 2},
            {"AAA" : 1}
        ]

    def get_leaderboard(self):
        return self._leaderboard

    def showLeaderboard(self):
        print("NAME", "SCORE")
        for index, entry in enumerate(self._leaderboard):
            name, score = list(entry.items())[0]
            print(name, " " , score)

    def newHighScore(self, new_high):
        index_to_replace = 0
        new_name = input("Enter your 3-letter, uppercase initials: ")
        new_score = {new_name: new_high}

        for index, entry in enumerate(self._leaderboard):
            name, score = list(entry.items())[0]
            if new_high > score:
                index_to_replace = index
                break

        # Replace the entry if a higher score is found
        if index_to_replace is not None:
            self._leaderboard[index_to_replace] = new_score

        self._leaderboard = sorted(self._leaderboard, key=lambda x: list(x.values())[0], reverse=True)


    def leaderboardMenu(self):
        self.showLeaderboard()
        choice = self.leaderboardSelect()

        if choice == "Exit":
            return

    def leaderboardSelect(self):
        selection = inquirer.select(
            message="HIGH SCORES Select:",
            choices=["Exit"],
        ).execute()
        confirm = inquirer.confirm(message="Confirm?").execute()

        while not confirm:
            selection = inquirer.select(
                message="HIGH SCORES Select:",
                choices=["Exit"],
            ).execute()
            confirm = inquirer.confirm(message="Confirm?").execute()

        return selection