import json
with open("steam.json", 'r') as json_file:
    data = json.load(json_file)

    for game in data:
            print(game['name'], 'heeft',game['positive_ratings'], "positieve ratings")
            break





with open("steam.json", 'r') as json_file:
    data = json.load(json_file)

    for game in data:
        if game["name"] == "The Witcher 3: Wild Hunt":
            print(game['name'], 'heeft', game['positive_ratings'], "positieve ratings")




