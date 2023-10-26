from os import system
from random import randint as rand
import ui
import storage as st


class NumberGuess:
    allowedTries = 5

    def __init__(self) -> None:
        self.start()
        self.roll()

    def start(self) -> None:
        self.number = rand(0, 9)

    def roll(self) -> None:
        tries = 1
        while True:
            ui.clear()
            guess = ui.inputFor("NGinput", tries)
            if guess.lower() == "q":
                break
            if not guess.isdigit():
                ui.wait("NGwrong")
            else:
                if int(guess) == self.number:
                    st.won("NumberGuess")
                    if ui.wait("NGwin").lower() == "q":
                        break
                    tries = 1
                    self.number = rand(0, 9)
                elif tries == self.allowedTries:
                    st.lost("NumberGuess")
                    if ui.wait("NGlost", self.number).lower() == "q":
                        break
                    tries = 1
                    self.number = rand(0, 9)
                else:
                    tries += 1
                    if ui.wait("NGmiss", guess).lower() == "q":
                        break
        ui.clear()
