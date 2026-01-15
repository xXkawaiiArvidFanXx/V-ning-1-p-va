from maingame import *
from map_module import *
from loading import *
from victory_or_lose import *


# Huvudprogrammet <3
def maingame_start(map):
    #game_loading()
    map_creation()
    load_or_save=startgame()
    if load_or_save != "load_game":
        player = class_chooser()
    else:
        player, map = load_game()
    
    save_loss_or_win = maingame(player)
    
    if save_loss_or_win != "save_game":
        victory_or_loosory(player)
#        endcredits()

    else:
        save_game(player, map)
    print("Spelet avslutas....")

if __name__ == "__main__":
    maingame_start(map)
