# här ska vi skapa vår huvuddel av spelet och imporera klasser etc eftersom vi jobbar
from os import name
from player import *
from text_func import *
from map_module import *
from fight_and_rooms import *
from save_funktion import *
import time

def class_chooser():
    buffered_type("""Välj din skollkaraktär!
 
(du kan inte leva ut dina vildaste fantasier i spelet med dom men endå)\n""", 0.01)
    while True:
        time.sleep(1)
        buffered_type("""1. Grisch har ett bälte som de kan använda som vapen, men de kan välja att springa ifrån en fiende fast då förlorar de aura och tappar byxorna. 
Däremot är grischpojken överdrivet självsäker som kanske kan komma till nytta. Grisch har Aura istället för Hp""", 0.01) #Självsäkerheten gör absolut ingenting, vi vill bara att man ska välja den sänsta karaktären.
        time.sleep(1)
        buffered_type("""2. Estet har en gitarr som de kan använda för att slå till sina fiender. Eftersom du har en gitarr har du hög karisma även fast du inte är en erfaren gitarr spelare då du endast har övat att spela trumpet hela ditt liv""", 0.01)
        time.sleep(1)
        buffered_type("3. Rektorn har en dator som kan användas för att skriva hem mejl, funkar för alla fiender (gör så att dom tar skada) men chans att stöta på tekniska problem och därmed förlorar man sin dator och fighten mot fienden", 0.01)
        time.sleep(1)
        buffered_type("""4. Lärare har fattat att pennan är mäktigare än svärdet. Speciellt när pennorna är vässade. Då du är en chill lärare så har du också relativt hög karisma""", 0.01)
        time.sleep(1)

        buffered_type("Välj nu noga vilken karaktär du väljer. Det kan komma att bli skillnaden mellan att bli en hjälte eller ett misslyckande", 0.01)
        time.sleep(1)
        character_selector = input("Välj nu din karaktär (1-4):")
        try:
            character_selector = int(character_selector)
            print("\n")

            if character_selector == 1:
                player_name = anoying_name("Fatima")
                player = Player(10, 1.5, player_name, 1.1, True)
                belt = weapon_create("bälte")
                player.add_item(belt)
                buffered_type("Du är nu den sämsta karaktären\n", 0.1)
                clear_terminal()
                print(f"Du är nu {player.name}, en grisch med hög (låg) aura \n")
                return player
            
            elif character_selector == 2:
                player_name = anoying_name("Phrank")
                player = Player(25, 1, player_name, 3, False)
                guitar = weapon_create("gitarr")
                player.add_item(guitar)
                print(f"Du är nu {player.name}, en estet med hög karisma \n")
                return player
            
            elif character_selector == 3:
                player_name = anoying_name("Geodor Von Tohn Fih")
                player = Player(15, 2, player_name, 1, False) 
                laptop = weapon_create("dator")
                player.add_item(laptop)
                print(f"Du är nu {player.name}, Rektorn på skolan med en mäktig dator \n")
                return player
            
            elif character_selector == 4:
                player_name = anoying_name("Geo Junior")
                player = Player(20, 2, player_name, 2.5, False)
                pen = weapon_create("penna")
                player.add_item(pen)
                print(f"Du är nu {player.name}, en lärare med en vass penna! \n")
                return player
            
            else:
                raise ValueError

        except ValueError:
            time.sleep(1)
            typo()
            time.sleep(5)
            buffered_type("Ogiltigt val, försök igen.", 0.1)
            time.sleep(1)



def maingame(player, game_map):
# här kör vi huvudspelet :D

    while player.hp > 0 and player.boss_room_cleared != 2:
        print("\n")
        row_marker()
        game_choice = input("Vad vill du göra? \n 1. Gå till rum. \n 2. Öppna Inventory/Stats. \n 3. Spara och avsluta. \n  ")
        try:
            game_choice = int(game_choice)

            if game_choice == 1:
                print("\n")
                player.pos_y, player.pos_x = player_position(player.pos_y, player.pos_x)
                room=get_room_type(player.pos_y, player.pos_x, game_map)
                player = room_chooser(room, player)
                

                
            elif game_choice == 2:
                inventory(player,game_map)
            elif game_choice == 3:
                if player.equipped_weapon == None:
                    print("Du måste ha ett vapen utrustat för att kunna spara spelet")
                    print("Tutorial: https://youtu.be/nWm1AwnhtY0")
                    continue
                return "save_game"
            else:
                raise ValueError

        except ValueError:
            time.sleep(1)
            typo()
            time.sleep(3)
            buffered_type("Ogiltigt val, försök igen.", 0.1)
            time.sleep(1)
    

def startgame(): #starten till spelet, här ska man välja om man ska skapa en ny sparfil eller om man vill importera en sparad version
    print("Välkommen till första våningen på åva \n")
    backgroundmusic("ljud/bakgrund.wav")

    try:    
        while True:
            startchoice = input("Välj 1 om du vill starta ett nytt spel eller 2 om du vill ladda in en sparfil!!! ")

            startchoice = int(startchoice)   

            if startchoice == 1:
                print("du har valt att starta ett nytt spel")
                return "new_game"
                    

            elif startchoice == 2:
                print("du har valt att ladda in en sparfil")
                #här ska vi skapa en load save funktion
                return "load_game"
                
    except ValueError:
        time.sleep(1)
        typo()
        time.sleep(3)
        buffered_type("Ogiltigt val, försök igen.", 0.1)
        time.sleep(1)
        startgame()
