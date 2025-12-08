from maingame import *
from map_module import *
from loading import *




# Huvudprogrammet <3
def maingame_start():
    Map_Creation()
    startgame()
    player = class_chooser()
    maingame(player)


if __name__ == "__main__":
    maingame_start()