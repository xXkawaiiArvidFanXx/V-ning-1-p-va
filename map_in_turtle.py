# Här ska du kunna Kalla på Turtle_Map() och se kartan i turtle
# man ska kunna se planlösningen med frågetecken i dem rum man inte varit i
# och se vad som varit i dem rum man varit i, 
# man ska se vart man är 
import turtle as t
from map_module import *
Print_map()
def Write_room():
    t.pendown()
    for i in range (4):
        t.forward(60)
        t.right(90)
    t.penup()

def Turtle_maps():
    #Map = t.Turtle()
    t.penup()
    t.goto(-300,200)
    # en for loop som går igenom alla rum 4*7 och skriver ut Vad som finns i dem (täks med ? om ett tag)
    antal_rum=0
    t.speed(100000)
    for a in range (1,5):
        for i in range (7):
            Write_room()
            antal_rum +=1
            if antal_rum < 7:
                t.forward(80)
            else:
                t.goto(-300,(200-a*75))#vart den nu ska gå tillbaka till början fast längre ned 
                antal_rum = 0
        


    t.done()


Turtle_maps()
