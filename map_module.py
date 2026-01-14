#Här skapas en karta och rummen slumpas fram
#karta grid lista i lista 
#map = kartan
#med funktionen Print_map() så kan du skriva ut kartan i terminalen
#med funktionen Map_Creation skapas en ny karta som sparas i den globala variabeln map
#med funktionen get_room_type() kan du få vad det är för typ av rum spelaren står i
import random as rand
from player import *
from soundengiene import *
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
    map[3][1] = "B"
    map[2][2] = "B"
    map[6][3] = "E"
    return map
def Print_map():
    for row in map: #Hur man kan skiva ut kartan fint
        print(row)

map = Map_Creation()



def illigal_move(player_pos_y, player_pos_x): #Säger om Spelaren går utanför kartan
    if player_pos_y < 0 or player_pos_y > 6 or player_pos_x < 0 or player_pos_x > 3:
        print("Du kan inte gå utanför kartan!")
        return True
    else:
        return False


def player_position(pos_y, pos_x):
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

def get_room_type(player_pos_y, player_pos_x):
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
    
