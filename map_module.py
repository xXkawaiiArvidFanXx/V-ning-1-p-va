#Här skapas en karta och rummen slumpas fram
#med funktionen Map_Creation skapas en ny karta
#med funktionen get_room_type() kan du få vad det är för typ av rum spelaren står i
import random as rand
from player import *
from soundengine import *

def map_creation():
    game_map = []
    
    for i in range (7): #En tom kart mall skapas
        game_map.append([0,0,0,0])

    for a in range (7):
        for b in range (4): #här slumpas rummens egenskaper fram N = Neutralt 
            #G = gott/GOOd O = Ont/OEvil   T = Trap/fälla B = BOSS (E = Empty)
            room_type = ["N","G","O","T"]
            game_map[a][b]=(room_type[rand.randint(0,3)])

    #förbestämda rum, bestämer två platser för bossar, samt gör det rummet man startar i till ett tomt rum
    game_map[3][1] = "B"
    game_map[2][2] = "B"
    game_map[6][3] = "E"
    return game_map

def illigal_move(player_pos_y, player_pos_x): #Säger om Spelaren går utanför kartan
    if player_pos_y < 0 or player_pos_y > 6 or player_pos_x < 0 or player_pos_x > 3:
        print("Du kan inte gå utanför kartan!")
        return True
    else:
        return False

def player_position(pos_y, pos_x): #När spelaren byter rum
    while True:
        player_move = input("Vart vill du gå? upp, ner, vänster, höger?\nAnvänd WASD\n").strip().lower()

        if player_move == "s":
            new_y, new_x = pos_y + 1, pos_x
        elif player_move == "w":
            new_y, new_x = pos_y - 1, pos_x
        elif player_move == "a":
            new_y, new_x = pos_y, pos_x -1
        elif player_move == "d":
            new_y, new_x = pos_y, pos_x + 1
        else:
            print("Ogiltig riktning — skriv 'W', 'S', 'A' eller 'D'.")
            continue

        if illigal_move(new_y, new_x):
            print("Du försöker att vara som harry potter och åka genom väggar. Olyckligtnog springer du rätt in i en stolpe som var lite oschyst placerat.")
            sound("ljud\stolpe.wav")
            continue

        return new_y, new_x

def get_room_type(player_pos_y, player_pos_x, game_map): #ger typen av rummet spelarn står i
    """player_pos_y, player_pos_x, game_map"""
    room = (game_map[player_pos_y][player_pos_x])

    if room == "N":
        return "Neutralt rum"
    elif room == "G":
        return "Gott rum"
    elif room == "O":
        return "Ont rum"
    elif room == "T":
        return "Fällrum"
    elif room == "B":
        return "Bossrum"
    elif room == "E":
        return "Tomt rum"
    
