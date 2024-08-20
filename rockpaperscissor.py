from tkinter import *
import random

class Logic:
    def __init__(self) -> None:
        pass

    def computerMove(self, choices: list[str]):
        return random.choice(choices)

    def winLoseTie(self, computerChoice, playerChoice):
        if computerChoice == playerChoice:
            return "It's a Tie"
        elif computerChoice == "Rock" and playerChoice == "Paper":
            return "Player Wins!"
        elif computerChoice == "Rock" and playerChoice == "Scissors":
            return "Player Loses"
        elif computerChoice == "Paper" and playerChoice == "Rock":
            return "Player Loses"
        elif computerChoice == "Paper" and playerChoice == "Scissors":
            return "Player Wins!"
        elif computerChoice == "Scissors" and playerChoice == "Rock":
            return "Player Wins!"
        elif computerChoice == "Scissors" and playerChoice == "Paper":
            return "Player Loses"

logic = Logic()

choices = ["Rock", "Paper", "Scissors"]
playerChoice = "Rock"
computerChoice = ""

def computerSendLogic():
    global computerChoice
    computerChoice = logic.computerMove(choices)
    ComputerChoice.config(text=computerChoice)
    checkResult()

def playerSendLogic():
    global playerChoice
    currentIndex = choices.index(playerChoice)
    playerChoice = choices[(currentIndex + 1) % 3]
    PlayerChoice.config(text=playerChoice)

def confirmChoice():
    computerSendLogic()

def checkResult():
    resultText = logic.winLoseTie(computerChoice, playerChoice)
    result.config(text=f"Result: {resultText}")

window = Tk()
window.geometry("500x500")
window.title("Rock Paper Scissors")
window.config(background="#06006d")

Title = Label(window, text="Rock Paper Scissors",
              font=("Arial", 20, "bold"),
              fg="white",
              bg="#06006d",
              bd=10)
Title.place(x=250, y=20, anchor="center")

PlayerTitle = Label(
    window,
    text="Player",
    font=("Arial", 20, "bold")
)
PlayerTitle.place(x=90, y=120, anchor=N)

PlayerChoice = Button(
    window,
    text=playerChoice,
    font=("Arial", 20, "bold"),
    width=10,
    height=2,
    command=playerSendLogic
)
PlayerChoice.place(x=100, y=200, anchor=N)

ConfirmButton = Button(
    window,
    text="Confirm",
    font=("Arial", 15, "bold"),
    width=10,
    height=2,
    command=confirmChoice
)
ConfirmButton.place(x=100, y=300, anchor=N)

ComputerTitle = Label(
    window,
    text="Computer",
    font=("Arial", 20, "bold")
)
ComputerTitle.place(x=330, y=120)

ComputerChoice = Button(
    window,
    text="?",
    font=("Arial", 20, "bold"),
    width=10,
    height=2
)
ComputerChoice.place(x=310, y=200)

result = Label(
    window,
    text="Result: ",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#06006d",
    bd=10
)
result.place(x=200, y=350)

window.mainloop()
