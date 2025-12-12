import math

def xp_req(level):
    """Funktion för hur mycket xp som krävs för att gå upp i nivå"""
    return 10 * 1.5 ** level
    #Derivatan till denna funktion är 10*ln(1.5)*1.5^level om då funktionen är f(level)

def level_up(xp, level, strenght, max_hp):
    """
    Hantera level up. Returnerar (xp, level, strenght, max_hp).
    """
    if xp >= xp_req(level):
        req = xp_req(level)
        choice = input("""Du kan gå upp i nivå! Men innan det måste du bestäma om du vill:
                1. Få mer styrka
                2. Få mer max hp
                       """)

        # trumpet ska spelas här
        if choice == '1':
            level += 1
            strenght += 1
            xp -= req
            print(f"Du är i level {level} och har ökat din styrka till {strenght}.")

        elif choice == '2':
            level += 1
            max_hp += 1
            xp -= req
            print(f"Du är i level {level} och har ökat din max hp till {max_hp}.")

        else:
            print("Ojdå, mannen med trumpeten slog dig så att du förlorade all xp du hade. Bättre lycka nästa gång")
            print("kanske skulle jag ha valt ett av valen istället för att vara lite dum tänker jag till för mig själv")
            xp = 0
    else:
        level_procent = 100*xp/xp_req(level)
        level_procent_kvar = 100 - level_procent
        print(f"Endast {level_procent_kvar}% kvar till nästa level")
    return xp, level, strenght, max_hp
