import json
import requests
from tkinter import *
import datetime
import threading

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


def binary_search(lst, target):  # binary search
    sorted_list = sort_list(lst)
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


def sort_list(lst):  # sort function selection sort? (vgm is het bubble sort)
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


def sort_list_with_dicts_by_onlinstatus(lst, button_state):
    if button_state == 0:
        index = 1
        lst_sorted = lst.copy()
        gewisseld = True
        while gewisseld:
            gewisseld = False
            for i in range(0, len(lst_sorted) - 1):
                if list(lst_sorted[i].values())[index] != 'Online' and list(lst_sorted[i + 1].values())[index] == 'Online':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                elif list(lst_sorted[i].values())[index] == 'Offline' and list(lst_sorted[i + 1].values())[index] != 'Offline':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                elif list(lst_sorted[i].values())[index] == 'Snooze' and list(lst_sorted[i + 1].values())[index] == 'Away':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                elif list(lst_sorted[i].values())[index] == 'Away' and list(lst_sorted[i + 1].values())[index] == 'Online':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                else:
                    continue
        return lst_sorted
    else:
        "online, away, snooze, offline"
        index = 1
        lst_sorted = lst.copy()
        gewisseld = True
        while gewisseld:
            gewisseld = False
            for i in range(0, len(lst_sorted) - 1):
                if list(lst_sorted[i].values())[index] == 'Online' and list(lst_sorted[i + 1].values())[index] != 'Online':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                elif list(lst_sorted[i].values())[index] != 'Offline' and list(lst_sorted[i + 1].values())[index] == 'Offline':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                elif list(lst_sorted[i].values())[index] == 'Away' and list(lst_sorted[i + 1].values())[index] == 'Snooze':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                elif list(lst_sorted[i].values())[index] == 'Snooze' and list(lst_sorted[i + 1].values())[index] == 'Offline':
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
                else:
                    continue
        return lst_sorted

def sort_list_with_dicts(lst, button_state):
    # if button_state == 0:
    index = 0
    lst_sorted = lst.copy()
    gewisseld = True
    while gewisseld:
        gewisseld = False
        for i in range(0, len(lst_sorted) - 1):
            if button_state == 0:
                if lst_sorted[i]['personaname'].lower() > lst_sorted[i + 1]['personaname'].lower():
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
            else:
                if lst_sorted[i]['personaname'].lower() < lst_sorted[i + 1]['personaname'].lower():
                    lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                    gewisseld = True
    return lst_sorted
    # else:
    #     index = 0
    #     lst_sorted = lst.copy()
    #     gewisseld = True
    #     while gewisseld:
    #         gewisseld = False
    #         for i in range(0, len(lst_sorted) - 1):
    #             if list(lst_sorted[i].values())[index].lower() < list(lst_sorted[i + 1].values())[index].lower():
    #                 lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
    #                 gewisseld = True
    #     return lst_sorted


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
    return get_json_file(
        f'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={steam_api_key}&steamid={steamid}&count=10')


def get_friendlist(steamid):
    return get_json_file(
        f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={steamid}&relationship=friend")


def get_player_info(steamid):
    return get_json_file(
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={steamid}")


def get_personaname(steamid):
    response = requests.get(
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={steamid}")
    data = response.json()
    personaname = data['response']['players'][0]['personaname']
    return personaname

def GetOwnedGames(steamid):
    return get_json_file(
        f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={steam_api_key}&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

def GetPlayerAchievements(steamid):
    return get_json_file(
        f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=440&key={steam_api_key}&steamid={steamid}")

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

def GetSteamLevel(steamid):
    response = requests.get(
        f"https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key={steam_api_key}&steamid={steamid}")
    data = response.json()
    print(data)
    if "player_level" in data['response']:
        friend_lvl = str(data["response"]["player_level"])
        return friend_lvl
    else:
        friend_lvl = "N/A"
        return friend_lvl

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
        else:
            countrycode = "N/A"

        if 'steamid' in data['response']['players'][0]:
            friendsteamid = data['response']['players'][0]['steamid']
        else:
            friendsteamid = "N/A"

        if 'realname' in data['response']['players'][0]:
            realname = data['response']['players'][0]['realname']
        else:
            realname = "N/A"

        friend_info_dict = {'personaname': personaname, 'onlinestatus': online_status, 'lastlogoff': lastlogoff,
                            'countrycode': countrycode,'realname': realname, 'friendsteamid': friendsteamid}
        friend_info_list.append(friend_info_dict)
    return friend_info_list


"""
GUI
"""


def sort_gui_friendlist_by_name():
    listbox_friends.delete(0, END)
    sorted_list = sort_list_with_dicts(friend_info_list, button_state)
    for friend in sorted_list:
        personaname = friend['personaname']
        onlinestatus = friend['onlinestatus']
        listbox_friends.insert(END, f"{personaname} - {onlinestatus}")
    # listbox_friends.grid(column=0, columnspan=2, row=3)

def sort_gui_friendlist_by_status():
    listbox_friends.delete(0, END)
    sorted_list = sort_list_with_dicts_by_onlinstatus(friend_info_list, button_state)
    for friend in sorted_list:
        personaname = friend['personaname']
        onlinestatus = friend['onlinestatus']
        listbox_friends.insert(END, f"{personaname} - {onlinestatus}")

def asc_desc():
    global button_state
    if button_state == 0:
        button_state = 1
        btn_asc_desc.config(text="Descending")
    else:
        button_state = 0
        btn_asc_desc.config(text="Ascending")

def friend_gui(event):
    selected_index = listbox_friends.nearest(event.y)
    if selected_index is not None:
        selected_item = listbox_friends.get(selected_index)
        print(f"Double-clicked on item: {selected_item}")
        username_friend, status_friend = str(selected_item).split(' - ')
        # print(friend_info_list)
        for i in range(0, len(friend_info_list)):
            if friend_info_list[i]['personaname'] == username_friend:
                clickedfriend_dict = friend_info_list[i]
                print(friend_info_list[i])
                break

        steamid = clickedfriend_dict["friendsteamid"]
        countrycode = clickedfriend_dict['countrycode']

        friend_lvl = GetSteamLevel(steamid)

        root_friend = Tk()

        root_friend.title("Friend")
        root_friend.geometry("400x500")

        friendnamelbl = Label(root_friend, text=f"{username_friend}")
        friendnamelbl.grid(row=0, column=0)

        friendstatuslbl = Label(root_friend, text=f"{countrycode}")
        friendstatuslbl.grid(row=1, column=0)

        friendlevellbl = Label(root_friend, text=f"level {friend_lvl}")
        friendlevellbl.grid(row=0, column=1)

        friend_recent_games_list = []
        response = requests.get(
            f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={steam_api_key}&steamid={steamid}&count=10")
        data = response.json()
        if 'games' in data['response']:
            listbox_recentgames_friend = Listbox(root_friend, selectmode=SINGLE, height=30, width=65)
            for game in data['response']['games']:
                print(game)
                friend_recent_games_list.append(game['name'])
            for game in friend_recent_games_list:
                listbox_recentgames_friend.insert(END, f"{game}")
            listbox_recentgames_friend.grid(row=2, column=0, columnspan=2)

        root_friend.mainloop()

def main_gui(steamid):
    global friend_info_list, listbox_friends, btn_asc_desc, button_state
    # global listbox_friends
    # global btn_asc_desc
    # global button_state
    button_state = 0
    root2 = Tk()

    root2.geometry("1200x600")
    root2.title("Main screen")

    personaname = get_personaname(steamid)

    lbl = Label(master=root2, text=f"Welcome {personaname}", anchor='center')
    lbl.grid(column=0, row=0, columnspan=2)

    lbl2 = Label(master=root2, text=f"friendlist")
    lbl2.grid(column=0, columnspan=2, row=1)

    btn_asc_desc = Button(master=root2, text="Ascending", command=asc_desc)
    btn_asc_desc.grid(column=0, row=2, sticky="NESW")
    # checkbox_state = BooleanVar()
    # checkbox = Checkbutton(master=root2, text="Descending", variable=checkbox_state, command=functie)
    # checkbox.grid(column=1, row=2, sticky="NESW")

    btn_sort_name = Button(master=root2, text="Sort by name", command=sort_gui_friendlist_by_name)
    btn_sort_name.grid(column=1, row=2, sticky="NESW")

    btn_sort_name = Button(master=root2, text="Sort by status", command=sort_gui_friendlist_by_status)
    btn_sort_name.grid(column=2, row=2, sticky="NESW")

    listbox_friends = Listbox(master=root2, selectmode=SINGLE, height=30, width=65)
    # scrollbar = Scrollbar(root2, command=listbox_friends.yview)
    # scrollbar.pack(side=RIGHT, fill=Y)
    #
    # listbox_friends.config(yscrollcommand=scrollbar.set)

    friend_info_list = get_friend_info(steamid)
    sorted_friendlist = sort_list_with_dicts_by_onlinstatus(friend_info_list, button_state)
    for friend in sorted_friendlist:
        personaname = friend['personaname']
        onlinestatus = friend['onlinestatus']
        listbox_friends.insert(END, f"{personaname} - {onlinestatus}")
    listbox_friends.grid(column=0, columnspan=3, row=3)

    listbox_friends.bind("<Double-Button-1>", friend_gui)

    lbl_friendsareplaying = Label(master=root2, text="Friends are playing:")
    lbl_friendsareplaying.grid(column=3, row=1)

    listbox_friend_games = Listbox(master=root2, selectmode=SINGLE, height=5, width=65)
    recent_games_count = get_friends_recent_games(steamid)
    recent_games_sorted = list(sort_dict_on_values(recent_games_count).keys())[:5]
    for game in recent_games_sorted:
        listbox_friend_games.insert(END, game)
    listbox_friend_games.grid(column=3, row=3, sticky="N")
    root1.destroy()
    root2.mainloop()

def create_gamelist():
    with open('steam.json', 'r') as file:
        data = json.load(file)
    # print(json.dumps(data, indent=2))
    all_games = []
    for i, game in enumerate(data):
        game_name = data[i]['name']
        game_id = data[i]['appid']
        game_price = data[i]['price']
        game_positive_ratings = data[i]['positive_ratings']
        game_negative_ratings = data[i]['negative_ratings']
        game_genre = data[i]['genres']
        game_release_date = data[i]['release_date']
        game_info_tuple = (game_name, game_id, game_price, game_positive_ratings, game_negative_ratings, game_genre, game_release_date)
        all_games.append(game_info_tuple)
    return all_games

def update_labels(games_frame, start, end):
    for label in games_frame.winfo_children():
        label.destroy()

    all_games = create_gamelist()
    for i, game in enumerate(all_games[start:end]):
        game_name_lbl = Label(master=games_frame, text=f"{game[0]}")
        game_name_lbl.grid(column=0, row=i, pady=3, sticky='W')
    for i, game in enumerate(all_games[start:end]):
        game_name_lbl = Label(master=games_frame, text=f"Price: {game[2]}$")
        game_name_lbl.grid(column=1, row=i, pady=3, padx=30, sticky='W')
    for i, game in enumerate(all_games[start:end]):
        game_name_lbl = Label(master=games_frame, text=f"Genre: {game[4]}")
        game_name_lbl.grid(column=2, row=i, pady=3, sticky='W')

def next_page():
    global start, end
    start += 20
    end += 20
    update_labels(games_frame, start, end)
    update_page_label()

def previous_page():
    global start, end
    start -= 20
    end -= 20
    update_labels(games_frame, start, end)
    update_page_label()

def update_page_label():
    page_label.config(text=f"Page {start // 15 + 1}")

def store_gui():
    global start, end, games_frame, page_label
    start = 0
    end = 20

    store = Tk()
    store.title("Steam Store")
    # store.geometry("1200x600")

    games_frame = Frame(master=store)
    games_frame.grid(column=0, columnspan=3, row=0, padx=100)

    previous_button = Button(master=store, text="<", font=("", 15), command=previous_page)
    previous_button.grid(column=0, row=1, pady=5, sticky="NESW")

    page_label = Label(master=store, text="Page 1")
    page_label.grid(column=1, row=1)

    next_button = Button(master=store, text=">", font=("", 15), command=next_page)
    next_button.grid(column=2, row=1, pady=5, sticky="NESW")

    update_labels(games_frame, start, end)

    store.mainloop()


def on_click():
    steamid = steamid_input.get()

    root1.title("Loading...")
    lbl1.config(text="Loading...", font=("", 20))
    steamid_input.destroy()
    confirm_btn.destroy()
    root1.update()
    main_gui(steamid)


root1 = Tk()
root1.geometry("1200x600")
root1.title("Login")
root1.configure(bg="#1b2838")

lbl1 = Label(master=root1, text="What is your steam ID?", bg="#66c0f4")
lbl1.pack(pady=20)

steamid_input = Entry(master=root1)
steamid_input.pack()

confirm_btn = Button(master=root1, text="Confirm", command=on_click)
confirm_btn.pack(pady=20)

root1.mainloop()

store_gui()