from tkinter import*
import sqlite3


def create():
    conn=sqlite3.connect("detail.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS record(name TEXT,address TEXT,contact TEXT,email TEXT,device TEXT)")
    conn.commit()
    conn.close()
    
create()

def save():

    conn=sqlite3.connect("detail.db")
    cur=conn.cursor()
    data=(name_entry.get(),address_entry.get(),contact_entry.get(),email_entry.get(),device_entry.get())
    cur.execute("INSERT INTO record(name,address,contact,email,device)VALUES(?,?,?,?,?)",data)
    conn.commit()
    conn.close()
    
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    contact_entry.delete(0,END)
    email_entry.delete(0,END)
    device_entry.delete(0,END)


app=Tk()
app.geometry("400x350")
app.title("AMRIT TV SERVICE")
title_label=Label(app,text="*****AMRIT TV REPAIR*****",font=("Times 18 bold underline"),fg="green")
title_label.place(x=20,y=5)
name_label=Label(app,text="Name",font="Times 13 bold")
name_label.place(x=50,y=100)
address_label=Label(app,text="Address",font="Times 13 bold")
address_label.place(x=50,y=130)
contact_label=Label(app,text="Contact",font="Times 13 bold")
contact_label.place(x=50,y=160)
email_label=Label(app,text="Email",font="Times 13 bold")
email_label.place(x=50,y=190)
device_label=Label(app,text="Device",font="Times 13 bold")
device_label.place(x=50,y=220)
author_label=Label(app,text="Create by:Amrit Chettri,20/01/2025",font="Times 8",fg="blue")
author_label.place(x=110,y=330)

name_entry=Entry(app)
name_entry.place(x=150,y=100)
address_entry=Entry(app)
address_entry.place(x=150,y=130)
contact_entry=Entry(app)
contact_entry.place(x=150,y=160)
email_entry=Entry(app)
email_entry.place(x=150,y=190)
device_entry=Entry(app)
device_entry.place(x=150,y=220)

save_button=Button(app,text="SAVE",font="Times 18 bold",bg="lightgreen",command=save)
save_button.place(x=160,y=270)



app.mainloop()
