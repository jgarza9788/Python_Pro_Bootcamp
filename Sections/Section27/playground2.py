# import tkinter
from tkinter import *
# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/contents.htm

window = Tk()
window.title("GUI Program")
window.minsize(width=500,height=300)

my_label = Label(text='I am a label',font=("Arial",24,"bold"))
my_label.pack(
    #side="left",
    #expand=False
    )
    
def fuct_button():
    print('hello')
    my_label['text']='hello'
    my_label.config(text=input_field.get())
    # my_label.config(text='yo')

button = Button(text="say hello",command=fuct_button)
button.pack(
    #side="left",
    #expand=False
    )

# def fuct_entry():
#     my_label.config(text=input_field.get())

input_field = Entry()
input_field.pack()
# print(input_field.get())

window.mainloop()