# här ska vi skapa vår huvuddel av spelet och imporera klasser etc eftersom vi jobbar
from player import *
from loading import *
from map_module import * 
from soundengien import *
from slowtype import *
import time
# importera där de behövs annar kommer de printas i start

def class_chooser():
    ("""                Välj din skollkaraktär! 
    (du kan inte leva ut dina vildaste fantasier i spelet med dom men endå)""")
    while True:
        time.sleep(1)
        slowtype("1. Grisch har ett bälte som de kan använda som vapen, men de kan välja att springa ifrån en fiende fast då förlorar de aura och tappar byxorna. Grisch har Aura istället för Hp", 0.1)
        time.sleep(5)
        slowtype("""2. Estet har en gitarr som de kan använda för att slå till sina fiender. Gitarren kan man använda för att höja sin karisma men om du använder gitarren för att slåss kommer den gå sönder. 
                Om du försöker spela med en sönder gitarr kommer du tappa allt förutom en karisma poäng. Du är inte erfaren i gitarr eftersom att du endast har övat att spela trumpet hela ditt liv""", 0.1)
        time.sleep(10)
        slowtype("3. har dator som kan användas för att skriva hem mejl, funkar för alla fiender (gör så att dom tar skada) men chans att stöta på tekniska problem och därmed förlorar man sin dator och fighten mot fienden", 0.1)
        time.sleep(5)
        slowtype("""4. Lärare har fattat att pennan är mäktigare än svärdet. Speciellt när pennorna är vässade. 
                Men efter 3 användningar kan inte pennan användas utan att vässas pennans udd ska kunna gå sönder och pennan kan ha vässats sönder, då måste man spendera 2 rundor på att få tillbaka udden""", 0.1)
        time.sleep(10)

        print("Välj nu noga vilken karaktär du väljer. Det kan komma att bli skillnaden mellan att bli en hjälte eller ett misslyckande")
        time.sleep(2)
        character_selector = input("eller bara skit i det och välj det du känner för")
        try:
            character_selector = int(character_selector)
            if character_selector == 1:
                return Player()
            elif character_selector == 2:
                return Player()
            elif character_selector == 3:
                return Player()
            elif character_selector == 4:
                return Player()
            else:
                raise ValueError

        except ValueError:
            time.sleep(1)
            deadahh()
            time.sleep(5)
            slowtype("Ogiltigt val, försök igen.", 0.1)
            time.sleep(1)
def maingame(player):
# här kör vi huvudspelet :D
    while player.hp > 0:
        game_choice = input("Vad vill du göra? 1. Gå till rum. 2. Öppna Inventory/Stats. 3. Spara och avsluta. ")
        try:
            game_choice = int(game_choice)

            if game_choice == 1:
                # här ska vi kalla på map modulen och låta spelaren röra sig
                pass
            elif game_choice == 2:
                inventory(player)
            elif game_choice == 3:
                print("Sparar och avslutar spelet...")
                break
            else:
                raise ValueError

        except ValueError:
            time.sleep(1)
            deadahh()
            time.sleep(3)
            slowtype("Ogiltigt val, försök igen.", 0.1)
            time.sleep(1)



def startgame(): #starten till spelet, här ska man välja om man ska skapa en ny sparfil eller om man vill importera en sparad version
    print("Välkommen till första våningen på åva \n")
    
    while True:
        startchoice = input("Välj 1 om du vill starta ett nytt spel eller 2 om du vill ladda in en sparfil? ")

        try:
            startchoice = int(startchoice)   

            if startchoice == 1:
                print("du har valt att starta ett nytt spel")
                return "new_game"
            elif startchoice == 2:
                print("du har valt att ladda in en sparfil")
                #här ska vi skapa en load save funktion
                return "load_game"
            
            else:
                raise ValueError
        except ValueError:
            time.sleep(1)
            deadahh()
            time.sleep(3)
            slowtype("Det kan omöjligt vara så svårt, lock in", 0.1)
            time.sleep(1)


# Huvudprogrammet <3

game_mode = startgame()
player = class_chooser()
maingame(player)