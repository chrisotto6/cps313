# Chris Otto
# Week 13 - Program Exercise 4
# CPS313

# Celsius to Fahrenheit

import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main)
        self.frame2 = tkinter.Frame(self.main)
        self.frame3 = tkinter.Frame(self.main)
        self.label1 = tkinter.Label(self.frame1, text='Enter Celsius Value:')
        self.entry1 = tkinter.Entry(self.frame1,width=10)
        self.label1.pack(side='left')
        self.entry1.pack(side='left')
        self.fahr = tkinter.StringVar()
        self.res = tkinter.Label(self.frame2, text='Fahrenheit Value:')
        self.result = tkinter.Label(self.frame2, textvariable=self.fahr)
        self.res.pack(side='left')
        self.result.pack(side='left')
        self.calc = tkinter.Button(self.frame3, text='Calculate Fahrenheit', command=self.calculate)
        self.quit = tkinter.Button(self.frame3, text = 'Quit', command=self.main.destroy)
        self.calc.pack(side='left')
        self.quit.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        tkinter.mainloop()

    def calculate(self):
        self.degree = float(self.entry1.get())
        self.thisanswer = float((1.8*(self.degree))+32)
        self.fahr.set(self.thisanswer)

g = GUI()