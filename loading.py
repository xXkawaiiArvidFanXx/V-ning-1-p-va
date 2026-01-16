import time
from text_func import *
from soundengine import *
#Med game_loading() SKrivs en estetsik lista ut där det verkar som att spelet "laddar ner"massa filer
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
    clear_terminal()
    return

def endcredits_common_names():
    buffered_type("Elias kronofogsvans (såg)", 0.2)
    buffered_type("Den kvalificerade Fofilolipop", 0.2)
    buffered_type("Den något kortare Frej", 0.2)

def endcredits_headline(i):
    row_marker()
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
    row_marker()
    buffered_type("Karta samt inledandet av spar funktion", 0.1)
    buffered_type("Den något kortare Frej", 0.2)
    time.sleep(2)
    row_marker()
    buffered_type("Projektöverseende fellstavningar och rum (inte hotell hahahahaha kanske (stav))", 0.1)
    buffered_type("Den kvalificerade Fofilolipop", 0.2)
    time.sleep(2)
    row_marker()
    buffered_type("Inventory, buggar och hälsoflaskor det är viktigt", 0.1)
    buffered_type("Elias kronofogsvans (såg)", 0.2)
    time.sleep(2)
    row_marker()
    print("Tack för att du spelade!")
    time.sleep(2)
    row_marker()
    print("Slutcredits musik spelas nu upp...")
    print("alla buggfixade")
    row_marker()
    time.sleep(10)
    buffered_type("""    
10/10!!!
Från och med första textraden och noten så var jag
trollbunden till detta charmiga indie-textäventyrsspel. 
Jag var som förälskad med alla karaktärer, 
speciellt den grischiga Fatima som jag hade äran att gestalta min första runda.
De kreativa vapnena och fiendenamnen lockar till tårar, 
mest ledsna med fienderna, men bryter aldrig den magi som har ingjutits av 
de otroligt professionella (och snygga om jag får säga det själv) kreatörerna. 
Ett spel för alla som alltid kan spelas, vare sig ålder, kön eller längd.

//Imponerad Scout (såna ser man inte ofta)
    """, 0.04)
    return 