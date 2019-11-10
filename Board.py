from tkinter import *
import tkinter.messagebox
import numpy as np

tk = Tk()

class Board:
    def __init__(self, tk):
        self.tk = tk
        self.tk.title("Tic Tac Toe")
        self.cases = np.zeros((3, 3), dtype=object)
        self.players = np.zeros(2, dtype=object)
        self.new_game()
        self.lineWinner =[[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6],]

    def new_game(self):
        self.turn = 1
        self.endGame = FALSE
        for i in range(3):
            for j in range(3):
                self.case(i, j)

    def show(self):
        self.tk.mainloop()

    def case(self, row, col):
        button = Button(self.tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: self.btnClick(button))
        button.grid(row=row, column=col)
        self.cases[row][col] = button


    def btnClick(self, buttons):
        if(buttons["text"] == " " and self.endGame == FALSE):
            buttons["text"] = "X" if self.turn % 2 == 1 else "O"
            winner = self.hasWon()
            if winner:
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "Winner is "+ "player 1" if self.turn % 2 == 1 else "player 2")

            self.addTurn()

    def addPlayer(self, player, num):
        self.players[num-1] = player

    def addTurn(self):
        self.turn = self.turn + 1

    def hasWon(self):
        if self.turn > 4 :
            simpleArray = self.simpleArray()
            for i in range(len(self.lineWinner)):
                a, b, c = self.lineWinner[i]
                if simpleArray[a] != " " and simpleArray[a] == simpleArray[b] and simpleArray[a] == simpleArray[c]:
                    return True

        return False

    def simpleArray(self):
        simpleArray = []
        for row in range(3):
            for col in range(3):
                simpleArray.append(self.cases[row][col]["text"])

        return simpleArray



board = Board(tk)
board.show()
