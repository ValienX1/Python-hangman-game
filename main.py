from nrGuess import NumberGuess
from hangman import Hangman
import storage as st
import ui

# In this project are used windows only functions


def main():
    st.init()
    ui.clear()
    name = st.get("name")
    if name == "":
        name = ui.inputFor("name")
        st.add("name", name)
    while True:
        ui.clear()
        gNr = ui.inputFor("main", name)
        if gNr.isdigit():
            if int(gNr) == 1:
                NumberGuess()
            elif int(gNr) == 2:
                Hangman()
        elif gNr.lower() == "q":
            ui.clear()
            break
    st.save()


if __name__ == "__main__":
    main()
