from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry
from datetime import date, datetime
from tkinter import Label

import time
import sys

def connect():
    conn=sqlite3.connect("amrit.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS income(ServiceDate TEXT,Customer TEXT,Address TEXT,Contact TEXT,Device TEXT,Fault TEXT,Report TEXT,Charge TEXT,id INTEGER PRIMARY KEY)")
    conn.commit()
    conn.close()
connect()    
    
    

def save():
    if A.get() == '':
        messagebox.showerror('Warning','Please Enter Service Date !!', parent=app)
        en.focus_force()
    elif B.get() == '':
        messagebox.showerror('Warning','Please Enter Customer Name !!', parent=app)
        en1.focus_force()
    elif C.get() == '':
        messagebox.showerror('Warning','Please Enter Customer Address !!', parent=app)
        en2.focus_force()
    elif D.get() == '':
        messagebox.showerror('Warning',"Please Enter Customer's Contact Number !!",parent=app)
        en3.focus_force()
    elif E.get() == '':
        messagebox.showerror('Warning','Please Enter Device Type !!', parent=app)
        en4.focus_force()
    elif F.get() == '':
        messagebox.showerror('Warning','Please Enter Fault Of Device !!', parent=app)
        en5.focus_force()
    elif G.get() == '':
        messagebox.showerror('Warning','Please Enter Service Report !!', parent=app)
        en6.focus_force()
    elif H.get() == '':
        messagebox.showerror('Warning','Please Enter Service Charge !!', parent=app)
        en7.focus_force()
    else:
        
        conn=sqlite3.connect("amrit.db")
        cur=conn.cursor()
        data=(A.get(),B.get(),C.get(),D.get(),E.get(),F.get(),G.get(),H.get())
        cur.execute("INSERT INTO income(ServiceDate,Customer,Address,Contact,Device,Fault,Report,Charge,id)VALUES(?,?,?,?,?,?,?,?,null)",data)
        conn.commit()
        en.delete(0,END)
        en1.delete(0,END)
        en2.delete(0,END)
        en3.delete(0,END)
        en4.delete(0,END)
        en5.delete(0,END)
        en6.delete(0,END)
        en7.delete(0,END)
        en.focus()
        tv.insert('',END,text=str(cur.lastrowid),values=data,tags=('oddrow'))
        conn.close()
        messagebox.showinfo('Complete','Record inserted successfully !!',parent=app)


def view():
    conn=sqlite3.connect("amrit.db")
    c=conn.cursor()
    c=conn.execute("SELECT rowid, * FROM income")

   
   
    for row in c:
         
            tv.insert('',END,iid=row[0],values=row[1:])
        
    conn.commit()
       

def delete():
    
    answer = messagebox.askyesno(title='Confirm',
                    message='Are you sure that you want to delete selected record?')
    if not answer:
         messagebox.showinfo('EmptyTable','There is nothing to delete')
    if answer:
     selected=tv.selection()
     rowid=selected[0]
     tv.delete(rowid)
     conn=sqlite3.connect('amrit.db')
     c=conn.cursor()
     c.execute('DELETE from income WHERE rowid = ?',(rowid,))
     conn.commit()
     conn.close()
     messagebox.showinfo('Success','Deleted record successfully')
   
       
    
    
    

     
    
        

app=Tk()
app.geometry('1320x600+15+50')
app.overrideredirect(True)
#app.resizable('false','false')
#app.attributes('-toolwindow',True)
app.title('AMRIT TV SERVICE')
app.iconbitmap(r'C:\Users\amrit\Desktop\BuildingProject\Later A.ico')
app.config(bg='#F5DEB3')
def get_time():
    timeVar=time.strftime("%I : %M : %S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)
clock=Label(app,font=("Times",12),text="Digital Clock",fg="darkblue",bg="#F5DEB3")
clock.place(x=80)
get_time()

lab=Label(app,text='AMRIT TV SERVICE',font=('Snap ITC',26),bg='#F5DEB3',fg='#FF6347')
lab.place(x=510)
label=Label(app,text='ServiceDate',font=('Times',11,'bold'),bg='#F5DEB3')
label.place(x=20,y=50)
label1=Label(app,text='CustomerName',font=('Times',11,'bold'),bg='#F5DEB3')
label1.place(x=20,y=90)
label2=Label(app,text='Address',font=('Times',11,'bold'),bg='#F5DEB3')
label2.place(x=20,y=130)
label3=Label(app,text='ContactNumber',font=('Times',11,'bold'),bg='#F5DEB3')
label3.place(x=20,y=170)
label4=Label(app,text='DeviceName',font=('Times',11,'bold'),bg='#F5DEB3')
label4.place(x=20,y=210)
label5=Label(app,text='Fault',font=('Times',11,'bold'),bg='#F5DEB3')
label5.place(x=20,y=250)
label6=Label(app,text='ServiceReport',font=('Times',11,'bold'),bg='#F5DEB3')
label6.place(x=20,y=290)
label7=Label(app,text='ServiceCharge',font=('Times',11,'bold'),bg='#F5DEB3')
label7.place(x=20,y=330)
bottomlabel=Label(app,text='designBy: @mrit',font=('Times',11,'bold'),fg='#696969',bg='#F5DEB3')
bottomlabel.place(x=620,y=580)

A=StringVar()
B=StringVar()
C=StringVar()
D=StringVar()
E=StringVar()
F=StringVar()
G=StringVar()
H=StringVar()

en=DateEntry(app,selectmode='day',date_pattern=('dd-mm-yyyy'),textvariable=A,width=22,justify='center')
en.place(x=150,y=50,height=25)
en1=Entry(app,textvariable=B,bg='#FAFAD2',width=25,justify='center')
en1.place(x=150,y=90,height=25)
en2=Entry(app,textvariable=C,bg='#FAFAD2',width=25,justify='center')
en2.place(x=150,y=130,height=25)
en3=Entry(app,textvariable=D,bg='#FAFAD2',width=25,justify='center')
en3.place(x=150,y=170,height=25)
en4=Entry(app,textvariable=E,bg='#FAFAD2',width=25,justify='center')
en4.place(x=150,y=210,height=25)
en5=Entry(app,textvariable=F,bg='#FAFAD2',width=25,justify='center')
en5.place(x=150,y=250,height=25)
en6=Entry(app,textvariable=G,bg='#FAFAD2',width=25,justify='center')
en6.place(x=150,y=290,height=25)
en7=Entry(app,textvariable=H,bg='#FAFAD2',width=25,justify='center')
en7.place(x=150,y=330,height=25)
btn=Button(app,text='SAVE',width=25,font=('Rockwell',12),bg='#9ACD32',command=save)
btn.place(x=300,y=480,height=40)
btn1=Button(app,text='MODIFY',width=25,font=('Rockwell',12),bg='#F0E68C')
btn1.place(x=600,y=480,height=40)
btn2=Button(app,text='DELETE',width=25,font=('Rockwell',12),bg='#F08080',command=delete)
btn2.place(x=900,y=480,height=40)
#photo = PhotoImage(file = r"C:\Users\amrit\Desktop\BuildingProject\cross.png")
btn=Button(app,text='X',font=('bold'),bg='#F5DEB3',fg='#B22222',activebackground='#F5DEB3',relief=FLAT,command=app.destroy)
btn.place(x=1295,y=0)


s = ttk.Style()
s.theme_use('clam')

# Configure the style of Heading in Treeview widget
s.map('Treeview', background=[('selected', '#D02090')])
#s.configure("Treeview",background = "#F5DEB3",foreground = "#A52A2A",fieldbackground = "silver")

s.configure('Treeview.Heading',font=('Times',12), background="#ADD8E6")



tv=ttk.Treeview(app,columns=(1,2,3,4,5,6,7,8,9),height=16)
tv.column('#0',width=0,stretch=NO)
tv.heading('#9',text='ID')
tv.column('#9',anchor='center',width=30)
tv.heading('#1',text='ServiceDate')
tv.column('#1',anchor='center')
tv.heading('#2',text='CustomerName')
tv.column('#2',anchor='center')
tv.heading('#3',text='CustomerAddress')
tv.column('#3',anchor='center')
tv.heading('#4',text='ContactNumber')
tv.column('#4',anchor='center')
tv.heading('#5',text='Device')
tv.column('#5',anchor='center')
tv.heading('#6',text='Fault')
tv.column('#6',anchor='center')
tv.heading('#7',text='ServiceReport')
tv.column('#7',anchor='center')
tv.heading('#8',text='ServiceCharge')
tv.column('#8',anchor='center')

tv.place(x=328,y=62,relx=-0.01,relwidth=0.75)

hsb=Scrollbar(app,orient='horizontal',command=tv.xview)
hsb.place(x=317,y=416,relwidth=.749)
tv.configure(xscrollcommand=hsb.set)

vsb=Scrollbar(app,orient='vertical',command=tv.yview)
vsb.place(x=1305,y=62,relheight=0.619)
tv.configure(yscrollcommand=vsb.set)
tv.tag_configure("evenrow", background="red")


view()







app.mainloop()
