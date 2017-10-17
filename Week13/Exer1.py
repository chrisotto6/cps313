# Chris Otto
# Week 13 - Program Exercise 1
# CPS313

# Name and Address

import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.top = tkinter.Frame(self.main)
        self.bottom = tkinter.Frame(self.main)
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.top, textvariable=self.value)
        self.info_button = tkinter.Button(self.bottom, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.bottom, text='Quit', command=self.main.destroy)
        self.info.pack()
        self.info_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top.pack()
        self.bottom.pack()
        tkinter.mainloop()

    def show(self):
        values = '\tChris Otto\n\t123 Test Way\n\tMilwaukee, WI 53211'
        self.value.set(values)

gu = GUI()