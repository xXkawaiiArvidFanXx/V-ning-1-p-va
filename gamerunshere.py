from maingame import *
from map_module import *
from loading import *
from victory_or_loosory import *


# Huvudprogrammet <3
def maingame_start():
    game_loading()
    Map_Creation()
    startgame()
    player = class_chooser()
    maingame(player)
    victory_or_loosory(player)

if __name__ == "__main__":
    maingame_start()