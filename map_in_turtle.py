# Här ska du kunna Kalla på Turtle_Map() lite som google maps och se kartan i turtle
# man ska kunna se planlösningen med frågetecken i dem rum man inte varit i
# och se vad som varit i dem rum man varit i, 
# man ska se vart man är 

import turtle
from map_module import *
from text_func import *
t = turtle

def Write_room(x,y, game_map):
    for i in range (4):
        t.pendown()
        t.forward(60)
        t.right(90)
        t.penup()
    t.right(50)
    t.forward(45)
    t.write(game_map[x][y])
    t.back(42)
    t.left(50)
    t.penup()
    
def Turtle_maps(x,y,game_map): #kanske en lista för icke hittade rum
    """player.pos_x, player.pos_y"""
    t = turtle
    wn = turtle.Screen()
    wn._root.deiconify() #återställer fönstret (behövde göra en workaround då turtle är mer eller mindre tänk att vara hela programet. (Igentligen inte så bra då en uppdatering till turtle skulle kunna förstöra alting, men funkar som en snabb lösninng))
    wn.tracer(0)
    t.penup()
    t.speed(-1)
    t.hideturtle()
    t.clear()
    # en for loop som går igenom alla rum 4*7 och skriver ut Vad som finns i dem (täks med ? om ett tag)
    for a in range (1,5):
        for i in range (7):
            t.goto(-300+65*a,225-65*i)
            Write_room(i,a-1,game_map)
            wn.update()
            time.sleep(0.5)
    #använd player pos som variabler x och y
    pos = t.Turtle()
    pos.clear()
    pos.shapesize(stretch_wid=1.5, stretch_len=1.5)
    pos.color("red")
    pos.shape("circle")
    pos.penup()
    pos.goto(-435+65*(x+3)+35, 25-65*(y-3)-30)
    pos.pendown()
    t.forward(90)
    t.write(""" 
 DU ÄR HÄR -->
 G = Gott rum
 T = Fälla
 E = Tomt rum
 O = Ont rum
 N = Neutralt rum
 B = Boss Rum """,font=("Creepster", 24, "bold"))
    player_map_icon = t.Turtle()
    player_map_icon.penup()
    player_map_icon.goto(290, 75)
    player_map_icon.shapesize(stretch_wid=1.5, stretch_len=1.5)
    player_map_icon.color("red")
    player_map_icon.shape("circle")

    wn.update()
    Loop = True
    while Loop == True:
        time.sleep(3)
        action = turtle.textinput("kollat klart på kartan?", "q = Släpp mig ut")
        if action.lower() == "q":
            pos.hideturtle()
            wn._root.withdraw() #gömmer fönstret (del av workaround)
            break
        else:
            typo()
            time.sleep(3)
            buffered_type("Lägg ägg med Felskrivandet",0.1)

#Testning

#if __name__ == "__main__":
#    Map_Creation()
#    Turtle_maps(3,6)

#    # Demo / manual test: import Player here to avoid circular import during module import
#    from player import Player
#    player = Player(20, 2, "magis", 3, "lububu")
#    Turtle_maps(player)
