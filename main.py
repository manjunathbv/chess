"""
This is the main module for my chess game.
"""


import random
import Canvas
import utils
import board
import Player
import globVar
import pathlib

def main():
    path = pathlib.Path("chess.save")
    if path.exists():
        Canvas.loadSave()
        running = True
    else:
        running = Canvas.startScreen()

    while(running):
        running = state()


def state():

    playing = True

    while playing:
        if (globVar.playerCount % 2) == 0:
            globVar.player = "W"
        else:
            globVar.player = "b"

        Player.turn()
        globVar.playerCount += 1
        #TODO clear and write save
        utils.clearSave()
        utils.writeSave()

        playing = utils.checkWin()

    return playing



if __name__ == "__main__":
    main()
