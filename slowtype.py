import sys, time


def slowtype(str, speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def deadahh():
        print("""    
                  _____
                _/ _ _ \_  
               (o / | \ o)
                || o|o ||
                | \_|_/ |
                |  ___  |
                | (___) |
                |\_____/|
                | \___/ |
                \       /
                 \__ __/""")

def hp(player):
    if player.name == "Fatima":
        return "Aura"
    else:
        return "HP"