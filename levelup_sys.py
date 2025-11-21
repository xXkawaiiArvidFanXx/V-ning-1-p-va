import math

def xp_req(level):
    """Funktion för hur mycket xp som krävs för att gå upp i nivå"""
    return 10 * 1.5 ** level

def level_up(xp, level, strenght, max_hp):
    """
    Hantera level up. Returnerar (xp, level, strenght, max_hp).
    """
    while xp >= xp_req(level):
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
            break

        elif choice == '2':
            level += 1
            max_hp += 1
            xp -= req
            print(f"Du är i level {level} och har ökat din max hp till {max_hp}.")
            break

        else:
            print("Ojdå, mannen med trumpeten slog dig så att du förlorade all xp du hade. Bättre lycka nästa gång")
            xp = 0
            
    return xp, level, strenght, max_hp
