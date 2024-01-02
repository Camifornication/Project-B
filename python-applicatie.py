import json
import requests
from tkinter import *

steam_api_key = "61D1D964724B68FC9F340D584CD500E3"
user_id = "76561198424424214"

def binary_search(lst, target):     #binary search
    sorted_list = my_sort(lst)
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_word = sorted_list[mid]
        if target == mid_word:
            return mid_word
        elif target < mid_word:
            high = mid - 1
        elif target > mid_word:
            low = mid + 1
    return "No results..."

def my_sort(lst):       #sort function selection sort? (vgm is het bubble sort)
    lst_sorted = lst.copy()
    gewisseld = True
    while gewisseld:
        gewisseld = False
        for i in range(0, len(lst_sorted) - 1):
            if lst_sorted[i] > lst_sorted[i + 1]:
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                gewisseld = True
            else:
                continue
    return lst_sorted

def get_json_file(steam_api_link):
    response = requests.get(steam_api_link)
    data = response.json()
    return json.dumps(data, indent=2)

def get_friendlist(user_id):
    return get_json_file(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={user_id}&relationship=friend")

# print(get_friendlist(user_id))

def get_player_info():
    return get_json_file(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={user_id}")

def last_logoff_friendlist():   #get each friend of friendlist with last logoff
    response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={user_id}&relationship=friend")
    data = response.json()
    steamid_list = []
    for friend in data['friendslist']['friends']:
        steamid = friend['steamid']
        steamid_list.append(steamid)
    for steamid in steamid_list:
        response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={steamid}")
        data = response.json()
        personaname = data['response']['players'][0]['personaname']
        lastlogoff = data['response']['players'][0]['lastlogoff']
        print(f"User: {personaname}, Last log-off: {lastlogoff}")

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

