from tkinter import *
from tkinter import Label
import time
import sys
app=Tk()
def get_time():
    timeVar=time.strftime("%I : %M : %S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)
Label(app,font=("Times",160),text="Digital Clock",fg="white",bg="#4682B4")
clock=Label(app,font=("Times",160),text="Digital Clock",fg="white",bg="#4682B4")
clock.pack()
get_time()
app.mainloop()
