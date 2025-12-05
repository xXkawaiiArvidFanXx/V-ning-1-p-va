
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

def B_room(player, boss):
    if player.pos_y == player.boss_room_cleared_posistion_y and player.pos_x == player.boss_room_cleared_posistion_x :
        print("Du har redan besegrat bossen i detta rum.")
        return
    else:
        if boss.room_cleared == 0:
            fight(player, boss)
        if boss.monsterhealth <= 0:
                player.boss_room_cleared += 1
                player.boss_room_cleared_posistion_y = player.pos_y
                player.boss_room_cleared_posistion_x = player.pos_x
        
