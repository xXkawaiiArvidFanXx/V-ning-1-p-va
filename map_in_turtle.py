# Här ska du kunna Kalla på Turtle_Map() och se kartan i turtle
# man ska kunna se planlösningen med frågetecken i dem rum man inte varit i
# och se vad som varit i dem rum man varit i, 
# man ska se vart man är 
import turtle as t
from map_module import *

def Turtle_maps():
    Map = t.Turtle()
    t.penup()
    t.goto(-300,100)
    # en for loop som går igenom alla rum 4*7 och skriver ut Vad som finns i dem (täks med ? om ett tag)

    t.done()
