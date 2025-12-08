import random as rand
from player import *
from soundengien import *
def fight(player, enemy):
    while player.hp > 0 and enemy.monsterhealth > 0:
        enemy.monsterhealth -= player.strenght
        print(enemy.takes_damage())

        player.hp -= enemy.monsterdamage
        print(player.takes_damage())

    if enemy.monsterhealth <= 0:
        print(f"Du har besegrat {enemy.monstername}!")
    else:
        print("Du har blivit besegrad...")
        print("försök att inte suga så mycket nästa gång!")


def O_room(player, monster):
    fight(player, monster)
    gissning = input("Om du vill kan du vila och kanske återhämta lite hälsa, men då måste du gissa rätt. 1, 2 eller 3? ")
    if gissning == "4":
        if player.hp == player.maxhp:
            print("Du har redan full hälsa, du kan inte vila nu.")
            return player.hp
        else:
            hpregen = player.maxhp - player.hp
            if hpregen > 5:
                hpregen = 5
            else:
                pass
            genhp =+ rand.randint(hpregen,3)
            print(f"snyggt du genererar {genhp} hp") 
            player.hp += genhp

    else:
        print("Fel gissning, ingen hälsa återhämtad.")
    return player.hp

def B_room(player, boss):
    if player.pos_y == player.boss_room_cleared_posistion_y and player.pos_x == player.boss_room_cleared_posistion_x :
        print("Du har redan besegrat bossen i detta rum.")
        return
    else:
        if boss.room_cleared == 0:
            fight(player, boss)
            player.boss_room_cleared += 1
            player.boss_room_cleared_posistion_y = player.pos_y
            player.boss_room_cleared_posistion_x = player.pos_x
            player.hp = player.max_hp
        if boss.room_cleared == 1:
            fight(player, boss)
            player.boss_room_cleared += 1
    return player.hp, boss.room_cleared, player.boss_room_cleared_posistion_y, player.boss_room_cleared_posistion_x

def G_room(player):
    print("Du har hittat ett gott rum och en hälsodryck och dricker den!")
    heal_amount = rand.randint(1, 2)
    player.hp =+ heal_amount
    return player.hp




def traptypes(num):
    if num == 1:
        trap_message = """Du går fram med raska men bestämda steg och kommer fram till att du ska köpa en chokladboll. Du lägger fram 25 kr som du gjort orimligt många gånger innan." 
        Men personalen i kiosken kollar på dig som om du är en idiot och pekar på priserna.
        Det är ju 50 för en chokladboll, med nyfunnen skam i kroppen så tar du tillbaka dina 25 kronor och går med ett sänkt huvud bort från kiosken ."""
        audio_file = "ljud\kiosken.wav "
    elif num == 2:
        trap_message = "Du går ner för en liten trappnednång på tre steg. Plötsligt tappar du fotfästet och faller handlöst ner för trappan och landar hårt på marken."
        audio_file = "fall.wav"
    elif num == 3:
        trap_message = "Du ser en väg in till rum 3545 (Workshopen) och tänker skapa ett vapen av materialen. Men när du ska skruva märker du att philips bittsen du satte in inte var rätt och pozidriv skruven skuts ut från ditt vapen och landar i ditt öga."
        audio_file = "pil.wav"
    elif num == 4:
        # hiss incident
        pass
    else:
        trap_message = "När du öppnar dörren till det rum du går fram till ser du bara mörker, men Mamma didnt raise no chicken. När du går in gör du illa dig på något vasst i mörkret."
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
        sound("ljud\Aj.wav")
    return player.hp


def E_room():
    print("Detta rum är tomt.")
    print("Det finns inget mer att säga liksom.")


def N_room(player):
    print("Mattanten: Hej! Jag har lagat ett litet experimentellt recept som du bara MÅSTE prova.")
    random_number = rand.choice("äcklig_mat", "god_mat", weights=[20, 5*player.charisma])
    if random_number == "äcklig_mat":
        print("Mattanten serverade dig äcklig mat! Du tappar hälsa.")
        player.hp -= 2
        print(player.takes_damage())
    else:
        print("Mattanten serverade dig god mat! Du återhämtar hälsa.")
        player.hp += 3
    return player.hp


def room_chooser(room, player, boss=None, trap_message="", audio_file=0):
    if room == "Ont rum":
        return O_room(player, Monster(20, 3, "Zombienbobi"))
    elif room == "Bossrum":
        return B_room(player, boss)
    elif room == "Gott rum":
        return G_room(player)
    elif room == "Fällrum":
        return T_room(player, rand.randint(2,4), rand.randint(1,3))
    elif room == "E":
        return E_room()
    elif room == "Tomt rum":
        return N_room(player)