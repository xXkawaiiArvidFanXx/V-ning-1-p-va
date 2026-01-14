import time
from slowtype import clear_terminal
from soundengien import *
#Med game_loading() SKrivs en estetsik lista ut där det verkar som att spelet laddar ner massa filer
def game_loading():
    """En Estetisk funktion"""
    clear_terminal()
    backgroundmusic("ljud\\bakgrund.wav")
    print("Spelet upplevs bäst med hörlurar eller suround sound med dolby atmos och high fidelity högtalare (rekomenderad mängd 5000 watt och 50 högtalare)")
    time.sleep(2)
    print("Laddar pojken...(viktig plot device)")
    time.sleep(1)
    print("Laddar trummor...")
    time.sleep(0.5)
    print("Laddar gitarrer...")
    #print("Speltips: Kartan kan bara visas en gång annars krashar spelet")
    time.sleep(0.7)
    print("Laddar orkester...")
    time.sleep(1.2)
    print("Laddar bas...")
    time.sleep(0.9)
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
    #trumpet dramatisk spelmusik
    time.sleep(1)
    stopmusic()
    print("!!    Studio FL    !!")
    sound("ljud/intro.wav")
    time.sleep(2)
    clear_terminal()
    return
    # Här skulle du lägga in kod för att spela upp ett ljud