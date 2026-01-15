import time
from text_func import *
from soundengine import *
#Med game_loading() SKrivs en estetsik lista ut där det verkar som att spelet laddar ner massa filer
def game_loading():
    """En Estetisk funktion"""
    clear_terminal()
    backgroundmusic("ljud/bakgrund.wav")
    print("Spelet upplevs bäst med hörlurar eller suround sound med dolby atmos och high fidelity högtalare (rekomenderad mängd 5000 watt och 50 högtalare)")
    time.sleep(2)
    print("Laddar pojken...(viktig plot device)")
    time.sleep(1)
    print("Laddar trummor...")
    time.sleep(0.5)
    print("Laddar gitarrer...")
    print("Speltips: Använd kartan, den kan ge dig vital information")
    time.sleep(0.7)
    print("Laddar orkester...")
    time.sleep(1.2)
    print("Laddar bas...")
    time.sleep(0.5)
    print("Speltips : Det kan vara bra att utrusta ditt vapen innan du börjar slåss!")
    time.sleep(1.9)
    print("Laddar trumpeter...")
    time.sleep(1.1)
    print("Laddar fioler...")
    time.sleep(0.8)
    print("Laddar trummor igen...")
    time.sleep(0.1)
    print("Laddar berättaröst...")
    time.sleep(1.3)
    print("Laddar lite annat gojs...")
    time.sleep(0.1)
    print("Speltips : Gå inte in i dom vassa väggarna")
    time.sleep(2.6)
    print("Ett Spel Av")
    time.sleep(0.5)
    print("invänta dramatisk musik")
    time.sleep(1)
    print("!!    Studio FL    !!")
    stopmusic()
    sound("ljud/intro.wav")
    time.sleep(2)
    backgroundmusic("ljud/bakgrund.wav")
    clear_terminal()
    return
    # Här skulle du lägga in kod för att spela upp ett ljud

def endcredits_common_names():
    buffered_type("Elias kronofogsvans (såg)", 0.2)
    buffered_type("Den kvalificerade Fofilolipop", 0.2)
    buffered_type("Den något kortare Frej", 0.2)

def endcredits_headline(i):
    print ("=========================================================================================================================")
    if i == 1:
        buffered_type("Programering" , 0.1)
    elif i == 2:
        buffered_type("Speldesign", 0.1)
    elif i == 3:
        buffered_type("Musik och Ljuddesign", 0.1)
    elif i == 4:
        buffered_type("Balans och Spelmekanik", 0.1)
    elif i == 5:
        buffered_type ("Balans och Spelmekanik", 0.1) 
    elif i == 6:
        buffered_type ("Monsterdesign", 0.1)

def endcredits():
    """Spelar upp slutcredits"""
    clear_terminal()
    for i in range(1,6):
        endcredits_headline(i)
        endcredits_common_names()
        if i == 5:
            buffered_type("tåbiah (raggmunk)", 0.2)
    print ("=========================================================================================================================")
    buffered_type("Karta samt inledandet av spar funktion", 0.1)
    buffered_type("Den något kortare Frej", 0.2)
    time.sleep(2)
    print ("=========================================================================================================================")
    buffered_type("Projektöverseende fellstavningar och rum (inte hotell hahahahaha kanske (stav))", 0.1)
    buffered_type("Den kvalificerade Fofilolipop", 0.2)
    time.sleep(2)
    print ("=========================================================================================================================")
    buffered_type("Inventory, buggar och hälsoflaskor det är viktigt", 0.1)
    buffered_type("Elias kronofogsvans (såg)", 0.2)
    time.sleep(2)
    print ("=========================================================================================================================")
    print("Tack för att du spelade!")
    time.sleep(2)
    print ("=========================================================================================================================")
    print("Slutcredits musik spelas nu upp...")
    print("alla buggfixade")
    print ("=========================================================================================================================")
    time.sleep(10)
    return 