from player import *
from map_module import *


# class Player():
#     def __init__(self, hp, strenght, name, charisma, special_weapon=None):
#         self.hp = hp
#         self.maxhp = hp
#         self.inventory = []  # här skapar vi listan för spelarens inventory
#         self.equipped_weapon = None  # Vapnet spelaren har utrustat
#         # Basstat för styrka (oförändrad av vapen)
#         self.base_strenght = strenght
#         # aktuell styrka som används i strid (uppdateras när vapen utrustas och när man går upp i level och väljer styrka)
#         self.strenght = strenght
#         self.name = name
#         self.charisma = charisma
#         self.pos_y = 6
#         self.pos_x = 3
#         self.boss_room_cleared = 0
#         self.boss_room_cleared_posistion_x = 0
#         self.boss_room_cleared_posistion_y = 0
#         self.xp = 0
#         self.level = 1
#         self.health_potion = 0

def save_game(player, map):
    """Player , map"""
    hp = player.hp
    maxhp = player.maxhp
    inventory = player.inventory
    weapon = player.equipped_weapon
    basestrenght =player.base_strenght
    strenght = player.strenght
    name =player.name
    charisma =player.charisma
    y =player.pos_y
    x =player.pos_x
    nr_boss =player.boss_room_cleared
    boss_x =player.boss_room_cleared_posistion_x
    boss_y =player.boss_room_cleared_posistion_y
    xp =player.xp
    level = player.level
    potsion = player.health_potion
    grich = player.grich 
    
    map_save = ""
    for a in range (7):
        for b in range (4): 
             map_save += map[a][b]

    file = open("save_file.txt", mode="w", encoding="utf-8") #encoding="utf-8"
    file.write(f"{hp}_{maxhp}_{inventory}_{weapon}_{basestrenght}_{strenght}_{name}_{charisma}_{y}_{x}_{nr_boss}_{boss_x}_{boss_y}_{xp}_{level}_{potsion}_{grich}_\n{map_save}")
    file.close()
    print("Spelet är nu sparat")

def load_game():

    file = open("save_file.txt", mode="r", encoding="utf-8") #encoding="utf-8" gör att åäö fungerar, taget från internet
    stats = file.readline() #läser alla 16 player stats
    map = file.read(-1) # hämtar kartan
    file.close() #stänger filen
    #print(stats)
    
    stats.split("_")
    list_of_stats = []
    one_stat = ""
    for letter in stats:
        if letter != "_":
            one_stat += letter
        else:
            list_of_stats.append(one_stat)
            one_stat = ""
    player = Player(2,2,"N",2,"W")
    player.hp =int(list_of_stats[0])
    player.maxhp =int(list_of_stats[1])
    player.inventory =list_of_stats[2]
    player.equip_weapon =list_of_stats[3]
    player.base_strenght =float(list_of_stats[4])
    player.strenght=float(list_of_stats[5])
    player.name=list_of_stats[6]
    player.charisma=float(list_of_stats[7])
    player.pos_y=int(list_of_stats[8])
    player.pos_x=int(list_of_stats[9])
    player.boss_room_cleared =list_of_stats[10]
    player.boss_room_cleared_posistion_x=int(list_of_stats[11])
    player.boss_room_cleared_posistion_y=int(list_of_stats[12])
    player.xp =int(list_of_stats[13])
    player.level=int(list_of_stats[14])
    player.health_potion=int(list_of_stats[15])
    player.grich = bool(list_of_stats[16])

    #gör Map save till formen av en karta
    map_save = []
    for i in range (7): #En tom kart mall skapas
        map_save.append([map[4*i-3],map[4*i-2],map[3+4*i-1],map[4*i]])
    # for row in map_save: #Hur man kan skiva ut kartan fint
    #        print(row)

    return player , map_save

#load_game()









# allt effter detta ska bort

# map = []
# map_size = 7 #bestämmer storlek på kartan
# for i in range (map_size): #En tom kart mall skapas
#     map.append([0,0,0,0])

# for a in range (map_size):
#     for b in range (4): #här slumpas rummens egenskaper fram N = Neutralt 
#         #G = gott/GOOd O = Ont/OEvil   T = Trap/fälla kanske R = Renoveras B = BOSS E= tomt rum
#         room_type = ["N","G","O","T"]
#         map[a][b]=(room_type[rand.randint(0,3)])

# #Bossmodul
# #Alltid en boss 1 i mittenrummet 
# #Boss 2 är alltid i sista rummet???
# map[3][1] = "B"
# map[2][2] = "B"
# map[6][3] = "E"

# spelare = Player(2,2,2,2,2)
# save_game(spelare, map)
