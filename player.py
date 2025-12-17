import random as rand
from slowtype import *
from map_in_turtle import *
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
        self.boss_room_cleared = 0
        self.boss_room_cleared_posistion_x = 0
        self.boss_room_cleared_posistion_y = 0
        self.xp = 0
        self.level = 1
    
    def __str__(self):
        return f"Du har {self.hp}/{self.maxhp} hp. Din styrka är {self.strenght} och du har en charisma på {self.charisma}"
    
    def takes_damage(self):
        return f"Du har nu {self.hp}/{self.maxhp} {hp(self)}."
    

    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def equip_weapon(self, weapon):
        if weapon in self.inventory:
            self.equipped_weapon = weapon

    def generate_weapon(self, wepontype=""):
        """Skapar ett vapen med `weapon_create` och lägger det i spelarens inventory.

        Args:
            wepontype (str): valfri typ/namn för vapnet. Tom sträng betyder slump.

        Returns:
            Weapon: det genererade vapnet som också har lagts till i inventory.
        """
        try:
            new_weapon = weapon_create(wepontype)
            self.add_item(new_weapon)
            return new_weapon
        except Exception as e:
            # Om något går fel, skriv ut ett felmeddelande och returnera None
            deadahh()
            print(f"Kunde inte skapa vapen: {e}")
            return None



def inventory(player):
    # här ska man kunna öppna sitt inventory och göra saker som att byta vapen,
    # kolla items och stats, och spara och stänga av
    while True:
        print("\n Inventory och Stats:")
        print(f"{hp(player)}: {player.hp}/{player.maxhp}")
        print(f"Styrka: {player.strenght}")
        print(f"Din charisma är: {player.charisma}")
        
        if player.equipped_weapon:
            print(f"Utrustat Vapen: {player.equipped_weapon.name} Som gör {player.equipped_weapon.damage} i skada")
        
        print(f"\nDina Saker är: {len(player.inventory)}")
        for i, item in enumerate(player.inventory):
            print(f"{i+1}. {item.name} - Skada: {item.damage}, Sällsynthet: {item.rarity}")
        
        # Meny Alternativ
        slowtype("\nVad vill du göra?\n", 0.05)
        slowtype("1. Byt Vapen\n2. Öppna Karta (haijper nice)\n3. Stäng Inventoryn\n", 0.05)
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
            elif choice == "3":
                break
            elif choice == "2":
                slowtype("Klicka in på Turtle Grafics fönstret.\n", 0.05)
                Turtle_maps(player.pos_x, player.pos_y)
        except ValueError:
            deadahh()
            slowtype("Lock in. Försök igen.\n", 0.05) 
               




class Weapon():
    def __init__(self, damage, name, rarity):
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

    def __str__(self):
        return f"{self.name} — Skada: {self.damage}, Sällsynthet: {self.rarity}"


class Monster():
    def __init__(self, monsterhealth, monsterdamage, monstername):
        self.monsterhealth = monsterhealth
        self.monstermaxhealth = monsterhealth
        self.monsterdamage = monsterdamage
        self.monstername = monstername
        self.monsterxp = monsterdamage * monsterhealth
        self.wepond = weapon_create("")
        self.wepond_drop_rate = rand.randint(1, 100)

    def __str__(self):
        return f"Fienden har {self.monsterhealth} och gör {self.monsterdamage} i skada"
    
    def takes_damage(self):
        return f"Fienden har nu {self.monsterhealth}/{self.monstermaxhealth}hp kvar"
    
    def attacks(self):
        return f"Fienden gör {self.monsterdamage} i skada"
    
    def drop_weapon(self, player):
        if self.wepond_drop_rate > 70:
            return 
        else:
            player.add_item(self.wepond)

def weapon_create(wepontype):
    adjektivlista = ["smal ", "hal ", "kladdig ","smörstekt ","ihålig ", "väldoftande ", "illaluktande ", "jättetung ", "urladdad ", "uråldrig ", "modern ", "politisk ","tondöv ","Toronto baserad ", "utomjordig ","långt ifrån stämd ","fläckig ","musikalisk ","lysande ","dubbelsidig ","politiskt korrekt ", "politiskt inkorrekt ", "dålig ","svag ","drogpåverkad ", "iskall" ]
    vapenlista = ["pilbåge", "projector kontroll", "dolk", "stekpanna", "kastrull", "mattebok","kniv","suddgummi","sköld","penna","saxofon", "gitarr","pappersflygplan","trombon", "bastrumma", "flagga", "musiksmak","kunskap","ljussabel", "nallebjörn"]

    if wepontype == "":
        wepontype = rand.choice(vapenlista)
    weponadjectiv = rand.choice(adjektivlista)
    weaponnames = weponadjectiv + wepontype
    rarity = rand.choice(["legendariskt", "Episkt", "normal", "temu kvalite"])
    weapon = Weapon(rand.randint(5,15), weaponnames, rarity)
    return weapon

def health_potion(hp, maxhp, min_heal, max_heal):
    heal_amount = rand.randint(min_heal, max_heal)
    hp += heal_amount
    if hp > maxhp:
        hp = maxhp
        print(f"Du återhämtar dig helt till {maxhp} hp!")
    elif heal_amount == min_heal:
        print(f"Du spilde väldigt mycket av din hälsodryck och återhämtar bara {min_heal} hp, du har nu {hp} hp")
    return hp
