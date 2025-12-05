import random as rand
from slowtype import slowtype, deadahh
class Player():
    def __init__(self, hp, strenght, name, charisma):
        self.hp = hp
        self.maxhp = hp
        self.strenght = strenght
        self.name = name
        self.charisma = charisma
        self.inventory = [] # här skapar vi listan för spelarens inventory
        self.equipped_weapon = None # Vapnet spelaren har utrustat
        self.pos_y = 6
        self.pos_x = 3
    
    def __str__(self):
        return f"Du har {self.hp}/{self.maxhp} hp. Din styrka är {self.strenght} och du har en charisma på {self.charisma}"
    
    def takes_damage(self):
        return f"Du har nu {self.hp}/{self.maxhp} hp."
    

    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def equip_weapon(self, weapon):
        if weapon in self.inventory:
            self.equipped_weapon = weapon



def inventory(player):
    # här ska man kunna öppna sitt inventory och göra saker som att byta vapen,
    # kolla items och stats, och spara och stänga av
    while True:
        print("\n Inventory och Stats:")
        print(f"HP: {player.hp}/{player.maxhp}")
        print(f"Styrka: {player.strenght}")
        print(f"Din charisma är: {player.charisma}")
        
        if player.equipped_weapon:
            print(f"Utrustat Vapen: {player.equipped_weapon.name} Som gör {player.equipped_weapon.damage} i skada")
        
        print(f"\nDina Saker är: {len(player.inventory)}")
        for i, item in enumerate(player.inventory):
            print(f"{i+1}. {item.name} - Skada: {item.damage}, Räckvidd: {item.range}, Sällsynthet: {item.rarity}")
        
        # Meny Alternativ
        slowtype("\nVad vill du göra?\n", 0.05)
        slowtype("1. Byt Vapen\n2. Stäng Inventory\n", 0.05)
        choice = input("Välj ett alternativ!!! ")
        try:
            if choice == "1":
                weapon_choice = int(input("Ange numret på vapnet du vill utrusta: ")) - 1
                if 0 <= weapon_choice < len(player.inventory):
                    player.equip_weapon(player.inventory[weapon_choice])
                    slowtype(f"Du har utrustat {player.equipped_weapon.name}.\n", 0.05)
                else:
                    deadahh()
                    slowtype("Ogiltigt val. Försök igen.\n", 0.05)
            elif choice == "2":
                break
        except ValueError:
            deadahh()
            slowtype("Lock in. Försök igen.\n", 0.05) 
               




class Weapon():
    def __init__(self, damage, range, name, rarity):
        self.range = range
        self.name1 = name
        self.rarity = rarity
        self.name = name

        if self.rarity == "legendariskt":
            self.damage = damage * 2

        elif self.rarity == "Episkt":
            self.damage = damage * 1.5

        elif self.rarity == "normal":
            self.damage = damage 

        elif self.rarity == "temu kvalite":
            self.damage = damage * 0.75


class Monster():
    def __init__(self, monsterhealth, monsterdamage, monstername, monsterxp):
        self.monsterhealth = monsterhealth
        self.monstermaxhealth = monsterhealth
        self.monsterdamage = monsterdamage
        self.monstername = monstername
        self.monsterxp = monsterxp

    def __str__(self):
        return f"Fienden har {self.monsterhealth} och gör {self.monsterdamage} i skada"
    
    def takes_damage(self):
        return f"Fienden har nu {self.monsterhealth}/{self.monstermaxhealth}hp kvar"
    
    def attacks(self):
        return f"Fienden gör {self.monsterdamage} i skada"



adjektivlista = ["smal ", "hal ", "kladdig ","smörstekt ","ihålig ", "väldoftande ", "illaluktande ", "jättetung ", "urladdad ", "uråldrig ", "modern ", "politisk ","tondöv ","Toronto baserad ", "utomjordig ","långt ifrån stämd ","fläckig ","musikalisk ","lysande ","dubbelsidig ","politiskt korrekt ", "politiskt inkorrekt ", "dålig ","svag ","drogpåverkad " ]
vapenlista = ["pilbåge", "projector kontroll", "dolk", "stekpanna", "kastrull", "mattebok","kniv","suddgummi","sköld","penna","saxofon", "gitarr","pappersflygplan","trombon", "bastrumma", "flagga", "musiksmak","kunskap","ljussabel"]
weaponnames = rand.choice(adjektivlista)+rand.choice(vapenlista)

def health_potion(hp, maxhp, min_heal, max_heal):
    heal_amount = rand.randint(min_heal, max_heal)
    hp += heal_amount
    if hp > maxhp:
        hp = maxhp
        print(f"Du återhämtar dig helt till {maxhp} hp!")
    elif heal_amount == min_heal:
        print(f"Du spilde väldigt mycket av din hälsodryck och återhämtar bara {min_heal} hp, du har nu {hp} hp")
    return hp
