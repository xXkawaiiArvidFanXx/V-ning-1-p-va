import random as rand

class Player():
    def __init__(self, hp, strenght, name):
        self.hp = hp
        self.maxhp = hp
        self.strenght = strenght
        self.name = name
        
class Weapon():
    def __init__(self, damage, range, name, rarity):
        self.damage = damage
        self.range = range
        self.name1 = name
        self.rarity = rarity
        self.name = name
class Monster():
    def __init__(self, monsterhealth, monsterdamage, monstername, monsterxp):
        self.monsterhealth = monsterhealth
        self.monstermaxhealth = monsterhealth
        self.monsterdamage = monsterdamage
        self.monstername = monstername
        self.monsterxp = monsterxp



adjektivlista = ["smal ", "hal ", "kladdig ","smörstekt ","ihålig ", "väldoftande ", "illaluktande ", "jättetung ", "urladdad ", "uråldrig ", "modern ", "politisk ","tondöv ","Toronto baserad ", "utomjordig ","långt ifrån stämd ","fläckig ","musikalisk ","lysande ","dubbelsidig ","politiskt korrekt ", "politiskt inkorrekt ", "dålig ","svag ","drogpåverkad " ]
vapenlista = ["pilbåge", "projector kontroll", "dolk", "stekpanna", "kastrull", "mattebok","kniv","suddgummi","sköld","penna","saxofon", "gitarr","pappersflygplan","trombon", "bastrumma", "flagga", "musiksmak","kunskap","ljussabel"]
weaponnames = rand.choice(adjektivlista)+rand.choice(vapenlista)
print(weaponnames)
