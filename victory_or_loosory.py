def victory_speach(player):
    print(f"Efter att du dödat 'le homme féminin Wilmér' så kommer pojken och sen vann du och ditt namn, {player.name}. Blev inristat i väggarna på åva")
    print("hejdå")
def victory_or_loosory(player):
    if player.boss_room_cleared == 2:
        victory_speach(player)
    else:
        print("du dog")
