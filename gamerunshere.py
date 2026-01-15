from maingame import *
from map_module import *
from loading import *
from victory_or_lose import *


# Huvudprogrammet <3
def maingame_start():
    game_loading()
    map_creation()
    startgame()
    player = class_chooser()
    maingame(player)
    victory_or_loosory(player)
    endcredits()

if __name__ == "__main__":
    maingame_start()