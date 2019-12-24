
from os import system, name
from time import sleep
import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.visible = False

    def turnCard(self):
        self.visible = not self.visible

    def printCard(self):

        def spacePadding(num):
            strVal = str(num)
            strValLen = len(strVal)
            if self.visible:
                if strValLen == 1:
                    strVal += " "
            else:
                if strValLen == 1:
                    strVal += "  "
                elif strValLen == 2:
                    strVal += " "
            return strVal

        if self.visible:
            strVal = spacePadding(self.value)
            print('\33[33m' + '[' + self.suit +
                  strVal + ']' + '\033[0m', end=" ")

        elif self.position == ' X':
            strVal = spacePadding(self.position)
            print('\33[30m' + '[' +
                  strVal + ']' + '\033[0m', end=" ")
        else:
            strVal = spacePadding(self.position)
            print('[' + strVal + ']', end=" ")


class Game:

    def __init__(self, playerCount, memorizeTimeSec):
        self.playerCount = playerCount
        self.memorizeTimeSec = memorizeTimeSec    # before failed match cards flip back
        self.playerScores = dict((k, 0) for k in range(playerCount))
        self.currentPlayerTurn = 0
        self.board = None
        self.matchedPositions = []
        self.openedCard1 = None
        self.openedCard2 = None
        self.generateBoard()

    def generateBoard(self):
        deck = []
        suits = ["♠", "♡", "♢", "♣"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9,
                  10, "J", "Q", "K"]
        # Testing game completion
        # suits = ["♠", "♡"]
        # values = ["A", 2, 3, 4]

        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        random.shuffle(deck)
        for i, card in enumerate(deck):
            card.position = i+1
        self.board = deck
        return deck

    def selectCard(self, position):
        position = int(position)
        selectedCard = None
        for card in self.board:
            if card:
                if card.position == position:
                    card.turnCard()
                    selectedCard = card
        if selectedCard == None:
            Exception("chosen card position doesn't exist on board.")
        if self.openedCard1 is None:
            self.openedCard1 = selectedCard
        else:
            self.openedCard2 = selectedCard

        return

    def passTurn(self):
        self.currentPlayerTurn = (
            self.currentPlayerTurn + 1) % self.playerCount

    def foldCards(self):
        self.openedCard1.turnCard()
        self.openedCard2.turnCard()
        self.openedCard1 = None
        self.openedCard2 = None

    def removeCards(self):
        self.matchedPositions.append(self.openedCard1.position)
        self.matchedPositions.append(self.openedCard2.position)
        self.openedCard1.position = ' X'
        self.openedCard2.position = ' X'

        self.foldCards()

    def isMatch(self):
        return self.openedCard1.value == self.openedCard2.value

    def isGameOver(self):
        count = 0
        for card in self.board:
            if card.position != ' X':
                return False
            else:
                count += 1
        return count == len(self.board)

    def calculateScore(self):
        score = 0
        winners = []  # for ties
        for player in self.playerScores:

            if self.playerScores[player] == score:
                winners.append(player)

            elif self.playerScores[player] > score:
                score = self.playerScores[player]
                winners = [player]

        return {"winners": winners, "score": score}
