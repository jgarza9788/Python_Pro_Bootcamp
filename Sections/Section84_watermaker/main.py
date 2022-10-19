
import os
import time
import sys
import math 

from tkinter import *
from PIL import Image, ImageTk

import tkinter.filedialog as fd


class App(Tk):
    def __init__(self):
        super().__init__()

        # mostly for UI purposes
        self.DIR = os.path.dirname(os.path.realpath(__file__))
        self.FONT_NAME = 'Helvetica'
        self.FONT_SIZE = 10
        self.WHITE ='#ffffff'
        self.BACKGROUND_COLOR = '#66d9ef'

        # set up window
        self.title("Water Mark 💧")
        self.config(
            padx=20,
            pady=20,
            bg=self.BACKGROUND_COLOR,
            )
        self.grid_columnconfigure(0, weight=1)
        self.geometry("600x250")
        self.resizable(0, 0)

        # some CONSTANTS and Variables

        # path for the watermark image
        self.watermark = os.path.join(self.DIR,'default_water_mark.png')

        self.sv_watermark = StringVar()
        self.sv_watermark.set(self.watermark.split('\\')[-1])

        # path for the photo to add the watermark to
        self.photo = ''

        self.sv_photo = StringVar()
        self.sv_photo.set('')

        # error (if any)
        self.sv_error = StringVar()
        self.sv_error.set('')

        # alpha of the watermark
        self.dv_alpha = DoubleVar()
        self.dv_alpha.set(127) #default value for alpha

        #modes for the watermark
        self.modes = ['center', 'topleft', 'repeat']
        self.sv_mode = StringVar()
        self.sv_mode.set(self.modes[0])

        #set up the window layout
        label = Label(
            text='WaterMark Maker 💧',
            font=(self.FONT_NAME,24,"bold"),
            bg=self.BACKGROUND_COLOR
            )
        label.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)

        label = Label(
            text='Water Mark Image',
            font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
            bg=self.BACKGROUND_COLOR,
            width=25
            )
        label.grid(row=1,column=0,sticky=W+E+N+S)

        label = Label(
                textvariable=self.sv_watermark,
                font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
                bg=self.WHITE,
                width=25
                )
        label.grid(row=1,column=1,sticky=W+E+N+S)

        btn = Button(text='Pick New File', 
            command=self.use_filedialog_watermark)
        btn.grid(row=1,column=2,sticky=W+E+N+S)

        label = Label(
            text='Photo',
            font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
            bg=self.BACKGROUND_COLOR,
            width=25
            )
        label.grid(row=2,column=0,sticky=W+E+N+S)

        label = Label(
            textvariable=self.sv_photo,
            font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
            bg=self.WHITE,
            width=25
            )
        label.grid(row=2,column=1,sticky=W+E+N+S)

        btn = Button(text='Pick New File', 
            command=self.use_filedialog_photo)
        btn.grid(row=2,column=2,sticky=W+E+N+S)

        label = Label(
            text='Alpha (0-255):',
            font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
            bg=self.BACKGROUND_COLOR,
            width=25
            )
        label.grid(row=3,column=0,sticky=W+E+N+S)

        slider = Scale(
                from_=0, 
                to=255, 
                # tickinterval=1,
                orient=HORIZONTAL, 
                variable=self.dv_alpha,
                command=self.use_slider_alpha
                )
        slider.grid(row=3,column=1,sticky=W+E+N+S)

        label = Label(
            text='Mode:',
            font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
            bg=self.BACKGROUND_COLOR,
            width=25
            )
        label.grid(row=4,column=0,sticky=W+E+N+S)

        options = OptionMenu(
            self,
            self.sv_mode,
            *self.modes,
            command=self.mode_changed
            )
        options.grid(row=4,column=1,sticky=W+E+N+S)

        btn = Button(text='Apply/Create', width = 50,
            command=self.apply)
        btn.grid(row=5,column=0,columnspan=3,sticky=W+E+N+S)

        label = Label(
            textvariable=self.sv_error,
            font=(self.FONT_NAME,self.FONT_SIZE,"normal"),
            bg=self.BACKGROUND_COLOR,
            fg='#ff0000',
            width=50
            )
        label.grid(row=6,column=0,columnspan=3,sticky=W+E+N+S)

    def use_filedialog_watermark(self):
        self.watermark = fd.askopenfilename() 
        self.sv_watermark.set(self.watermark.split('/')[-1])
        print(self.watermark)

    def use_filedialog_photo(self):
        self.photo = fd.askopenfilename() 
        self.sv_photo.set(self.photo.split('/')[-1])
        print(self.photo)

    def use_slider_alpha(self,event):
        self.alpha = self.dv_alpha.get()
        print(self.alpha)

    def mode_changed(self,choice):
        print(self.sv_mode.get())

    def apply(self):

        print(self.watermark)
        print(self.photo)
        
        if os.path.exists(self.photo) == False:
            self.sv_error.set('photo doesn\'t exist')
            return None
        
        if os.path.exists(self.watermark) == False:
            self.sv_error.set('watermark doesn\'t exist')
            return None

        self.sv_error.set('')
        
        img_photo = Image.open(self.photo)
        img_watermark = Image.open(self.watermark)

        #allpy transparency
        img_watermark.putalpha(int(self.dv_alpha.get()))

        # process alpha for water mark
        rgba = img_watermark.convert('RGBA')
        
        newImage = []
        for item in rgba.getdata():
            # print(item[3])
            if item[:3] == (0, 0, 0):
                newImage.append((0, 0, 0, 0))
            else:
                newImage.append(item)
        rgba.putdata(newImage)

        img_watermark = rgba

        wm_w, wm_h = img_watermark.size
        p_w, p_h = img_photo.size

        offset = (0,0)
        if self.sv_mode.get() == 'center':

            offset = ((p_w - wm_w) // 2, (p_h - wm_h) // 2)

            img_photo.paste(img_watermark, offset, mask = img_watermark)

        elif self.sv_mode.get() == 'topleft':
            offset = (0,0)
            img_photo.paste(img_watermark, offset, mask = img_watermark)

        elif self.sv_mode.get() == 'repeat':

            xy = [0,0]
            # x_repeat = math.trunc(bg_w / img_w)
            # y_repeat = math.trunc(bg_h / img_h)

            x_repeat = int(p_w / wm_w) + 1
            y_repeat = int(p_h / wm_h) + 1

            x_repeat = max([x_repeat,1])
            y_repeat = max([y_repeat,1])

            for x in range(x_repeat):
                for y in range(y_repeat):
                    offset = (wm_w*x ,wm_h*y)
                    img_photo.paste(img_watermark, offset, mask = img_watermark)

        img_photo.show()

if __name__ == '__main__':
    app = App()
    app.mainloop()

