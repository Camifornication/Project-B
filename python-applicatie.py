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

gui()