import random as rand

class Player():
    def __init__(self, hp, strenght, name, charisma):
        self.hp = hp
        self.maxhp = hp
        self.strenght = strenght
        self.name = name
        self.charisma = charisma
    
    def __str__(self):
        return f"Du har {self.hp}/{self.maxhp} hp. Din styrka är {self.strenght} och du har en charisma på {self.charisma}"
    
    def takes_damage(self):
        return f"Du har nu {self.hp}/{self.maxhp} hp."
        
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
print(weaponnames)

bihahh = Monster(2, "whore", 3, 5)

print(bihahh.attacks())