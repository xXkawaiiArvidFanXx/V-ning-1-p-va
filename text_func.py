import sys, time, os
import random as rand
def buffered_type(str, speed):
    for letter in str:
        sys.stdout.write(letter) #skriver en bokstav (utan radbrytning)
        sys.stdout.flush()  #Gör så att texsten väntar med att skiva ut allt sammtidigt 
        time.sleep(speed)   #Hastighet
    print("\n")

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def hp_or_aura(player):
    if player.grisch == True:
        return "Aura"
    else:
        return "HP"

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


def anoying_name(player):
        """står player iställer för playername men de ska vara ett namn här inte en player objekt"""
        i=0
        
        name = input("Innan du börjar ditt äventyr vill jag först veta ditt namn!\nHej, jag heter: ")
        if name == "":
            buffered_type(f"Du skrev ingenting, därmed blir ditt namn {player}!\n", 0.1)
        
        elif player.lower() != name.lower():

            name = name.capitalize()

            yes_or_no = input(f"Du skrev {name}, \nMenade du {player} \nJa eller Nej\n")
            while yes_or_no.lower() != "ja": 
                clear_terminal()
                time.sleep(0.5)
                if i <= 3:
                    yes_or_no = input(f"Förlåt jag såg inte om du skrev ja eller nej \nKan du svara igen?\n")
                    i += 1
                elif i <= 7:
                    yes_or_no = input(f"Allvarligt, ge dig. Skriv bara ja\n")
                    i += 1
                elif i <= 14:
                    typo()
                    yes_or_no = input(f"KOOOOOOOOOOOOOOM IGEEEEEEEEEEEEENNNNNNNNNN\n")
                    i += 1
                elif i <= 20:
                    yes_or_no = input(f"Om du fortsätter kommer ditt beteende få konsikvenser\n")
                    i += 1
                elif i <= 21:
                    last_trick = input(f"Skriv inte ja om du inte vill heta {name}! ")
                    if last_trick.lower() != "ja":
                        yes_or_no = "ja"
                    i += 1
                elif i <= 22:
                    buffered_type(f"Okej du vinner, ditt namn är nu {name}", 1)
                    time.sleep(2)
                    buffered_type("Var det värt det?", 1.5)
                    time.sleep(2)
                    buffered_type("aja, lycka till", 2)
                    player = name
                    return player
                
            buffered_type(f"Okej\n", 0.1)
        return player