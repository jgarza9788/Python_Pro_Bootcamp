# this is just so i can see the fonts
from tkinter import Tk, font

root = Tk()
font_tuple = font.families()
root.destroy()
for font in font_tuple:
    print(font)