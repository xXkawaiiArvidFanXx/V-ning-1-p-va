# Här ska du kunna Kalla på Turtle_Map() lite som google maps och se kartan i turtle
# man ska kunna se planlösningen med frågetecken i dem rum man inte varit i
# och se vad som varit i dem rum man varit i, 
# man ska se vart man är 

import turtle
from map_module import *
from player import *
from slowtype import *
from maingame import *
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

    t.penup()
    # en for loop som går igenom alla rum 4*7 och skriver ut Vad som finns i dem (täks med ? om ett tag)
    t.speed(-1)
    for a in range (1,5):
        for i in range (7):
            t.goto(-300+75*i,200-75*a)
            Write_room(i,a-1)
    #använd player pos som variabler x och y
    Player = t.Turtle()
    Player.color("red")
    Player.shape("turtle")
    Player.penup()
    Player.goto(-300+75*(x+3)+37,200-75*(y-2)-37)
    Player.pendown()

    Loop = True
    while Loop == True:
        action = turtle.textinput("Är du klar eller vill du se kartan skrivas upp en gång till?", """Y = en gång till, q = Släpp mig ut
        Ta bort rutan genom att trycka på X när du kollat klart på kartan""")
        if action == "Y":
           Turtle_maps(player.pos_x, player.pos_y)
        elif action == "q":
            t.done()
            break
        else:
            deadahh()
            time.sleep(3)
            slowtype("Lägg ägg med Felskrivandet",0.1)
            
    
t = turtle
#Spelaren = Player(2,2,2,2) # Denna ska bort och Spelaren.pos_x, Spelaren.pos_y ersätts med namn på spelaren
Print_map()
Turtle_maps(player.pos_x, player.pos_y)
