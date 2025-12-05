import random as rand

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

def T_room(player, trap_damage, trap_message,audio_file):
    """Om det inte finns någon ljudfil, sätt audio_file till 0"""
    print(trap_message)
    if audio_file == 0:
        pass
    else:
        # Spela upp ljudfilen här
        pass
    player.hp -= trap_damage
    print(player.takes_damage())
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