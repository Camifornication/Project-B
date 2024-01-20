import json
import requests
from tkinter import *
import datetime

jort_ID = 76561198424424214
camiel_ID = 76561199075949807
abi_ID = 76561199499642445
joeri_ID = 76561198811411788
viggo_ID = 76561198901321655
chris_ID = 76561199055661530

steam_api_key = "61D1D964724B68FC9F340D584CD500E3"
user_id = "76561198424424214"

"""
Zoek functies
"""
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

"""
Sorteer functies
"""
def sort_list(lst):       #sort function selection sort? (vgm is het bubble sort)
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

def sort_list_with_dicts(lst):
    index = 0
    lst_sorted = lst.copy()
    gewisseld = True
    while gewisseld:
        gewisseld = False
        for i in range(0, len(lst_sorted) - 1):
            if list(lst_sorted[i].values())[index] > list(lst_sorted[i + 1].values())[index]:
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                gewisseld = True
    return lst_sorted

def sort_dict_on_values(input_dict):
    items = list(input_dict.items())
    gewisseld = True
    while gewisseld:
        gewisseld = False
        for i in range(0, len(items) - 1):
            if items[i][1] < items[i + 1][1]:
                gewisseld = True
                items[i], items[i + 1] = items[i + 1], items[i]
    dict_sorted = dict(items)
    return dict_sorted

"""
Get json file functies / api
"""
def get_json_file(steam_api_link):
    response = requests.get(steam_api_link)
    data = response.json()
    return json.dumps(data, indent=2)
def get_all_games():
    return get_json_file('https://api.steampowered.com/ISteamApps/GetAppList/v2')

def get_recently_played_games(steamid):
    return get_json_file(f'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={steam_api_key}&steamid={steamid}&count=10')

def get_friendlist(steamid):
    return get_json_file(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={steamid}&relationship=friend")

def get_player_info(steamid):
    return get_json_file(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={steamid}")

def get_personaname(steamid):
    response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={steamid}")
    data = response.json()
    personaname = data['response']['players'][0]['personaname']
    return personaname

"""
Tijd functies
"""
def unix_to_normal(unix_date):
    datetime_object = datetime.datetime.fromtimestamp(unix_date)

    date_format = "%d-%m-%Y %H:%M"
    return datetime_object.strftime(date_format)

"""
functies voor informatie
"""
def get_friendlist_ids(steamid):
    friend_ids_list = []

    response = requests.get(
        f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={steamid}&relationship=friend")
    data = response.json()
    for friend in data['friendslist']['friends']:
        friend_id = friend['steamid']
        friend_ids_list.append(friend_id)
    return friend_ids_list

def get_friends_recent_games(steamid):
    friends_recent_games_list = []
    recent_games_count = {}
    for friendid in get_friendlist_ids(steamid):
        response = requests.get(
            f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={steam_api_key}&steamid={friendid}&count=10")
        data = response.json()
        if 'games' in data['response']:
            for game in data['response']['games']:
                friends_recent_games_list.append(game['name'])

    for game in friends_recent_games_list:
        if game in recent_games_count:
            recent_games_count[game] += 1
        else:
            recent_games_count[game] = 1
    return recent_games_count


def get_friend_info(steamid):
    friend_info_list = []
    friend_ids_list = get_friendlist_ids(steamid)
    for friendid in friend_ids_list:
        response = requests.get(
            f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={friendid}")
        data = response.json()

        personaname = data['response']['players'][0]['personaname']

        if 'lastlogoff' in data['response']['players'][0]:
            lastlogoff = data['response']['players'][0]['lastlogoff']
            lastlogoff = unix_to_normal(lastlogoff)
        else:
            lastlogoff = "N/A"

        if 'personastate' in data['response']['players'][0]:
            personastate = data['response']['players'][0]['personastate']
            if personastate == 0:
                online_status = "Offline"
            elif personastate == 1:
                online_status = "Online"
            elif personastate == 2:
                online_status = "Do Not Disturb"
            elif personastate == 3:
                online_status = "Away"
            elif personastate == 4:
                online_status = "Snooze"
        else:
            online_status = "N/A"

        if 'loccountrycode' in data['response']['players'][0]:
            countrycode = data['response']['players'][0]['loccountrycode']
        else: countrycode = "N/A"

        friend_info_dict = {'personaname': personaname, 'onlinestatus': online_status, 'lastlogoff': lastlogoff, 'countrycode': countrycode}
        friend_info_list.append(friend_info_dict)
    return friend_info_list

"""
GUI
"""
def main_gui():
    steamid = steamid_input.get()

    root1.destroy()

    root2 = Tk()

    root2.geometry("1200x600")
    root2.title("Main screen")

    personaname = get_personaname(steamid)

    lbl = Label(master=root2, text=f"Welcome {personaname}", anchor='center')
    lbl.grid(column=0, row=0, columnspan=2)

    lbl2 = Label(master=root2, text=f"friendlist")
    lbl2.grid(column=0, row=1)

    btn = Button(master=root2, text="Sort")
    btn.grid(column=1, row=1, sticky="NESW")
    "sort knop staat op prima plek, combobox werkt nog niet"

    # options = ['Sort ascending', 'sort descending']
    # combobox_sort_friendlist = Combobox(master=root2, values=options)
    # combobox_sort_friendlist.grid(column=1, row=1, sticky="NESW")

    listbox_friends = Listbox(master=root2, selectmode=SINGLE, height=30, width=65)
    #
    # # scrollbar = Scrollbar(root2, command=listbox_friends.yview)
    # # scrollbar.pack(side=RIGHT, fill=Y)
    #
    # # listbox_friends.config(yscrollcommand=scrollbar.set)

    # friendinfo_lst, friend_info_list, top3games = last_logoff_friendlist(steamid)

    friend_info_list = get_friend_info(steamid)
    for friend in friend_info_list:
        personaname = friend['personaname']
        onlinestatus = friend['onlinestatus']
        listbox_friends.insert(END, f"{personaname} - {onlinestatus}")
    listbox_friends.grid(column=0, columnspan=2, row=2)

    lbl_friendsareplaying = Label(master=root2, text="Friends are playing:")
    lbl_friendsareplaying.grid(column=2, row=1)

    listbox_friend_games = Listbox(master=root2, selectmode=SINGLE, height=5, width=65)
    recent_games_count = get_friends_recent_games(steamid)
    recent_games_sorted = list(sort_dict_on_values(recent_games_count).keys())[:5]
    for game in recent_games_sorted:
        listbox_friend_games.insert(END, game)
    listbox_friend_games.grid(column=2, row=2, sticky='N')

    root2.mainloop()

def loading_screen():
    global loadingscreen
    loadingscreen = Tk()
    loadingscreen.title("Loading Screen")
    loadingscreen.geometry("1200x600")

    loading_lbl = Label(master=loadingscreen, text="Loading...")
    loading_lbl.pack()

    loadingscreen.mainloop()
def login_gui():
    global root1
    global steamid_input
    root1 = Tk()
    root1.geometry("1200x600")
    root1.title("Login")
    # root.resizable(0,0)
    root1.configure(bg="#1b2838")

    lbl1 = Label(master=root1, text="What is your steam ID?", bg="#66c0f4")
    lbl1.pack(pady=20)

    steamid_input = Entry(master=root1)
    steamid_input.pack()

    confirm_btn = Button(master=root1, text="Confirm", command=main_gui)
    confirm_btn.pack(pady=20)


    root1.mainloop()

login_gui()



# print(friend_info_list)