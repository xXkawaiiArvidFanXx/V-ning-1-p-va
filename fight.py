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


