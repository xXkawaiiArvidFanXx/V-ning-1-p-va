#Här skapas en karta och rummen slumpas fram
#karta grid lista i lista 
#map = kartan
#Börja med map creation för att skapa kartan
#med funktionen Print_map() så kan du skriva ut kartan i terminalen
import random as rand

def Map_Creation():
    map = []
    map_size = 7 #bestämmer storlek på kartan
    for i in range (map_size): #En tom kart mall skapas
        map.append([0,0,0,0])

    for a in range (map_size):
        for b in range (4): #här slumpas rummens egenskaper fram N = Neutralt 
            #G = gott/GOOd O = Ont/OEvil   T = Trap/fälla kanske R = Renoveras B = BOSS
            Room_Type = ["N","G","O","T"]

            map[a][b]=(Room_Type[rand.randint(0,3)])

    #Bossmodul
    #Alltid en boss 1 i mittenrummet 
    #Boss 2 är alltid i sista rummet???
    map[2][2] = "B"
    return map
def Print_map():
    for row in map: #Hur man kan skiva ut kartan fint
        print(row)

map = Map_Creation()