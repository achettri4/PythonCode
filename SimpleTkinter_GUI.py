from tkinter import*
from tkinter import ttk
import sqlite3

def connect():
    conn = sqlite3.connect("dewa.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS roshan(Customer TEXT, Address TEXT)")
    conn.commit()
    conn.close()

def save():
    conn=sqlite3.connect("dewa.db")
    cur = conn.cursor()
    data= (cstmr.get(),adrs.get())
    # insert data in db
    cur.execute("INSERT INTO roshan(Customer, Address) VALUES(?,?)", data)
    conn.commit()
    # After save data we can make entry field empty
    en1.delete(0,END)
    en2.delete(0,END)
    en1.focus()
    # insert data in treeview
    trv.insert('',END, text=str(cur.lastrowid), values=data)
    conn.close()


    connect()


def DisplayData():
    # open databse
    conn = sqlite3.connect('dewa.db')
    #select query
    cursor=conn.execute("SELECT rowid,* FROM roshan")
    fetch = cursor.fetchall()
    for row in fetch:
        trv.insert('',END,iid=row[0],values=row[1:])
    cursor.close()
    conn.close()

def remove_one():
    rowid = trv.selection()[0]
    trv.delete(rowid)

    conn = sqlite3.connect('dewa.db')
    c = conn.cursor()

    c.execute("DELETE from roshan WHERE rowid = ?",(rowid,))
    conn.commit()
    conn.close()





win=Tk()
win.title('DEMO')
win.iconbitmap(r'C:\Users\amrit\Desktop\Apps\A2.ico')
win.geometry('800x500')
win.resizable('true','true')
lfrm=LabelFrame(win,text='Form',font=('Times',14),bg='skyblue',bd=4,labelanchor='nw')
lfrm.pack(fill='both',expand='yes')
lfrm1=LabelFrame(win,text='RecordList',font=('Times',14),bg='lightgreen',bd=4,labelanchor='n')
lfrm1.pack(fill='both',expand='yes')


cstmr=StringVar()
adrs=StringVar()
clbl=Label(lfrm,text='Customer',font=('Helvetica',14),bg='skyblue')
clbl.place(x=20,y=10)
albl=Label(lfrm,text='Address',font=('Helvetica',14),bg='skyblue')
albl.place(x=24,y=50)

en1=Entry(lfrm,textvariable=cstmr,font=('Times',14),justify='center')
en1.place(x=150,y=10)

en2=Entry(lfrm,textvariable=adrs,font=('Times',14),justify='center')
en2.place(x=150,y=50)



save=Button(lfrm,text='SAVE',font=('Times',10,'bold'),fg='green',command=save)
save.place(x=150,y=120,relwidth=0.16,relheight=0.2)
delete=Button(lfrm,bg='red',text='DELETE',font=('Times',10,'bold'),fg='white',command=remove_one)
delete.place(x=390,y=120,relwidth=0.15,relheight=0.2)



s = ttk.Style()
s.theme_use('clam')

# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading',font=('Times',12), background="orange")

trv=ttk.Treeview(lfrm1,column=(1,2,3))
trv.column('#0',width=0,stretch=NO)
trv.heading('1',text='Number')
trv.column('1',anchor=CENTER)
trv.heading('2',text='Customer')
trv.column('2',anchor=CENTER)
trv.heading('3',text='Address')
trv.column('3',anchor=CENTER)

trv.pack(fill='both',expand='yes')
DisplayData()
verscrlbar = ttk.Scrollbar(trv,
                           orient ="vertical",
                           command = trv.yview)

# Calling pack method w.r.to vertical
# scrollbar
verscrlbar.pack(side ='right',fill='y')

# Configuring treeview
trv.configure(yscrollcommand = verscrlbar.set)

win.mainloop()
