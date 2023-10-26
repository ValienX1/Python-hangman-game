from msvcrt import getch
from os import system


def inputFor(*args) -> str:
    return input(message(*args))


def prt(msg) -> None:
    print(msg)


def message(*args) -> str:
    try:
        if args[0] == "NGinput":
            return f"Give a number between 0 and 9 both included. \nOr press Q to quit. Try {args[1]}\n"
        elif args[0] == "NGwin":
            return "You have won!'\nPress any Key to try again or Q to quit"
        elif args[0] == "NGlost":
            return f"You have lost!'\n The number was {args[1]}. \nPress any key to continue or Q to quit."
        elif args[0] == "NGmiss":
            return f"Given number {args[1]} is not correct answer.\nPress any key to continue or Q to quit"
        elif args[0] == "NGwrong":
            return "Given input is not number between 0 and 9 and not Q to quit\nPress ay Key to continue."
        elif args[0] == "name":
            return "Please Enter your name: "
        elif args[0] == "wordsNotFound":
            return "Words not found!\nPress any key to close the game"
        elif args[0] == "main":
            return f"Welcom {args[1]}!\n1. Number Guess\n2. Hangman\nPlease choose the game number (q == Quit): "
        elif args[0] == "hangMenu":
            return "P -> Play\nQ -> Quit"
        elif args[0] == "Hwin":
            return "You have won!'\nPress any Key to try again or Q to quit"
        elif args[0] == "Hlost":
            return "You have lost!'\nPress any Key to try again or Q to quit"
        elif args[0] == "Hstep":
            return "Type a letter or press ESC to quit."
        elif args[0] == "":
            return "Empty Message"
        else:
            return str(args[0])
    except:
        return "UI message Arguments error"


def wait(*args) -> str:
    print(message(*args))
    return bytes.decode(getch())


def clear() -> None:
    system("cls||clear")
