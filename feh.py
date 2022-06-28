import json
import random
import os

with open("$HOME/Code/scripts/data.json") as data_file:
    data = json.load(data_file)

if data['number'] == 3:
    rand = random.randint(1, 300)
    os.system('feh --bg-scale $HOME/Pictures/Wallpapers/{}.jpg'.format(rand))
    data["number"] = 0
    data["random"] = rand
else:
    prev = data["random"]
    os.system('feh --bg-scale $HOME/Pictures/Wallpapers/{}.jpg'.format(prev))
    data["number"] += 1

with open("$HOME/Code/scripts/data.json", "w") as write_file:
    json.dump(data, write_file)


