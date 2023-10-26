from os.path import exists
import json
from typing import List

model = {
    "name": "",
    "NumberGuess": {"wins": 0, "losses": 0},
    "Hangman": {"wins": 0, "losses": 0},
}

data = model

file = "storage.json"
hangmanDataFile = "hangman.json"


def init() -> None:
    global data
    if not exists(file):
        try:
            open(file, "x")
            json.dump(model, open(file, "w"))
        except:
            print("Settings File not found and couldn't create new one")
            data = model
    else:
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except:
            print("Settings file is not readable")
            data = model


def words() -> List[str]:
    if not exists(hangmanDataFile):
        print("Words not found")
        return None
    else:
        try:
            with open(hangmanDataFile, "r") as f:
                return list(filter(lambda w: len(w) > 4, json.load(f)["words"]))
        except:
            print("Words not found")
            return None


def get(atr) -> str:
    return "" if not atr in data else data[atr]


def won(game) -> None:
    data[game]["wins"] += 1


def lost(game) -> None:
    data[game]["losses"] += 1


def add(atr, value) -> None:
    data[atr] = value


def save() -> None:
    try:
        json.dump(data, open(file, "w"))
    except:
        print("Couldn't save settings.")
