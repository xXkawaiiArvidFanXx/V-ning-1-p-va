from player import *
from map_module import *


def save_game(player, game_map, weapon):
    """Player , game_map, weapon"""
    hp = player.hp
    maxhp = player.maxhp
    # Inventory
    inventory = ""
    for w in player.inventory:
        inventory += f"{w.damage},{w.name},{w.rarity}|"

    e_weapon = player.equipped_weapon
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
    grisch = player.grisch 
    
    weapon_damage = weapon.damage
    weapon_name = weapon.name
    weapon_rarity = weapon.rarity


    # Bygger inventory som text: damage,name,rarity|



    print(game_map)
    map_save = ""
    for a in range (7):
        for b in range (4): 
             map_save += game_map[a][b]

    file = open("save_file.txt", mode="w", encoding="utf-8") #encoding="utf-8"
    file.write(f"{hp}_{maxhp}_{inventory}_{e_weapon}_{basestrenght}_{strenght}_{name}_{charisma}_{y}_{x}_{nr_boss}_{boss_x}_{boss_y}_{xp}_{level}_{potsion}_{grisch}_{weapon_damage}_{weapon_name}_{weapon_rarity}_\n{map_save}\n")
    file.close()
    print("Spelet är nu sparat")

def load_game():

    file = open("save_file.txt", mode="r", encoding="utf-8") #encoding="utf-8" gör att åäö fungerar, taget från internet
    stats = file.readline() #läser alla 16 player stats
    game_map = file.read(-1) # hämtar kartan
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


    inventory =list_of_stats[2]
    player.inventory = []

    inventory = list_of_stats[2]
    player.inventory = []

    if inventory != "":
        for w in inventory.split("|"):
            if w == "":
                continue
            damage, name, rarity = w.split(",")
            player.inventory.append(Weapon(int(damage), name, rarity))


    player.equipped_weapon =list_of_stats[3]
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
    player.grisch = bool(list_of_stats[16])
    weapon_damage = int(list_of_stats[17])
    weapon_name = list_of_stats[18]
    weapon_rarity =list_of_stats[19]
    wepon =Weapon(weapon_damage, weapon_name, weapon_rarity)

    player.equipped_weapon = wepon
    
    #gör Map save till formen av en karta
    map_save = []
    for i in range (7): #En tom kart mall skapas
        map_save.append([game_map[4*i-3],game_map[4*i-2],game_map[3+4*i-1],game_map[4*i]])
    # for row in map_save: #Hur man kan skiva ut kartan fint
    #        print(row)
    if player.equipped_weapon == None:
        eqwep = "INGENTING"
    else:
        eqwep = player.equipped_weapon
    print(f"""    Välkommen tillbaka {player.name}. du har {player.hp} av {player.maxhp}. 
    Du är i level {player.level} och har {player.strenght} i styrka.
    Just nu använder du {eqwep}""")
    return player , map_save
