import json

def save_data(player, map_data):
    save_data = {
        "player": player,
        "map": map_data
    }

with open("savefile.json", "w") as file:
    json.dump(save_data, file, indent=4)


import json

with open("savefile.json", "r") as file:
    save_data = json.load(file)

player = save_data["player"]
map_data = save_data["map"]
