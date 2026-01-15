import random as rand
from player import *
from soundengiene import *
from levelup_sys import *
from text_func import *
import time

def fight(player, enemy):
    """Kod för slagsmål"""

    first_strike = enemy.monster_start(player)

    while player.hp > 0 and enemy.monsterhealth > 0:

        if first_strike:
            print(f"\n{enemy.monstername} attackerar dig först!")
            player.hp -= enemy.monsterdamage
            print(player.takes_damage())
            first_strike = False

        if enemy.fight_or_flight(player):
            print(f"{enemy.monstername} ser din karisma!")
            return "fled"

        choice = input("Vill du slåss (1) eller dricka en hälsodryck (2) eller försöka fly (3)? ").strip()

        if choice == "1":
            print(f"\nDu attackerar {enemy.monstername}\n")
            time.sleep(0.5)
            enemy.monsterhealth -= player.strenght
            if enemy.monsterhealth < 0:
                enemy.monsterhealth = 0
            print(enemy.takes_damage())
            time.sleep(0.5)

            if enemy.monsterhealth > 0:
                player.hp -= enemy.monsterdamage
                print(f"\n{enemy.monstername} attackerar dig tillbaka!")
                print(f"{player.takes_damage()}")
                time.sleep(0.5)
        elif choice == "2":
            if player.health_potion <= 0:
                print("Du har inga hälsodrycker kvar!")
                continue
            else:
                player = use_health_potion(player)
                buffered_type("Du dricker en hälsodryck och återhämtar lite hälsa!\n", 0.05)

        elif choice == "3":
            flee_chance = rand.randint(1, 10)
            if enemy.is_boss == True:
                print("Precis när du försöker fly från bossen så greppar han tag i dig och slår dig!")
                player.hp -= enemy.monsterdamage
                print(player.takes_damage())

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
        enemy.drop_weapon(player)
        return "victory"
        


    if player.hp <= 0:
        print("Du har blivit besegrad...")
        print("Försök att inte suga så mycket nästa gång!")
        return "defeat"



def O_room(player, monster):
    """Ont rum, startar slagsmål. Efter slagsmålet kollar koden vissa saker t.ex hur man vann o om man kan levla upp"""
    clear_terminal()
    
    print("Du har gått in i ett ont rum och en {} dyker upp! \n".format(monster.monstername))
    print(f"""-------------------{monster}-------------------""")
    fight_clear_method = fight(player, monster)

    if fight_clear_method == "victory":
        correct_choice = str(rand.randint(1, 3))
        print("\n")
        gissning = input("Om du vill kan du vila och kanske återhämta lite hälsa, men då måste du gissa rätt. 1, 2 eller 3? \n").strip()
        if gissning == correct_choice:
            if player.hp == player.maxhp:
                print("Du har redan full hälsa, du kan inte vila nu.")
            hpregen = player.maxhp - player.hp
            if hpregen == 0:
                print("Du är redan fullt återhämtad.")
            genhp = rand.randint(1, hpregen)
            print(f"Du återhämtar {genhp} {hp_or_aura(player)}.")
            player.hp += genhp
        else:
            print("Fel gissning, ingen hälsa återhämtad.")
        player.xp, player.level, player.strenght, player.maxhp, player.hp, player.base_strenght = level_up(player)
    return player



def B_room(player):
    boss = None
    if player.pos_y == player.boss_room_cleared_posistion_y and player.pos_x == player.boss_room_cleared_posistion_x :
        print("Du har redan besegrat bossen i detta rum.")
        return player
    else:

        buffered_type("Bossen har små minjoner som spelar episk musik på GIGANORMA högtalare", 0.1)
        buffered_type("Det rekomenderas att sänka volymen", 0.1)
        buffered_type("Du har 5 sekunder på dig", 0.1)
        stopmusic()
        backgroundmusic("ljud\hesa_filip.waw")
        for i in range (0,4):
            time.sleep(1)
            print(i+1) # Eventuelt ljud
        backgroundmusic("ljud\cinematic_drum_loop.wav")
        
        
        if player.boss_room_cleared == 0:
            print("Du har kommit till ett bossrum! Förbered dig på en tuff strid mot le cuisinier! \n")
            boss = Monster(round(player.level*1.05*75), round(player.level*1.05*5), True, "Le Cuisinier")
            boss_clear_method = fight(player, boss)
            if boss_clear_method == "victory":
                print("Grattis! Du har besegrat Le Cuisinier och klarat av det första bossrummet!")
                player.boss_room_cleared += 1
                player.boss_room_cleared_posistion_y = player.pos_y
                player.boss_room_cleared_posistion_x = player.pos_x
                player.hp = player.maxhp

        elif player.boss_room_cleared == 1:
            boss = Monster(round(player.level*1.05*150),round(player.level*1.05*10), True, "Le Homme Féminin Wilmér")
            fight(player, boss)
            player.boss_room_cleared += 1
        stopmusic()
        backgroundmusic("ljud\\bakgrund.wav")
    return player

def G_room(player):
    print("Du har hittat en kista och öppnar den!\n")
    chest(player)
    return player


def traptypes(num, player):
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
        trap_message = "Du ser en väg in till rum 3545 (Workshopen) och tänker skapa ett vapen av materialen med hjälp av din kunskap och ditt snille. Men när du ska skruva märker du att philips bittsen du satte in inte var rätt bits till en pozidriv skruv, så pozidriv skruven skuts ut från ditt vapen och landar i ditt öga."
        audio_file = rand.choice(["ljud\pzidriv_2", "ljud/pozidriv_1.wav"])
    elif num == 4:
        trap_message = "När du öppnar dörren till rummet ser du bara mörker, men Mamma didnt raise no chicken, så du går in. När du går in gör du illa dig på något vasst i mörkret."
        audio_file = 0
    elif num == 5:
        trap_message = "Du råkade öppna fel dörr och du gick in i en improv musikgrupp som spelar lite jazz!"
        audio_file = "ljud/jazztrap.wav"
    elif len(player.inventory) >= 5:
        trap_message = "Du försöker att smyga förbi en lärare som patrullerar korridoren, men du snubblar över din egen ficka full med saker och faller pladask på marken. Läraren ser dig och du får en varning för att ha sprungit i korridoren."
        audio_file = 0
    else:
        trap_message = "Du trodde att du hittade en genväg till matsalen, men du hade otur och hamnade i en trång korridor med kladdiga väggar. Du fastnar i väggen i flera timmar och du blir hungrig. I desperation börjar du att äta på väggen som är giftig och du tar skada och blir mildt arg på dig själv för att du åt av väggen istället för mackan i din hand"
        audio_file = 0

    return trap_message, audio_file



def T_room(player, trap_damage, traptype):
    print("\n")
    trap_message, audio_file = traptypes(traptype, player)
    print(trap_message)
    if audio_file == 0:
        pass
    else:
        sound(audio_file)
    player.hp -= trap_damage
    print(player.takes_damage())
    ajj = rand.randint(round(player.maxhp*0.1,), round(player.maxhp*0.75))
    if ajj == 1:
        sound("ljud/oj_aj.wav")
    return player


def E_room(player):
    print("Dette rum er tomt.")
    print("Det finns inget mer att säga liksom.")
    return player


def N_room(player):

    print("Mattanten: Hej! Jag har lagat ett litet experimentellt recept som du bara MÅSTE prova.")

    time.sleep(1)

    weights = [1, max(1, int(player.charisma))]

    rand.randint(0,100)

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
            print(f"Mattanten serverade dig god mat! Du återhämtar {actual_healed} {hp_or_aura(player)}.")
            print(player.takes_damage())

    time.sleep(1)

    return player



def room_chooser(room, player, boss=None, trap_message="", audio_file=0):
    if room == "Ont rum":
        monster_hp = round(player.level *1.10 * rand.randint(7, 15))
        base_attack = round(player.level *1.1 + 0.23 * monster_hp) #bara formel som förhoppningsvis är balancerad
        monster_attack = max(1, base_attack + rand.randint(-1, 1)) #max ifall ekvationen skulle ge tall under 1 (max väljer argumentet som är störst )

        return O_room(player, Monster(monster_hp, monster_attack, False))
    elif room == "Bossrum":
        return B_room(player)
    elif room == "Gott rum":
        return G_room(player)
    elif room == "Fällrum":
        return T_room(player, rand.randint(2,4), rand.randint(1,5))
    elif room == "Tomt rum":
        return E_room(player)
    elif room == "Neutralt rum":
        return N_room(player)