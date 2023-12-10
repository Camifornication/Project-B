import json
from tkinter import *
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

sorted()