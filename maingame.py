# här ska vi skapa vår huvuddel av spelet och imporera klasser etc eftersom vi jobbar
# from player import *
# from loading import *
# from map_module import * 
# from soundengien import *
# importera där de behövs annar kommer de printas i start




def startgame(): #starten till spelet, här ska man välja om man ska skapa en ny sparfil eller om man vill importera en sparad version
    print("Välkommen till första våningen på åva")
    startchoice = input("Välj 1 om du vill starta ett nytt spel eller 2 om du vill ladda in en sparfil")
    if startchoice == "1":
        print("du har valt att starta ett nytt spel")
        #här körs main
        pass
    elif startchoice == "2":
        print("du har valt att ladda in en sparfil")
        #här ska vi skapa en load save funktion
        pass
    else:
        print("FEL val, locka in och försök igen")
        startgame()
    print("Vad för klass vill du spela som?")

def maingame():
    # här kör vi huvudspelet
    while player.hp > 0:
        



