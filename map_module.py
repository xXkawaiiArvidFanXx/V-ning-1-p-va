#Här skapas en karta och rummen slumpas fram
#karta grid lista i lista 
#map = kartan
#Börja med map creation för att skapa kartan
#med funktionen Print_map() så kan du skriva ut kartan i terminalen
import random as rand
from player import *
def Map_Creation():
    map = []
    map_size = 7 #bestämmer storlek på kartan
    for i in range (map_size): #En tom kart mall skapas
        map.append([0,0,0,0])

    for a in range (map_size):
        for b in range (4): #här slumpas rummens egenskaper fram N = Neutralt 
            #G = gott/GOOd O = Ont/OEvil   T = Trap/fälla kanske R = Renoveras B = BOSS E= tomt rum
            Room_Type = ["N","G","O","T"]

            map[a][b]=(Room_Type[rand.randint(0,3)])

    #Bossmodul
    #Alltid en boss 1 i mittenrummet 
    #Boss 2 är alltid i sista rummet???
    map[2][2] = "B"
    map[6][3] = "E"
    return map
def Print_map():
    for row in map: #Hur man kan skiva ut kartan fint
        print(row)

def update_player_position(player_pos_y, player_pos_x, player_move):
    """Uppdaterar spelarens position baserat på deras rörelse och position"""
    while True:
        if player_move == "up":
            player_pos_y += 1
        elif player_move == "down":
            player_pos_y -= 1
        elif player_move == "left":
            player_pos_x -= 1
        elif player_move == "right":
            player_pos_x += 1

        else:
            print("ogiltig riktning")
            continue
        return player_pos_y, player_pos_x
    
def get_room_type(player_pos_y, player_pos_x):
    """Returnerar vilken typ av rum spelaren är i baserat på deras position"""
    room = (map[player_pos_y][player_pos_x])

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
    

#test spelare, se till att ta bort den när vi använder detta i maingame.py

map = Map_Creation()

#Lägg in detta i maingame.py med spelare så kommer det funka, funkar inte i denna fil eftersom det inte finns någon player  inte finns här

# player.pos_y, player.pos_x = update_player_position(player.pos_y, player.pos_x, "down") detta är för att flytta spelaren

# get_room_type(player.pos_y, player.pos_x) detta är för att kolla vilket rum spelaren är i och för att
