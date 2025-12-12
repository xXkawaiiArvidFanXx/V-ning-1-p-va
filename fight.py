import random as rand
from player import *
from soundengien import *
from levelup_sys import *

def fight(player, enemy):

    while player.hp > 0 and enemy.monsterhealth > 0:
        choice = input("Vill du slåss (1) eller försöka fly (2)? ").strip()

        if choice == "1":
            enemy.monsterhealth -= player.strenght
            print(enemy.takes_damage())

            if enemy.monsterhealth > 0:
                player.hp -= enemy.monsterdamage
                print(player.takes_damage())

        elif choice == "2":
            flee_chance = rand.randint(1, 10)
            if flee_chance > 3:
                print("Du lyckades fly från striden!")
                return "fled"
            elif player.name == "Fatima":
                print("Du lyckas att fly men du tappade byxorna!")
                player.hp -= 3
                print(player.takes_damage())
                return "fled_with_loss"
            else:
                print("Du misslyckades att fly! Fienden attackerar.")
                player.hp -= enemy.monsterdamage
                print(player.takes_damage())

        else:
            print("Ogiltigt val, skriv 1 eller 2.")
            continue

    if enemy.monsterhealth <= 0:
        print(f"Du har besegrat {enemy.monstername}!")
        player.xp += enemy.monsterxp
        player.xp, player.level, player.strenght, player.maxhp = level_up(player.xp, player.level, player.strenght, player.maxhp)
        return "victory"

    if player.hp <= 0:
        print("Du har blivit besegrad...")
        print("Försök att inte suga så mycket nästa gång!")
        return "defeat"



def O_room(player, monster):
    print("Du har gått in i ett ont rum och en fiende dyker upp!")
    print(monster)
    fight(player, monster)
    correct_choice = str(rand.randint(1, 3))
    gissning = input("Om du vill kan du vila och kanske återhämta lite hälsa, men då måste du gissa rätt. 1, 2 eller 3? ").strip()
    if gissning == correct_choice:
        if player.hp == player.maxhp:
            print("Du har redan full hälsa, du kan inte vila nu.")
            return player.hp
        hpregen = player.maxhp - player.hp
        if hpregen > 5:
            hpregen = 5
        if hpregen <= 0:
            print("Du är redan fullt återhämtad.")
            return player.hp
        genhp = rand.randint(1, hpregen)
        print(f"Snyggt! Du återhämtar {genhp} HP.")
        player.hp += genhp
    else:
        print("Fel gissning, ingen hälsa återhämtad.")
    return player.hp

def B_room(player):
    boss = None
    if player.pos_y == player.boss_room_cleared_posistion_y and player.pos_x == player.boss_room_cleared_posistion_x :
        print("Du har redan besegrat bossen i detta rum.")
        return
    else:
        if player.boss_room_cleared == 0:
            boss = Monster(20,2, "le cuisinier")
            fight(player, boss)
            player.boss_room_cleared += 1
            player.boss_room_cleared_posistion_y = player.pos_y
            player.boss_room_cleared_posistion_x = player.pos_x
            player.hp = player.maxhp
        elif player.boss_room_cleared == 1:
            boss = Monster(25,3, "le homme féminin Wilmér")
            fight(player, boss)
            player.boss_room_cleared += 1
    return player.hp, player.boss_room_cleared, player.boss_room_cleared_posistion_y, player.boss_room_cleared_posistion_x

def G_room(player):
    print("Du har hittat ett gott rum och en hälsodryck och dricker den!")
    heal_amount = rand.randint(1, 2)
    player.hp += heal_amount
    if player.hp > player.maxhp:
        player.hp = player.maxhp
    return player.hp




def traptypes(num):
    audio_file = 0
    if num == 1:
        trap_message = """Du går fram med raska men bestämda steg och kommer fram till att du ska köpa en chokladboll. Du lägger fram 25 kr som du gjort orimligt många gånger innan." 
        Men personalen i kiosken kollar på dig som om du är en idiot och pekar på priserna.
        Det är ju 50 för en chokladboll, med nyfunnen skam i kroppen så tar du tillbaka dina 25 kronor och går med ett sänkt huvud bort från kiosken ."""
        audio_file = "ljud/kiosken.wav"
    elif num == 2:
        trap_message = "Du går ner för en liten trappnednång på tre steg. Plötsligt tappar du fotfästet och faller handlöst ner för trappan och landar hårt på marken."
        audio_file = "ljud\jag_faller.wav"

    elif num == 3:
        trap_message = "Du ser en väg in till rum 3545 (Workshopen) och tänker skapa ett vapen av materialen. Men när du ska skruva märker du att philips bittsen du satte in inte var rätt och pozidriv skruven skuts ut från ditt vapen och landar i ditt öga."
        audio_file = rand.choice(["ljud\pzidriv_2", "ljud/pozidriv_1.wav"])
    elif num == 4:
        trap_message = "När du öppnar dörren till det rum du går fram till ser du bara mörker, men Mamma didnt raise no chicken. När du går in gör du illa dig på något vasst i mörkret."
        audio_file = 0
    else:
        trap_message = "En mystisk fälla…"
        audio_file = 0

    return trap_message, audio_file



def T_room(player, trap_damage, traptype):

    trap_message, audio_file = traptypes(traptype)
    print(trap_message)
    if audio_file == 0:
        pass
    else:
        sound(audio_file)
    player.hp -= trap_damage
    print(player.takes_damage())
    ajj = rand.randint(1,10)
    if ajj == 1:
        sound("ljud/oj_aj.wav")
    return player.hp


def E_room():
    print("Detta rum är tomt.")
    print("Det finns inget mer att säga liksom.")


def N_room(player):
    print("Mattanten: Hej! Jag har lagat ett litet experimentellt recept som du bara MÅSTE prova.")
    colunary_experience = ["äcklig_mat", "god_mat"]
    weights = [1, max(1, int(player.charisma))]
    random_tastey = rand.choices(colunary_experience, weights=weights, k=1)[0]

    if random_tastey == "äcklig_mat":
        print("Mattanten serverade dig äcklig mat! Du tappar hälsa.")
        player.hp -= 2
        print(player.takes_damage())
    else:
        print("Mattanten serverade dig god mat! Du återhämtar hälsa.")
        player.hp += 3
    return player.hp

types_of_monsters = ["El och energi elev", "arg lärare", "Levande mobillåda", "Matte gollum"]


def room_chooser(room, player, boss=None, trap_message="", audio_file=0):
    if room == "Ont rum":
        return O_room(player, Monster(20, 3, rand.choice(types_of_monsters)))
    elif room == "Bossrum":
        return B_room(player, boss)
    elif room == "Gott rum":
        return G_room(player)
    elif room == "Fällrum":
        return T_room(player, rand.randint(2,4), rand.randint(1,4))
    elif room == "E":
        return E_room()
    elif room == "Tomt rum":
        return N_room(player)