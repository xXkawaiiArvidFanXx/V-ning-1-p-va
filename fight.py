import random as rand
from player import *
from soundengien import *
from levelup_sys import *
from slowtype import *


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
                if player.name != "Fatima":
                    print("Du lyckades fly från striden!")
                    return "fled"
                else:
                    print("Du lyckas att fly men du tappade byxorna!")
                    player.hp -= 3
                    print(player.takes_damage())
                    return "fled"

            else:
                print("Du misslyckades att fly! Fienden attackerar.")
                player.hp -= enemy.monsterdamage
                print(player.takes_damage())

        else:
            print("Medans du tvekar, tar fienden chansen att attackera!")
            player.hp -= enemy.monsterdamage
            print(player.takes_damage())
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
    clear_terminal()
    
    print("Du har gått in i ett ont rum och en fiende dyker upp! \n")
    print(f"""-------------------{monster}-------------------""")
    fight_clear_method = fight(player, monster)

    correct_choice = str(rand.randint(1, 3))
    print("\n")
    gissning = input("Om du vill kan du vila och kanske återhämta lite hälsa, men då måste du gissa rätt. 1, 2 eller 3? \n").strip()
    if gissning == correct_choice and fight_clear_method == "victory":
        if player.hp == player.maxhp:
            print("Du har redan full hälsa, du kan inte vila nu.")
            return player.hp
        hpregen = player.maxhp - player.hp
        if hpregen == 0:
            print("Du är redan fullt återhämtad.")
            return player.hp
        genhp = rand.randint(1, hpregen)
        print(f"Du återhämtar {genhp} {hp(player)}.")
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
            boss = Monster(40,3, "le cuisinier")
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
    print("Du har hittat ett gott rum och en hälsodryck och dricker den! \n")
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
        trap_message = "Du går ner för en liten trappnednång på tre steg. Plötsligt halkar du och tappar fotfästet och faller handlöst ner för trappan och landar hårt på marken."
        audio_file = "ljud\jag_faller.wav"

    elif num == 3:
        trap_message = "Du ser en väg in till rum 3545 (Workshopen) och tänker skapa ett vapen av materialen med hjälp av din kunskap och ditt snille. Men när du ska skruva märker du att philips bittsen du satte in inte var rätt och pozidriv skruven skuts ut från ditt vapen och landar i ditt öga."
        audio_file = rand.choice(["ljud\pzidriv_2", "ljud/pozidriv_1.wav"])
    elif num == 4:
        trap_message = "När du öppnar dörren till rummet ser du bara mörker, men Mamma didnt raise no chicken, så du går in. När du går in gör du illa dig på något vasst i mörkret."
        audio_file = 0
    else:
        trap_message = "Du trodde att du hittade en genväg till matsalen, men du hade otur och hamnade i en trång korridor med kladdiga väggar. Du fastnar i väggen i flera timmar och du blir hungrig. I desperation börjar du att äta på väggen som är giftig och du tar skada och blir mildt arg på dig själv för att du åt av väggen istället för mackan i din hand"
        audio_file = 0

    return trap_message, audio_file



def T_room(player, trap_damage, traptype):
    print("\n")
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

    weights = [1, max(1, int(player.charisma))]
    outcome = rand.choices(["äcklig_mat", "god_mat"], weights=weights, k=1)[0]

    if outcome == "äcklig_mat":
        damage = 2
        player.hp = max(0, player.hp - damage)
        print("\n")
        print(f"Mattanten serverade dig äcklig mat! Du tar {damage} skada.\n")
        print(player.takes_damage())
    else:
        heal_amount = 3
        actual_healed = min(heal_amount, player.maxhp - player.hp)
        if actual_healed <= 0:
            player.xp += 1
            print("Mattanten serverade dig god mat, men du är redan fullhälsad. Du får 1 XP istället.")
            print(f"XP: {player.xp}")
        else:
            player.hp += actual_healed
            print(f"Mattanten serverade dig god mat! Du återhämtar {actual_healed} {hp(player)}.")
            print(player.takes_damage())

    return player.hp



def room_chooser(room, player, boss=None, trap_message="", audio_file=0):
    types_of_monsters = ["El och energi elev", "arg lärare", "Levande mobillåda", "Matte gollum", "Blöt och lerig fotboll", "Wilmers skugga", "Hemlösa Alvin"]
    if room == "Ont rum":
        monster_hp = 2 * rand.randint(4, 15)
        base_attack = max(1, int(monster_hp * 0.15))
        monster_attack = max(1, base_attack + rand.randint(-1, 1))

        return O_room(player, Monster(monster_hp, monster_attack, rand.choice(types_of_monsters)))
    elif room == "Bossrum":
        return B_room(player)
    elif room == "Gott rum":
        return G_room(player)
    elif room == "Fällrum":
        return T_room(player, rand.randint(2,4), rand.randint(1,4))
    elif room == "Tomt rum":
        return E_room()
    elif room == "Neutralt rum":
        return N_room(player)