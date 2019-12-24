import model
from time import sleep
from os import system, name


class View:
    def __init__(self, model, numberOfCardsInRow):
        self.model = model
        self.numberOfCardsInRow = numberOfCardsInRow

    def displayBoard(self):
        count = 0
        for card in self.model.board:
            if count == self.numberOfCardsInRow:
                print("\n")
                count = 0
            card.printCard()
            count += 1
        print("\n")

    def displayScores(self):
        score = self.model.calculateScore()
        if len(score["winners"]) == 1:
            print('\33[32m' + "Player " + str(score["winners"][0] + 1) +
                  " wins! Score:" + str(score["score"]) + '\033[0m')
        else:
            winners = ""
            for player in score["winners"]:
                winners += "Player" + str(player + 1) + " "
            print('\33[34m' + "Tie! " + winners +
                  "wins! Score: " + str(score["score"]) + '\033[0m')

    def clear(self):

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

        # prevents scroll
        system("printf '\033c'")

    def displayPlayerTurn(self):
        print("Player " + str(self.model.currentPlayerTurn + 1) + "'s turn.")

    def displayIsMatch(self, isMatch):
        if isMatch:
            print('\33[32m' + "Match!\n" + '\033[0m')
        else:
            print('\33[34m' + "Not a Match.\n" + '\033[0m')
