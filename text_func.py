import sys, time, os
import random as rand
def buffered_type(str, speed):
    for letter in str:
        sys.stdout.write(letter) #skriver en bokstav (utan radbrytning)
        sys.stdout.flush()  #Gör så att texsten väntar med att skiva ut allt sammtidigt 
        time.sleep(speed)   #Hastighet
    print("\n")

def typo():
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

def hp_or_aura(player):
    if player.grisch == True:
        return "Aura"
    else:
        return "HP"

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

