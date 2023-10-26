import storage as st
import ui
from random import randint


class Hangman:
    def __init__(self) -> None:
        self.words = st.words()
        if not self.words:
            ui.wait("wordsNotFound")
            return
        self.board = Board()
        self.mistakes = 0
        self.pickWord()
        self.menu()

    def pickWord(self) -> None:
        word = self.words[randint(0, len(self.words) - 1)]
        self.word = [
            *map(
                lambda c: Letter(c[1], c[0], c[1] == word[0] or c[1] == word[-1]),
                enumerate([*word]),
            )
        ]

    def menu(self) -> None:
        ui.clear()
        res = ui.wait("hangMenu")

        if res.lower() == "p":
            self.play()
        elif res.lower() != "q":
            self.menu()

    def play(self) -> None:
        self.draw()
        ch = ui.wait("Hstep")
        if not ch == chr(27):
            if ch.isalpha() and not self.check(ch):
                self.mistakes += 1
            if self.won():
                st.won("Hangman")
                self.draw()
                if ui.wait("Hwin").lower() != "q":
                    self.restart()
            elif self.mistakes == self.board.max:
                st.lost("Hangman")
                self.draw("Hlost")
            else:
                self.play()

    def draw(self):
        ui.clear()
        ui.prt(" ".join(map(lambda l: l.str, self.word)))
        self.board.draw(self.mistakes)

    def restart(self) -> None:
        self.mistakes = 0
        self.pickWord()
        self.play()

    def check(self, l) -> bool:
        guessed = False
        for a in self.word:
            if a.char == l and a.guessed:
                return True
            elif a.char == l:
                a.guessed = guessed = True
        return guessed

    def won(self) -> bool:
        return len([x for x in self.word if x.guessed]) == len(self.word)


class Board:
    def __init__(self) -> None:
        self.steps = [
            Field(0, 0, "/"),
            Field(2, 0, "\\"),
            Field(1, 1, "|"),
            Field(1, 2, "|"),
            Field(1, 3, "|"),
            Field(1, 4, "|"),
            Field(1, 5, "_"),
            Field(2, 5, "_"),
            Field(3, 5, "_"),
            Field(4, 5, "_"),
            Field(5, 5, "_"),
            Field(5, 4, "|"),
            Field(5, 3, "O"),
            Field(5, 2, "|"),
            Field(4, 2, "/"),
            Field(6, 2, "\\"),
            Field(4, 1, "/"),
            Field(6, 1, "\\"),
        ]

    @property
    def max(self):
        return len(self.steps)

    def img(self, mistakes) -> str:
        s = ""
        for y in range(6):
            line = ""
            for x in range(7):
                line += self.get(x, y, mistakes)
            s = line + "\n" + s
        return s

    def get(self, x, y, mistakes):
        for i, a in enumerate(self.steps):
            if a.x == x and a.y == y and i < mistakes:
                return a.char
        return " "

    def draw(self, mistakes):
        print(self.img(mistakes))


class Field:
    def __init__(self, x, y, char) -> None:
        self.x = x
        self.y = y
        self.char = char
        pass


class Letter:
    def __init__(self, char, idx, guessed) -> None:
        self.char = char
        self.idx = idx
        self.guessed = guessed

    def __str__(self) -> str:
        return ("_", self.char)[self.guessed]

    def __repr__(self) -> str:
        return f"Letter: {self.char}, index: {self.idx}, guessed: {self.guessed}"

    @property
    def str(self):
        return ("_", self.char)[self.guessed]

    def guess(self, char):
        self.guessed = self.char == char
