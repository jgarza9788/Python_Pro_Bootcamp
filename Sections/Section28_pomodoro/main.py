import os
import sys
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

DIR = os.path.dirname(os.path.realpath(__file__))
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# TIMER_STATUS = 0

STATE = 0
STATES = [
    {'name': 'not started','seconds': 0, 'color':YELLOW, 'checks':'🔲🔲🔲'},
    {'name': 'work1','seconds': (25*60), 'color': GREEN ,'checks':'🔲🔲🔲'},
    {'name': 'break1','seconds': (5*60), 'color': PINK ,'checks':'✅🔲🔲'},
    {'name': 'work2','seconds': (25*60), 'color': GREEN ,'checks':'✅🔲🔲'},
    {'name': 'break2','seconds': (5*60), 'color': PINK ,'checks':'✅✅🔲'},
    {'name': 'work3','seconds': (25*60), 'color': GREEN ,'checks':'✅✅🔲'},
    {'name': 'break3','seconds': (20*60), 'color': RED ,'checks':'✅✅✅'},
]

STATES = [
    {'name': 'not started','seconds': 0, 'color':YELLOW, 'checks':'🔲🔲🔲'},
    {'name': 'work1','seconds': (2.5), 'color': GREEN ,'checks':'🔲🔲🔲'},
    {'name': 'break1','seconds': (0.5), 'color': PINK ,'checks':'✅🔲🔲'},
    {'name': 'work2','seconds': (2.5), 'color': GREEN ,'checks':'✅🔲🔲'},
    {'name': 'break2','seconds': (0.5), 'color': PINK ,'checks':'✅✅🔲'},
    {'name': 'work3','seconds': (2.5), 'color': GREEN ,'checks':'✅✅🔲'},
    {'name': 'break3','seconds': (2.0), 'color': RED ,'checks':'✅✅✅'},
]


def increment_state():
    global STATE, STATES
    nState = STATE+1
    STATE = (STATE+1) % len(STATES)
    if nState == 7:
        return False
    else:
        return True
    

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global STATE, STATES
    STATE = 0
    title.config(text=STATES[STATE]['name'],fg= STATES[STATE]['color'])
    count_down(STATES[STATE]['seconds'])
    checks.config(text=STATES[STATE]['checks'])

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    # global TIMER_STATUS
    # if TIMER_STATUS == 1:
    #     return None
    # TIMER_STATUS = 1

    global STATE, STATES
    do_next_state = increment_state()

    if do_next_state:
        title.config(text=STATES[STATE]['name'],fg= STATES[STATE]['color'])
        count_down(STATES[STATE]['seconds'])
        checks.config(text=STATES[STATE]['checks'])

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global STATE, STATES
    MMSS = time.strftime('%M:%S', time.gmtime(count))
    canvas.itemconfig(timer_text,text=MMSS)
    print(count)
    if count > 0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro 🍅")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file=os.path.join(DIR,'tomato.png'))
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

title = Label(
    text='Timer',
    font=(FONT_NAME,50,"bold"),
    bg=YELLOW,fg=GREEN
    )
title.grid(row=0,column=1)

checks = Label(
    text='🔲🔲🔲',
    font=(FONT_NAME,20,"bold"),
    bg=YELLOW,fg=GREEN
    )
checks.grid(row=3,column=1)

# state_label = Label(
#     text=STATES[STATE]['name'],
#     font=(FONT_NAME,16,"normal"),
#     bg=YELLOW,fg=RED
#     )
# state_label.grid(row=4,column=1)

start_button = Button(
    text="Start",
    font=(FONT_NAME,18,"bold"),
    bg=YELLOW,fg="BLACK"
    ,command=start_timer
    )
start_button.grid(row=3,column=0)

reset_button = Button(
    text="Reset",
    font=(FONT_NAME,18,"bold"),
    bg=YELLOW,fg="BLACK",
    command=reset_timer
    )
reset_button.grid(row=3,column=2)

window.mainloop()