import json
import requests
from tkinter import *

steam_api_key = "61D1D964724B68FC9F340D584CD500E3"
user_id = "76561198424424214"
def get_json_file(steam_api_link):
    response = requests.get(steam_api_link)
    data = response.json()
    return json.dumps(data, indent=2)

def get_friendlist(user_id):
    return get_json_file(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={user_id}&relationship=friend")

print(get_friendlist(user_id))

def gui():
    root = Tk()
    root.geometry("1200x600")
    root.title("BeginGui")
    # root.resizable(0,0)
    lbl1 = Label(root, text="test")
    lbl1.pack()


    root.mainloop()

# gui()

def sorted():
    game_name_list = []
    with open('steam.json', 'r') as json_file:
        data = json.load(json_file)
        for game_name in data:
            game_name_list.append(game_name['name'])
        game_name_list.sort()
        for element in game_name_list:
            print(element)

# sorted()

