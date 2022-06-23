

import os
import sys
# import json

import pandas as pd

import time
import random

from tkinter import *
# from tkinter import messagebox
from PIL import Image, ImageTk


# ---------------------------- CONSTANTS ------------------------------- #

DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = os.path.join(DIR,'images')

CARD_BACK = os.path.join(IMG_DIR,'card_back.png')
CARD_FRONT = os.path.join(IMG_DIR,'card_front.png')
RIGHT = os.path.join(IMG_DIR,'right.png')
WRONG = os.path.join(IMG_DIR,'wrong.png')

FONT_NAME = 'Helvetica'
LANG_FONT_SIZE = 48
WORD_FONT_SIZE = 60

WHITE ='#ffffff'
BACKGROUND_COLOR = '#B1DDC6'
DATA = []
FILE_NAME = os.path.join(DIR,'data','french_words.csv')
LANG = {-1:'French',1:'English'}
INT_LANG = -1
INT_RECORD = 0

# ---------------------------- JSON ------------------------------- #



DATA = pd.read_csv(FILE_NAME).to_dict(orient='records')
# print(DATA)

def next_word():
    global INT_LANG,INT_RECORD,DATA,INT_RECORD
    INT_RECORD = random.randint(0,len(DATA)-1)
    canvas.itemconfig(lang_text,text=[LANG[INT_LANG]])
    canvas.itemconfig(word_text,text=DATA[INT_RECORD][LANG[INT_LANG]])

def flip_card():
    global INT_LANG,INT_RECORD,DATA,INT_RECORD
    INT_LANG *= -1
    if INT_LANG == 1:
        canvas.itemconfig(front,state='hidden')
        canvas.itemconfig(back,state='normal')
    else:
        canvas.itemconfig(front,state='normal')
        canvas.itemconfig(back,state='hidden')
    canvas.itemconfig(lang_text,text=[LANG[INT_LANG]])
    canvas.itemconfig(word_text,text=DATA[INT_RECORD][LANG[INT_LANG]])


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards ⚡")
window.config(
    padx=30,
    pady=30,
    bg=BACKGROUND_COLOR,
    )
window.resizable(0, 0)

canvas = Canvas(width=800,height=626,bg=BACKGROUND_COLOR,highlightthickness=0)

back_img = Image.open(CARD_BACK)
b_tki = ImageTk.PhotoImage(back_img.rotate(0))
back = canvas.create_image(400,263,image=b_tki)

front_img = Image.open(CARD_FRONT)
f_tki = ImageTk.PhotoImage(front_img.rotate(0))
front = canvas.create_image(400,263,image=f_tki)


lang_text = canvas.create_text(400,150,text='french',font=(FONT_NAME,LANG_FONT_SIZE,'italic'))
word_text = canvas.create_text(400,263,text='word',font=(FONT_NAME,WORD_FONT_SIZE,'bold'))

canvas.grid(row=0,column=0,columnspan=2)
next_word()



right_img = PhotoImage(file=RIGHT)
wrong_img = PhotoImage(file=WRONG)

right_button = Button(
            image=right_img,
            highlightthickness=0,
            borderwidth=0
            ,command=next_word
            )
right_button.place(width=100,height=100,x=0,y=526)

wrong_button = Button(
            image=wrong_img,
            highlightthickness=0,
            borderwidth=0
            ,command=flip_card
            )
wrong_button.place(width=100,height=100,x=700,y=526)



window.mainloop()