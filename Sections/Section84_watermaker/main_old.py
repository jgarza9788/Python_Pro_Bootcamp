
import os
import time
import sys
import math 

from tkinter import *
from PIL import Image, ImageTk

import tkinter.filedialog as fd
# tkinter.filedialog.asksaveasfilename()
# tkinter.filedialog.asksaveasfile()
# tkinter.filedialog.askopenfilename()
# tkinter.filedialog.askopenfile()
# tkinter.filedialog.askdirectory()
# tkinter.filedialog.askopenfilenames()
# tkinter.filedialog.askopenfiles()

# ---------------------------- CONSTANTS ------------------------------- #

DIR = os.path.dirname(os.path.realpath(__file__))
FONT_NAME = 'Helvetica'
FONT_SIZE = 10
WHITE ='#ffffff'
BACKGROUND_COLOR = '#66d9ef'

watermark = os.path.join(DIR,'default_water_mark.png')
photo = ''
alpha = 255 #default alpha value
error_label = ''


def main():
    global photo
    global watermark
    global alpha


    # set up window 
    window = Tk()
    window.title("Water Mark 💧")
    window.config(
        padx=20,
        pady=20,
        bg=BACKGROUND_COLOR,
        )


    window.grid_columnconfigure(0, weight=1)

    window.geometry("600x250")
    window.resizable(0, 0)

    svwm = StringVar()
    svwm.set(watermark.split('\\')[-1])

    svp = StringVar()
    svp.set('')

    sv_error = StringVar()
    sv_error.set('')

    
    tk_alpha = DoubleVar()
    tk_alpha.set(alpha)

    sv_mode = StringVar()
    sv_mode.set('center')

    modes = ['center','topleft', 'repeat']


    def use_filedialog_wm():
        global watermark
        watermark = fd.askopenfilename() 
        svwm.set(watermark.split('/')[-1])
        print(watermark)

    def use_filedialog_p():
        global photo
        photo = fd.askopenfilename() 
        svp.set(photo.split('/')[-1])
        print(photo)

    def change_slider(event):
        global alpha
        alpha = tk_alpha.get()
        print(alpha)

    def mode_changed(chice):
        print(sv_mode.get())

    def go():
        global photo
        global watermark
        global alpha
        global modes

        print(photo)
        print(watermark)

        if os.path.exists(photo) == False:
            sv_error.set('photo doesn\'t exist')
            return None

        if os.path.exists(watermark) == False:
            sv_error.set('watermark doesn\'t exist')
            return None

        sv_error.set('')

        imgp = Image.open(photo)
        imgwm = Image.open(watermark)
        imgwm.putalpha(int(alpha))

        rgba = imgwm.convert('RGBA')
        
        newImage = []
        for item in rgba.getdata():
            # print(item[3])
            if item[:3] == (0, 0, 0):
                newImage.append((0, 0, 0, 0))
            else:
                newImage.append(item)
        rgba.putdata(newImage)

        imgwm = rgba

        img_w, img_h = imgwm.size
        bg_w, bg_h = imgp.size

        offset = (0,0)
        if sv_mode.get() == 'center':

            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            imgp.paste(imgwm, offset, mask = imgwm)

        elif sv_mode.get() == 'topleft':
            offset = (0,0)
            imgp.paste(imgwm, offset, mask = imgwm)

        elif sv_mode.get() == 'repeat':

            xy = [0,0]
            # x_repeat = math.trunc(bg_w / img_w)
            # y_repeat = math.trunc(bg_h / img_h)

            x_repeat = int(bg_w / img_w) + 1
            y_repeat = int(bg_h / img_h) + 1

            x_repeat = max([x_repeat,1])
            y_repeat = max([y_repeat,1])

            for x in range(x_repeat):
                for y in range(y_repeat):
                    offset = (img_w*x ,img_h*y)
                    imgp.paste(imgwm, offset, mask = imgwm)


        # No transparency mask specified, 
        # simulating an raster overlay

        imgp.paste(imgwm, offset, mask = imgwm)

        imgp.show()

    title = Label(
        text='WaterMark Maker 💧',
        font=(FONT_NAME,24,"bold"),
        bg=BACKGROUND_COLOR
        )
    title.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)

    wmi_ll = Label(
        text='Water Mark Image',
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=BACKGROUND_COLOR,
        width=25
        )
    wmi_ll.grid(row=1,column=0,sticky=W+E+N+S)

    wmi_l = Label(
        textvariable=svwm,
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=WHITE,
        width=25
        )
    wmi_l.grid(row=1,column=1,sticky=W+E+N+S)

    wmi_b = Button(text='Pick New File', 
        command=use_filedialog_wm)
    wmi_b.grid(row=1,column=2,sticky=W+E+N+S)

    pwm_ll = Label(
        text='Photo',
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=BACKGROUND_COLOR,
        width=25
        )
    pwm_ll.grid(row=2,column=0,sticky=W+E+N+S)

    pwm_l = Label(
        textvariable=svp,
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=WHITE,
        width=25
        )
    pwm_l.grid(row=2,column=1,sticky=W+E+N+S)

    pwm_b = Button(text='Pick New File', 
        command=use_filedialog_p)
    pwm_b.grid(row=2,column=2,sticky=W+E+N+S)

    alpha_l = Label(
        text='Alpha (0-255):',
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=BACKGROUND_COLOR,
        width=25
        )
    alpha_l.grid(row=3,column=0,sticky=W+E+N+S)

    alpha_sli = Scale(
            window, 
            from_=60, 
            to=255, 
            # tickinterval=1,
            orient=HORIZONTAL, 
            variable=tk_alpha,
            command=change_slider
            )
    alpha_sli.grid(row=3,column=1,sticky=W+E+N+S)

    mode_l = Label(
        text='Mode:',
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=BACKGROUND_COLOR,
        width=25
        )
    mode_l.grid(row=4,column=0,sticky=W+E+N+S)

    mode_om = OptionMenu(
        window,
        sv_mode,
        *modes,
        command=mode_changed
        )
    mode_om.grid(row=4,column=1,sticky=W+E+N+S)


    b = Button(text='<< go >>', width = 50,
        command=go)
    b.grid(row=5,column=0,columnspan=3,sticky=W+E+N+S)

    error_l = Label(
        textvariable=sv_error,
        font=(FONT_NAME,FONT_SIZE,"normal"),
        bg=BACKGROUND_COLOR,
        fg='#ff0000',
        width=50
        )
    error_l.grid(row=6,column=0,columnspan=3,sticky=W+E+N+S)




    window.mainloop()



if __name__ == '__main__':
    main()

# todo: reformat code to match this style
# https://code-paper.com/python/examples-tkinter-boilerplate