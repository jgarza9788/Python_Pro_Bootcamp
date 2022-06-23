import os
import sys
import json

import password_generator as pg
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- CONSTANTS ------------------------------- #

DIR = os.path.dirname(os.path.realpath(__file__))
FONT_NAME = 'Helvetica'
FONT_SIZE = 10
WHITE ='#ffffff'
DATA = []
FILE_NAME = os.path.join(DIR,'data.json')

# ---------------------------- JSON ------------------------------- #

def get_data(file):
    try:
        with open(file,'r',encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def set_data(data,file):
    # self.sort()
    with open(file,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4)


DATA = get_data(FILE_NAME)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_field.delete(0,END)
    new_pw = str(pg.get_password(4,4,4))
    password_field.insert(0,new_pw)
    pyperclip.copy(new_pw)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():

    d = DATA[website_field.get()]
    em_user_field.delete(0,END)
    password_field.delete(0,END)
    em_user_field.insert(0,d['email'])
    password_field.insert(0,d['password'])



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_field.get()
    email = em_user_field.get()
    password = password_field.get()

    # answer = messagebox.askyesno(title=website,message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs this ok to save?")
    # if answer:

    if len(website) > 0 and len(email) > 0 and len(password) > 0 :

            # with open(os.path.join(DIR,"data.txt"),"a",encoding='utf-8') as data_file:
            #     data_file.write(f"{website} | {email} | {password}\n")

        DATA[website] = {'email':email,'password':password}
        set_data(DATA,FILE_NAME)

        website_field.delete(0,END)
        # em_user_field.delete(0,END)
        password_field.delete(0,END)

        messagebox.showinfo(title='password added',message='the password was added')
    else:
        messagebox.showerror(title='no password was saved',message='the password was not added')

        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("myPass 🔒")
window.config(padx=30,pady=30,bg=WHITE)

canvas = Canvas(width=200,height=200,bg=WHITE,highlightthickness=0)
logo_img = PhotoImage(file=os.path.join(DIR,'logo.png'))
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(
    text='Website',
    font=(FONT_NAME,FONT_SIZE,"normal"),
    bg=WHITE
    )
website_label.grid(row=1,column=0)

website_field = Entry(width=30)
website_field.grid(row=1,column=1,columnspan=2,sticky='W') 
website_field.focus()

search_button = Button(
            text="search",
            font=(FONT_NAME,FONT_SIZE,"normal"),
            bg=WHITE,
            width=15
            ,command=search
            )
search_button.grid(row=1,column=2,sticky='W') 

em_user_label = Label(
    text='email/UserName',
    font=(FONT_NAME,FONT_SIZE,"normal"),
    bg=WHITE
    )
em_user_label.grid(row=2,column=0)

em_user_field = Entry(width=55)
em_user_field.grid(row=2,column=1,columnspan=2,sticky='W') 
em_user_field.insert(0,'JGarza9788@gmail.com')

password_label = Label(
    text='Password',
    font=(FONT_NAME,FONT_SIZE,"normal"),
    bg=WHITE
    )
password_label.grid(row=3,column=0)

password_field = Entry(width=30)
password_field.grid(row=3,column=1,sticky='W') 

generate_button = Button(
            text="Generate Password",
            font=(FONT_NAME,FONT_SIZE,"normal"),
            bg=WHITE,
            width=15
            ,command=generate_password
            )
generate_button.grid(row=3,column=2,sticky='W') 

add_button = Button(
            text="Update",
            font=(FONT_NAME,FONT_SIZE,"normal"),
            bg=WHITE,
            width=40
            ,command=save
            )
add_button.grid(row=4,column=1,columnspan=2,sticky='W') 


window.mainloop()