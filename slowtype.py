import sys, time, os
import random as rand

def slowtype(str, speed):
    for letter in str:
        sys.stdout.write(letter) #skriver en bokstav (utan radbrytning)
        sys.stdout.flush()  #Gör så att texsten väntar med att skiva ut allt sammtidigt 
        time.sleep(speed)   #Hastighet
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

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')