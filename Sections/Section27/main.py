from tkinter import *

window = Tk()
window.title("miles to kilometers")
# window.minsize(width=500,height=300)


result = 0

def calc():
    try:
        result = float(input_field.get())*1.6
        result_label.config(text='{0:.2f}'.format(result))
    except:
        result_label.config(text='error')

font = ("Arial",12,"normal")

prompt_label = Label(text='Is equal to',font=font)
prompt_label.grid(row=1,column=0)

result_label = Label(text='{0}'.format(result),font=font)
result_label.grid(row=1,column=1)

input_field = Entry()
input_field.grid(row=0,column=1)

mile_label = Label(text='Miles',font=font)
mile_label.grid(row=0,column=2)

km_label = Label(text='Km',font=font)
km_label.grid(row=1,column=2)

button = Button(text="calculate",command=calc)
button.grid(row=2,column=1)


# for i in range(4):
#     window.grid_columnconfigure(i, minsize=50)
#     window.grid_rowconfigure(i, minsize=50)

window.mainloop()