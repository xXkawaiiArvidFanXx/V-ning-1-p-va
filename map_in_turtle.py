# Här ska du kunna Kalla på Turtle_Map() lite som google maps och se kartan i turtle
# man ska kunna se planlösningen med frågetecken i dem rum man inte varit i
# och se vad som varit i dem rum man varit i, 
# man ska se vart man är 

import turtle
from map_module import *
from slowtype import *
t = turtle

def Write_room(x,y):
    for i in range (4):
        t.pendown()
        t.forward(60)
        t.right(90)
        t.penup()
    t.right(50)
    t.forward(45)
    t.write(map[x][y])
    t.back(42)
    t.left(50)
    t.penup()
    

def Turtle_maps(x,y): #kanske en lista för icke hittade rum
    """player.pos_x, player.pos_y"""
    wn = turtle.Screen()
    wn.tracer(0) 
    t.penup()
    t.speed(-1)
    t.hideturtle()
    
    # en for loop som går igenom alla rum 4*7 och skriver ut Vad som finns i dem (täks med ? om ett tag)
    for a in range (1,5):
        for i in range (7):
            t.goto(-300+75*i,200-75*a)
            Write_room(i,a-1)
            wn.update()
            time.sleep(0.5)
    #använd player pos som variabler x och y
    pos = t.Turtle()
    pos.color("red")
    pos.shape("turtle")
    pos.penup()
    pos.goto(-300+75*(x+3)+37,200-75*(y-2)-37)
    pos.pendown()
    wn.update() 
    Loop = True
    while Loop == True:
        action = turtle.textinput("Är du klar eller vill du se kartan skrivas upp en gång till?", """Y = en gång till, q = Släpp mig ut""")
        if action == "Y":
           Turtle_maps(x, y)
        elif action == "q":
            wn.bye()
            break
        else:
            deadahh()
            time.sleep(3)
            slowtype("Lägg ägg med Felskrivandet",0.1)

#if __name__ == "__main__":
#    # Demo / manual test: import Player here to avoid circular import during module import
#    from player import Player
#    player = Player(20, 2, "magis", 3, "lububu")
#    Turtle_maps(player)
