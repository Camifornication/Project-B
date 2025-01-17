import json
import requests
from tkinter import *
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from s_c import serial_communication, check_online, read_serial

jort_ID = 76561198424424214
camiel_ID = 76561199075949807
abi_ID = 76561199499642445
joeri_ID = 76561198811411788
viggo_ID = 76561198901321655
chris_ID = 76561199055661530

steam_api_key = "61D1D964724B68FC9F340D584CD500E3"
user_id = "76561198424424214"

blackish_blue = "#171a21"
light_blue = "#66c0f4"
darker_blue = "#1b2838"
dark_blue = "#2a475e"
grey = "#c7d5e0"

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

def binary_search_substring(list, target_string):
    target = target_string.lower()
    index = 0
    results = []
    low, high = 0, len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_word = list[mid]
        if target in mid_word[index].lower()[0:len(target)]:

            left = mid
            while left >= 0 and target in list[left][index].lower():
                results.append(list[left])
                left -= 1

            right = mid + 1
            while right < len(list) and target in list[right][index].lower():
                results.append(list[right])
                right += 1

            return results

        elif target < mid_word[index].lower():
            high = mid - 1
        elif target > mid_word[index].lower():
            low = mid + 1

    return results

"""
Sorteer functies
"""
def quicksort_lst_with_tuples(lst):
    index = 0
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        lesser = []
        greater = []
        for x in lst[1:]:
            if x[index].lower() <= pivot[index].lower():
                lesser.append(x)
            else:
                greater.append(x)
        return quicksort_lst_with_tuples(lesser) + [pivot] + quicksort_lst_with_tuples(greater)

def sort_list(lst):
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

def sort_list_with_tuples(lst):
    lst_sorted = lst.copy()
    gewisseld = True
    while gewisseld:
        gewisseld = False
        for i in range(0, len(lst_sorted) - 1):
            if lst_sorted[i][0] > lst_sorted[i + 1][0]:
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

def calculate_sse(a, b, X, y):
    n = len(y)
    predictions = [a + b * xi for xi in X]
    sse = sum((predictions[i] - y[i]) ** 2 for i in range(n))
    return sse


def gradient_descent(X, y, learning_rate, epochs):
    a = 0
    b = 0
    m = len(y)

    for epoch in range(epochs):
        predictions = [a + b * xi for xi in X]
        errors = [predictions[i] - y[i] for i in range(m)]

        a -= learning_rate * (1/m) * sum(errors)
        b -= learning_rate * (1/m) * sum(errors[i] * X[i] for i in range(m))

    return a, b

def linear_regression():
    price_list = []
    average_playtime_list = []
    with open('steam.json', 'r') as file:
        data = json.load(file)
    for i, game in enumerate(data):
        price = data[i]['price']
        average_playtime = data[i]['average_playtime']
        price_list.append(price)
        average_playtime_list.append(average_playtime)

    X = price_list
    y = average_playtime_list

    learning_rate = 0.01
    epochs = 1000

    a, b = gradient_descent(X, y, learning_rate, epochs)

    predicted_values = [a + b * xi for xi in X]

    sse = calculate_sse(a, b, X, y)

    fig, ax = plt.subplots(figsize=(4, 2), facecolor=darker_blue)
    plt.scatter(X, y, label='Actual values', s=5)
    plt.plot(X, predicted_values, color='red', label='Predicted values')
    plt.xlabel('Price ($)', fontsize=8, color=grey)
    plt.ylabel('Average playtime (minutes)', fontsize=8, color=grey)

    plt.xticks(fontsize=8, color=grey)
    plt.yticks(fontsize=8, color=grey)

    ax.tick_params(axis="x", color=grey)
    ax.tick_params(axis="y", color=grey)

    plt.legend(fontsize=6)
    plt.title(f'Playtime and price graph', fontsize=10, color=grey)
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

    graph_btn.destroy()

    canvas = FigureCanvasTkAgg(fig, master=store)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(column=0, row=2, padx=10, pady=10)

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
        username_friend, status_friend = str(selected_item).split(' - ')
        for i in range(0, len(friend_info_list)):
            if friend_info_list[i]['personaname'] == username_friend:
                clickedfriend_dict = friend_info_list[i]
                break

        steamid = clickedfriend_dict["friendsteamid"]
        countrycode = clickedfriend_dict['countrycode']
        friend_lvl = GetSteamLevel(steamid)

        root_friend = Tk()

        root_friend.title("Friend")
        root_friend.configure(bg=darker_blue)

        friendnamelbl = Label(root_friend, text=f"{username_friend}", fg=light_blue, bg=darker_blue, font=('', 10, "bold"))
        friendnamelbl.grid(row=0, column=0)

        friendcountrylbl = Label(root_friend, text=f"{countrycode}", fg=light_blue, bg=darker_blue, font=('', 10, "bold"))
        friendcountrylbl.grid(row=1, column=0)

        TI_button = Button(root_friend, text="Refresh status on lcd", command=lambda: serial_communication(steamid))
        TI_button.grid(row=1, column=1)

        friendlevellbl = Label(root_friend, text=f"level {friend_lvl}", fg=light_blue, bg=darker_blue, font=('', 10, "bold"))
        friendlevellbl.grid(row=0, column=1)

        friend_recent_games_list = []
        response = requests.get(
            f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={steam_api_key}&steamid={steamid}&count=10")
        data = response.json()
        if 'games' in data['response']:
            listbox_recentgames_friend = Listbox(root_friend, selectmode=SINGLE, height=15, width=50, fg=grey, bg=dark_blue, font=('', 10, "bold"))
            for game in data['response']['games']:
                friend_recent_games_list.append(game['name'])
            for game in friend_recent_games_list:
                listbox_recentgames_friend.insert(END, f"{game}")
            listbox_recentgames_friend.grid(row=2, column=0, columnspan=2)
        else:
            placeholderlbl = Label(bg=dark_blue, height=15, width=50, text="No recently played games", fg=light_blue, font=('', 10, "bold"))
            placeholderlbl.grid(row=2, column=0, columnspan=2)

        root_friend.mainloop()

def on_click_refresh(steamid):
    refresh_friendlist.config(text="Loading...")
    update_friendlist(steamid)

def update_friendlist(steamid):
    global friend_info_list
    refresh_friendlist.config(text="Refresh")
    listbox_friends.delete(0, END)
    friend_info_list = get_friend_info(steamid)
    sorted_friendlist = sort_list_with_dicts_by_onlinstatus(friend_info_list, button_state)
    for friend in sorted_friendlist:
        personaname = friend['personaname']
        onlinestatus = friend['onlinestatus']
        listbox_friends.insert(END, f"{personaname} - {onlinestatus}")

def main_gui(steamid, personaname):
    global listbox_friends, btn_asc_desc, button_state, refresh_friendlist, friend_info_list
    button_state = 0
    root2 = Tk()

    root2.geometry("800x600")
    root2.title("Main screen")
    root2.configure(bg=dark_blue)

    lbl = Label(master=root2, text=f"Welcome {personaname}", anchor='center', bg=dark_blue, fg=grey, font=('', 10, "bold"))
    lbl.grid(column=1, row=0)

    lbl2 = Label(master=root2, text=f"friendlist")
    lbl2.grid(column=0, columnspan=2, row=1, sticky="NESW")

    btn_asc_desc = Button(master=root2, text="Ascending", command=asc_desc)
    btn_asc_desc.grid(column=0, row=2, sticky="NESW")

    btn_sort_name = Button(master=root2, text="Sort by name", command=sort_gui_friendlist_by_name)
    btn_sort_name.grid(column=1, row=2, sticky="NESW")

    btn_sort_name = Button(master=root2, text="Sort by status", command=sort_gui_friendlist_by_status)
    btn_sort_name.grid(column=2, row=2, sticky="NESW")

    refresh_friendlist = Button(master=root2, text="Load Friendlist", command=lambda: on_click_refresh(steamid))
    refresh_friendlist.grid(column=2, row=1, stick="NESW")

    friend_info_list = []
    listbox_friends = Listbox(master=root2, selectmode=SINGLE, height=30, width=65, bg=darker_blue, fg=grey, font=('', 10, "bold"))
    listbox_friends.grid(column=0, columnspan=3, row=3)

    listbox_friends.bind("<Double-Button-1>", friend_gui)

    lbl_friendsareplaying = Label(master=root2, text="Friends are playing:", bg=dark_blue, fg=grey, font=('', 10, "bold"))
    lbl_friendsareplaying.grid(column=3, row=1)

    listbox_friend_games = Listbox(master=root2, selectmode=SINGLE, height=5, width=45, bg=darker_blue, fg=grey, font=('', 10, "bold"))
    recent_games_count = get_friends_recent_games(steamid)
    recent_games_sorted = list(sort_dict_on_values(recent_games_count).keys())[:5]
    for game in recent_games_sorted:
        listbox_friend_games.insert(END, game)
    listbox_friend_games.grid(column=3, row=3, sticky="N", padx=5)

    open_store = Button(master=root2, text="Open Store", command=store_gui)
    open_store.grid(column=0, row=0, sticky="W")

    root1.destroy()

    root2.mainloop()

def create_gamelist():
    with open('steam.json', 'r') as file:
        data = json.load(file)
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
        game_name_lbl = Label(master=games_frame, text=f"{game[0]}", fg=grey, bg=dark_blue)
        game_name_lbl.grid(column=0, row=i, pady=3, sticky='W')
    for i, game in enumerate(all_games[start:end]):
        if game[2] == 0.0:
            game_name_lbl = Label(master=games_frame, text=f"Free to play", fg=grey, bg=dark_blue)
        else:
            game_name_lbl = Label(master=games_frame, text=f"Price: {game[2]}$", fg=grey, bg=dark_blue)
        game_name_lbl.grid(column=1, row=i, pady=3, padx=30, sticky='W')

    for i, game in enumerate(all_games[start:end]):
        genres = game[5].split(";")
        genre_string = "Genre: "
        for j, genre in enumerate(genres):
            if j == 0:
                genre_string += genre
            else:
                genre_string += f", {genre}"
        game_name_lbl = Label(master=games_frame, text=genre_string, fg=grey, bg=dark_blue)
        game_name_lbl.grid(column=2, row=i, pady=3, sticky='W')

def next_page():
    global start, end
    start += 20
    end += 20
    update_labels(games_frame, start, end)
    update_page_label()

def previous_page():
    global start, end
    if start >= 20:
        start -= 20
        end -= 20
        update_labels(games_frame, start, end)
        update_page_label()

def update_page_label():
    page_label.config(text=f"Page {start // 20 + 1}")

def search_game(event):
    target_string = search_entry.get()
    if target_string == "":
        update_labels(games_frame, start, end)
    else:
        results = binary_search_substring(quicksort_lst_with_tuples(create_gamelist()), target_string)
        for label in games_frame.winfo_children():
            label.destroy()
        if results == []:
            game_name_lbl = Label(master=games_frame, text="No results found...")
            game_name_lbl.grid(column=0, row=0, pady=3, sticky='W')
        else:
            for i, game in enumerate(results[:20]):
                game_name_lbl = Label(master=games_frame, text=f"{game[0]}")
                game_name_lbl.grid(column=0, row=i, pady=3, sticky='W')
            for i, game in enumerate(results[:20]):
                if game[2] == 0.0:
                    game_name_lbl = Label(master=games_frame, text=f"Free to play")
                else:
                    game_name_lbl = Label(master=games_frame, text=f"Price: {game[2]}$")
                game_name_lbl.grid(column=1, row=i, pady=3, padx=30, sticky='W')

            for i, game in enumerate(results[:20]):
                genres = game[5].split(";")
                genre_string = "Genre: "
                for j, genre in enumerate(genres):
                    if j == 0:
                        genre_string += genre
                    else:
                        genre_string += f", {genre}"
                game_name_lbl = Label(master=games_frame, text=genre_string)
                game_name_lbl.grid(column=2, row=i, pady=3, sticky='W')

def prijs_statistieken():
    all_prices = []
    with open('steam.json', 'r') as file:
        data = json.load(file)
    for i, game in enumerate(data):
        price = data[i]['price']
        all_prices.append(price)

    data = {'Price': all_prices}
    df = pd.DataFrame(data)

    gemiddelde_prijs = df['Price'].mean()
    mediaan_prijs = df['Price'].median()
    standaarddeviatie_prijs = df['Price'].std()

    return gemiddelde_prijs.round(2), mediaan_prijs.round(2), standaarddeviatie_prijs.round(2)

def genre_frequentie():
    all_genres = []
    all_genres_count = {}
    with open('steam.json', 'r') as file:
        data = json.load(file)
    for i, game in enumerate(data):
        game_genres = data[i]['genres']
        game_genre = game_genres.split(";")
        for genre in game_genre:
            all_genres.append(genre)

    for genre in all_genres:
        if genre in all_genres_count:
            all_genres_count[genre] += 1
        else:
            all_genres_count[genre] = 1
    sorted_genre_count = sort_dict_on_values(all_genres_count)
    return sorted_genre_count

def store_gui():
    global start, end, games_frame, page_label, search_entry, graph_btn, store
    start = 0
    end = 20

    store = Tk()
    store.title("Steam Store")
    store.configure(bg=darker_blue)

    gemiddelde_prijs, mediaan_prijs, standaarddeviatie_prijs = prijs_statistieken()
    prijs_statistiek = Label(master=store, text=f"Statistieken over prijs:\n\nGemiddelde prijs: ${gemiddelde_prijs}\nMediaan prijs: ${mediaan_prijs}\nStandaarddeviatie prijs: ${standaarddeviatie_prijs}", fg=grey, bg=darker_blue)
    prijs_statistiek.grid(column=0, row=3, padx=20, sticky="N")

    sorted_genre_count = genre_frequentie()
    genre_string = "Genres: \n\n"
    count_string = "Count: \n\n"
    for genre, count in sorted_genre_count.items():
        genre_string += f"{genre}: \n"
        count_string += f"{count} \n"

    genre_lbl = Label(master=store, text=f"{genre_string}", fg=grey, bg=darker_blue)
    genre_lbl.grid(column=4, row=2, padx=20, rowspan=2, sticky="N")

    genre_count_lbl = Label(master=store, text=f"{count_string}", fg=grey, bg=darker_blue)
    genre_count_lbl.grid(column=5, row=2, padx=20, rowspan=2, sticky="N")

    graph_btn = Button(master=store, text=f"Plot graph", command=linear_regression)
    graph_btn.grid(column=0, row=2, padx=20, sticky="N")

    store_lbl = Label(master=store, text="Steam Store", fg=grey, bg=darker_blue)
    store_lbl.grid(column=1, columnspan=3, row=0)

    search_frame = Frame(master=store, bg=darker_blue)
    search_frame.grid(column=1, columnspan=3, row=1)

    search_lbl = Label(master=search_frame, text="Search: ", fg=grey, bg=darker_blue)
    search_lbl.grid(column=0, row=0, sticky="W")

    search_entry = Entry(master=search_frame, width=50, bg=grey)
    search_entry.grid(column=1, row=0, columnspan=2, sticky="W")
    search_entry.bind("<Return>", search_game)

    games_frame = Frame(master=store, bg=dark_blue)
    games_frame.grid(column=1, columnspan=3, row=2, rowspan=2)

    previous_button = Button(master=store, text="<", font=("", 15), command=previous_page)
    previous_button.grid(column=1, row=4, pady=5, sticky="NESW")

    page_label = Label(master=store, text="Page 1", fg=grey, bg=darker_blue)
    page_label.grid(column=2, row=4)

    next_button = Button(master=store, text=">", font=("", 15), command=next_page)
    next_button.grid(column=3, row=4, pady=5, sticky="NESW")

    update_labels(games_frame, start, end)

    store.mainloop()

def on_click(event):
    steamid = steamid_input.get()

    root1.title("Loading...")
    lbl_login.config(text="Loading...", font=("", 20))
    steamid_input.destroy()
    continue_lbl.destroy()
    root1.update()

    try:
        personaname = get_personaname(steamid)
        main_gui(steamid, personaname)
    except:
        root1.title("Error")
        lbl_login.config(text="Error\nSteam ID does not exist", font=("", 20))
        return_btn = Button(master=root1, text="Return to login", command=return_to_login)
        return_btn.pack()

def return_to_login():
    root1.destroy()
    login()

def login():
    global steamid_input, root1, lbl_login, continue_lbl
    root1 = Tk()
    root1.geometry("800x400")
    root1.title("Login")
    root1.configure(bg=darker_blue)

    lbl_login = Label(master=root1, text="What is your steam ID?", fg=light_blue, bg=darker_blue)
    lbl_login.pack(pady=20)

    steamid_input = Entry(master=root1, width=25)
    steamid_input.pack()
    steamid_input.bind("<Return>", on_click)

    continue_lbl = Label(master=root1, text="Press 'Enter' to continue",fg=light_blue, bg=darker_blue)
    continue_lbl.pack(pady=20)

    root1.mainloop()

login()
