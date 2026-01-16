import math
from text_func import *
from soundengine import *
def xp_req(level):
    """Funktion för hur mycket xp som krävs för att gå upp i nivå"""
    return 10 * 1.5 ** level
    #Derivatan till denna funktion är 10*ln(1.5)*1.5^level om då funktionen är f(level)

def level_up(player):
    """
    Hantera level up. Returnerar (xp, level, strenght, max_hp).
    """
    req = xp_req(player.level)
    if player.xp >= req:
         print ("====================================================================================================================\n")
         choice = input("""Du kan gå upp i nivå! Men innan det måste du bestäma om du vill:
1. Få mer styrka
2. Få mer max hp\n""")
         sound("ljud/xp_ljud.mp3")
         clear_terminal()

         if choice == '1':#om choice är 1 så ökar styrkan
            player.level += 1
            player.base_strenght += 2
            player.xp -= req
            if player.equipped_weapon == None:
                player.strenght = player.base_strenght
            else:
                player.strenght = player.base_strenght + player.equipped_weapon.damage
            print(f"Du är i level {player.level} och har ökat din skada till {player.strenght}.")

         elif choice == '2': #om choice är 2 så ökar max hp och healas helt
            player.level += 1
            player.maxhp += 5
            player.hp = player.maxhp
            player.xp -= req
            print(f"Du är i level {player.level} och har ökat din max {hp_or_aura(player)} till {player.maxhp} och du har nu {player.hp}/{player.maxhp} {hp_or_aura(player)}.")

         else:
            print("Ojdå, mannen med trumpeten slog dig så att du förlorade all xp du hade. Bättre lycka nästa gång")
            print("kanske skulle jag ha valt ett av valen istället för att vara lite dum tänker jag till för mig själv")
            player.xp = 0
            sound("ljud/wompwomp.mp3")

    else:
        level_procent = 100*player.xp/req
        level_procent = round(level_procent)
        level_procent_left = 100 - level_procent
        print(f"Endast {level_procent_left}% kvar till nästa level")
    return player.xp, player.level, player.strenght, player.maxhp, player.hp, player.base_strenght
