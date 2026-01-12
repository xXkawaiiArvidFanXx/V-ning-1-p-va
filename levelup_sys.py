import math
from slowtype import *
def xp_req(level):
    """Funktion för hur mycket xp som krävs för att gå upp i nivå"""
    return 10 * 1.5 ** level
    #Derivatan till denna funktion är 10*ln(1.5)*1.5^level om då funktionen är f(level)

def level_up(player):
    """
    Hantera level up. Returnerar (xp, level, strenght, max_hp).
    """
    if player.xp >= xp_req(player.level):
        req = xp_req(player.level)
        choice = input("""Du kan gå upp i nivå! Men innan det måste du bestäma om du vill:
1. Få mer styrka
2. Få mer max hp\n""")
        clear_terminal()
        # trumpet ska spelas här
        #om choice är 1 så ökar styrkan
        if choice == '1':
            player.level += 1
            player.base_strenght += 2
            player.xp -= req
            if player.equipped_weapon == None:
                player.strenght = player.base_strenght
            else:
                player.strenght = player.base_strenght * player.equipped_weapon.damage
            print(f"Du är i level {player.level} och har ökat din styrka till {player.strenght}.")

        #om choice är 2 så ökar max hp och healas helt
        elif choice == '2':
            player.level += 1
            player.maxhp += 5
            player.hp = player.maxhp
            player.xp -= req
            print(f"Du är i level {player.level} och har ökat din max {hp(player)} till {player.maxhp} och du har nu {player.hp}/{player.maxhp} {hp(player)}.")

        else:
            print("Ojdå, mannen med trumpeten slog dig så att du förlorade all xp du hade. Bättre lycka nästa gång")
            print("kanske skulle jag ha valt ett av valen istället för att vara lite dum tänker jag till för mig själv")
            player.xp = 0
    else:
        level_procent = 100*player.xp/xp_req(player.level)
        level_procent_kvar = 100 - level_procent
        print(f"Endast {level_procent_kvar}% kvar till nästa level")
    return player.xp, player.level, player.strenght, player.maxhp, player.hp, player.base_strenght
