from time import sleep
from os import system, name
import view
import model
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--players", type=int, help="Enter number of players. Default is set to 1",
                    default=1)
parser.add_argument("--timeToMemorize", type=int, help="Enter number of seconds cards stay open until closing. Default is set to 3",
                    default=2)
parser.add_argument("--cardsInRow", type=int, help="Enter number of cards in Row. Default is 13",
                    default=13)
args = parser.parse_args()
print("\n")
gameModel = model.Game(args.players, args.timeToMemorize)
gameView = view.View(gameModel, numberOfCardsInRow=args.cardsInRow)
gameView.clear()
gameView.displayBoard()


while (not gameModel.isGameOver()):
    print("\n")
    gameView.displayPlayerTurn()
    userInput = input("Open Card : ")
    try:
        userInput = int(userInput)
    except:
        continue
    if gameModel.openedCard1 and gameModel.openedCard1.position == userInput:
        continue
    if int(userInput) in gameModel.matchedPositions:
        continue
    gameModel.selectCard(userInput)
    gameView.clear()
    gameView.displayBoard()

    if gameModel.openedCard1 and gameModel.openedCard2:
        if (gameModel.isMatch()):
            gameView.displayIsMatch(True)
            gameModel.playerScores[gameModel.currentPlayerTurn] += 1
            gameModel.removeCards()
            if(gameModel.isGameOver()):
                gameView.displayScores()

        else:  # not a match
            gameView.displayIsMatch(False)
            gameModel.foldCards()
            gameModel.passTurn()
            sleep(2)
            gameView.clear()
            gameView.displayBoard()
