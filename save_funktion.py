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
    strenght =player.base_strenght
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
    
    map_save = ""
    for a in range (map_size):
        for b in range (4): #här slumpas rummens egenskaper fram N = Neutralt 
             map_save += map[a][b]

    file = open("save_file.txt", mode="w", encoding="utf-8") #encoding="utf-8"
    file.write(f"{hp}{maxhp}{inventory}{strenght}{name}{charisma}{y}{x}{nr_boss}{boss_x}{boss_y}{xp}{level}{potsion}\n{map_save}")
    file.close()



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
