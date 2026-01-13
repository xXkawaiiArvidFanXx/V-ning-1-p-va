import random as rand
from slowtype import *
from map_in_turtle import *

class Player():
    def __init__(self, hp, strenght, name, charisma, special_weapon=None):
        self.hp = hp
        self.maxhp = hp
        self.inventory = []  # här skapar vi listan för spelarens inventory
        self.equipped_weapon = None  # Vapnet spelaren har utrustat
        # Basstat för styrka (oförändrad av vapen)
        self.base_strenght = strenght
        # aktuell styrka som används i strid (uppdateras när vapen utrustas och när man går upp i level och väljer styrka)
        self.strenght = strenght
        self.name = name
        self.charisma = charisma
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

    def equip_weapon(self):
        """Visa inventory och låt spelaren välja ett vapen att utrusta.

        Visar en numrerad lista, 0 = avbryt. Uppdaterar `self.equipped_weapon` och
        `self.strenght` direkt (alla inventory-items är vapen).
        """
        if not self.inventory:
            print("Ditt inventory är tomt.")
            self.equipped_weapon = None
            self.strenght = self.base_strenght
            return

        while True:
            print("\nVälj ett vapen att utrusta (0 för avbryt):\n")
            for i, item in enumerate(self.inventory): #enumerate gör så att vi kan få index och item samtidigt
                print(f"{i+1}. {item.name} - Skada: {item.damage}, Sällsynthet: {item.rarity}")

            choice = input("\nSkriv siffran för vapnet du vill utrusta: ")
            print("")
            try:
                item_chooser = int(choice)
            except ValueError:
                print("Ogiltig inmatning, ange en siffra.")
                continue

            if item_chooser == 0:
                print("Avbröt utrustning.")
                return

            item_chooser -= 1  # gör så att valet matchar list startande från 0 eller vad man ska säga
            if item_chooser < 0 or item_chooser >= len(self.inventory):
                print("Ogiltigt val. Försök igen.")
                continue

            self.equipped_weapon = self.inventory[item_chooser]
            self.strenght = self.base_strenght + self.equipped_weapon.damage
            print(f"Du utrustade: {self.equipped_weapon.name}. Din skada är nu {self.strenght}.")
            return




def inventory(player):
    # här ska man kunna öppna sitt inventory och göra saker som att byta vapen,
    # kolla items och stats, och spara och stänga av
    print("\n Inventory och Stats:")
    print(f"Din level är: {player.level}")
    print(f"{hp(player)}: {player.hp}/{player.maxhp}")
    print(f"Styrka: {player.strenght}")
    print(f"Din charisma är: {player.charisma}")
    if player.equipped_weapon != None:
        print(f"\nUtrustat Vapen: {player.equipped_weapon.name}")
    time.sleep(2)

    slowtype(f"\nDina Saker är: {len(player.inventory)}", 0.05)
    time.sleep(0.5)
    for i, item in enumerate(player.inventory):
        print(f"{i+1}. {item.name} - Skada: {item.damage}, Sällsynthet: {item.rarity}")
        time.sleep(0.2)

    while True: 
        # Meny Alternativ
        slowtype("\nVad vill du göra?\n", 0.05)
        slowtype("1. Byt Vapen\n2. Öppna Karta (haijper nice)\n3. Stäng Inventoryn\n", 0.05)
        choice = input("Välj ett alternativ!!! ")
        try:
            if choice == "1":
                player.equip_weapon()
                time.sleep(2)
                clear_terminal()
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
        self.damage = damage
        self.rarity = rarity
        self.name = name

        if self.rarity == "legendariskt":
            self.damage = round(damage * 2)
        elif self.rarity == "Episkt":
            self.damage = round(damage * 1.5)
        elif self.rarity == "normal":
            self.damage = damage
        elif self.rarity == "temu kvalite":
            self.damage = round(damage * 0.75)

    def __str__(self):
        return f"{self.name} ||| Skada: {self.damage} ||| Sällsynthet: {self.rarity} |||"

def monsterRANDname(monstername=""):
    adjektivlista = ["smal ", "hal ", "kladdig ","smörstekt ","ihålig ", "väldoftande ", "illaluktande ", "jättetung ", "urlladad ", "uråldrig ", "modern ", "politisk ","tondöv ","Toronto baserad ", "utomjordig ","långt ifrån stämd ","fläckig ","musikalisk ","lysande ","dubbelsidig ","politiskt korrekt ", "politiskt inkorrekt ", "dålig ","svag ","drogpåverkad ", "iskall" ]
    monsterlista = ["Teknikare", "lerig och blöt fotboll", "Bokhylla", "Multimeter","El och energi elev", "arg lärare", "Levande mobillåda", "Matte gollum", "Blöt och lerig fotboll", "Wilmers skugga", "Hemlösa Alvin"]
    # om inget namn ges så slumpas ett namn fram
    if monstername == "" or monstername is None:
        return rand.choice(adjektivlista) + rand.choice(monsterlista)
    return monstername

class Monster():
    def __init__(self, monsterhealth, monsterdamage, boss, monstername=""):
        self.monsterhealth = monsterhealth
        self.monstermaxhealth = monsterhealth
        self.monsterdamage = monsterdamage
        self.monstername = monsterRANDname(monstername)
        self.monsterxp = monsterdamage * monsterhealth
        self.wepond = weapon_create("")
        self.wepond_drop_rate = rand.randint(1, 100)
        self.is_boss = boss #booleskt värde, True innebär att det är en boss, detta gör bara så att man inte kan fly från slagsmålet





    def __str__(self):
        return f"Fienden ({self.monstername}) har {self.monsterhealth} hp och gör {self.monsterdamage} i skada"
    
    def takes_damage(self):
        return f"Fienden har nu {self.monsterhealth}/{self.monstermaxhealth}hp kvar"
    
    def attacks(self):
        return f"Fienden gör {self.monsterdamage} i skada"
    
    def drop_weapon(self, player):
        if self.wepond_drop_rate > 70:
            return 
        else:
            player.add_item(self.wepond)
            print(f"Efter att du dödade {self.monstername} dropade han {self.wepond}")
            print("För att använda detta vapen gå in i ditt inventory och byt vapen")
        


def weapon_create(wepontype):
    adjektivlista = ["smal ", "hal ", "kladdig ","smörstekt ","ihålig ", "väldoftande ", "illaluktande ", "jättetung ", "urladdad ", "uråldrig ", "modern ", "politisk ","tondöv ","Toronto baserad ", "utomjordig ","långt ifrån stämd ","fläckig ","musikalisk ","lysande ","dubbelsidig ","politiskt korrekt ", "politiskt inkorrekt ", "dålig ","svag ","drogpåverkad ", "iskall" ]
    vapenlista = ["pilbåge", "projector kontroll", "dolk", "stekpanna", "kastrull", "mattebok","kniv","suddgummi","sköld","penna","saxofon", "gitarr","pappersflygplan","trombon", "bastrumma", "flagga", "musiksmak","kunskap","ljussabel", "nallebjörn"]

    if wepontype == "":
        wepontype = rand.choice(vapenlista)
    weponadjectiv = rand.choice(adjektivlista)
    weaponnames = weponadjectiv + wepontype
    wepond_rarity = rand.randint(1,100)
    if wepond_rarity > 95:
        rarity = "legendariskt"
    elif wepond_rarity > 80:
        rarity = "Episkt"
    elif wepond_rarity > 50:
        rarity = "normal"
    else:
        rarity = "temu"
    weapon = Weapon(rand.randint(2,10), weaponnames, rarity)
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


