from player import *
from fight import *

player = Player(20, 5, "Hero", 10)

enemy = Monster(15, 3, "Goblin")
fight(player, enemy)    

#ta bort när spelet är klart