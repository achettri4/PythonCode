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
    cur.execute("""CREATE TABLE IF NOT EXISTS income(
                id INTEGER PRIMARY KEY,
                ServiceDate TEXT,
                Customer TEXT,
                Address TEXT,
                Contact TEXT,
                Device TEXT,
                Fault TEXT,
                Report TEXT,
                Charge TEXT
                )""")
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
        cur.execute("INSERT INTO income(ServiceDate,Customer,Address,Contact,Device,Fault,Report,Charge)VALUES(?,?,?,?,?,?,?,?)",data)
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
        #tv.insert('',END,text=str(cur.lastrowid),values=data,tags=('oddrow'))
        view()
        conn.close()
        messagebox.showinfo('Complete','Record inserted successfully !!',parent=app)


def view():
    tv.delete(*tv.get_children())
    conn=sqlite3.connect("amrit.db")
    c=conn.cursor()
    c=conn.execute("SELECT rowid, * FROM income")
    
    global count
    count = 0
    for row in c:
        if count%2 == 0:
         
            tv.insert('',END,iid=row[0],values=row[1:],tags=('evenrow',))
        else:
            tv.insert('',END,iid=row[0],values=row[1:],tags=('oddrow',))
        count += 1    
    conn.commit()
    conn.close()

def Update():
    
        data1 = en.get()
        data2 = en1.get()
        data3 = en2.get()
        data4 = en3.get()
        data5 = en4.get()
        data6 = en5.get()
        data7 = en6.get()
        data8 = en7.get()
        
        for selected in tv.selection()[0]:
            en.insert(0, selected)
            en1.insert(0, selected)
            en2.insert(0, selected)
            en3.insert(0, selected)
            en4.insert(0, selected)
            en5.insert(0, selected)
            en6.insert(0, selected)
            en7.insert(0, selected)
            conn = sqlite3.connect("amrit.db")
            cur = conn.cursor()
            cur.execute("UPDATE income SET ServiceDate=?, Customer=?, Address=?, Contact=?, Device=?, Fault=?, Report=?, Charge=? WHERE id=?", (data1,data2,data3,data4,data5,data6,data7,data8,selected))
            conn.commit()
            conn.close()
            tv.delete(*tv.get_children())
            view()
            en.delete(0,END)
            en1.delete(0,END)
            en2.delete(0,END)
            en3.delete(0,END)
            en4.delete(0,END)
            en5.delete(0,END)
            en6.delete(0,END)
            en7.delete(0,END)
            messagebox.showinfo("Updated","Record Updated Successfully",parent=app)


def select(e):
    en.delete(0,END)
    en1.delete(0,END) #Clears SN_entry Box
    en2.delete(0,END) #Clears name_entry Box
    en3.delete(0,END) #Clears num_entry Box
    en4.delete(0,END)
    en5.delete(0,END)
    en6.delete(0,END)
    en7.delete(0,END)
    selected = tv.focus() #Selects the Contacts Focused in Treeview
    values=tv.item(selected, 'values') #Define values variables with the list Selected
    en.insert(0, values[1])
    en1.insert(0, values[2]) #Inserts Name value in Name Entry Box
    en2.insert(0, values[3]) #Inserts Number value in Number Entry Box
    en3.insert(0, values[4]) #Inserts Email value in Email Entry Box
    en4.insert(0, values[5])
    en5.insert(0, values[6])
    en6.insert(0, values[7])
    en7.insert(0, values[8])
    
    

def delete():
    answer = messagebox.askyesno('Cirnform','Do you want to Delete ?')
           
    if answer == False :
        
        messagebox.showinfo('Cancle','Not delete')
    else:
        
        selected=tv.selection()
        rowid=selected[0]
        tv.delete(rowid)
        conn=sqlite3.connect('amrit.db')
        c=conn.cursor()
        c.execute('DELETE from income WHERE rowid = ?',(rowid,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Deleted record successfully')
    


    view() 

     
    
        

app=Tk()
app.geometry('1320x600+15+50')
app.overrideredirect(True)
#app.resizable('false','false')
#app.attributes('-toolwindow',True)
app.title('AMRIT TV SERVICE')
app.iconbitmap(r'C:\Users\amrit\Desktop\BuildingProject\Later A.ico')
app.config(bg='#87CEFA')
def get_time():
    timeVar=time.strftime("%I : %M : %S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)
clock=Label(app,font=("Times",12),text="Digital Clock",fg="darkblue",bg="#87CEFA")
clock.place(x=80)
get_time()

s = ttk.Style()
    
s.configure("TButton",font=('Times',20,'bold'),borderwidth =8)
s.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

lab=Label(app,text='AMRIT TV SERVICE',font=('Snap ITC',26),bg='#87CEFA',fg='#FF6347')
lab.place(x=510)
label=Label(app,text='ServiceDate',font=('Times',11,'bold'),bg='#87CEFA')
label.place(x=20,y=50)
label1=Label(app,text='CustomerName',font=('Times',11,'bold'),bg='#87CEFA')
label1.place(x=20,y=90)
label2=Label(app,text='Address',font=('Times',11,'bold'),bg='#87CEFA')
label2.place(x=20,y=130)
label3=Label(app,text='ContactNumber',font=('Times',11,'bold'),bg='#87CEFA')
label3.place(x=20,y=170)
label4=Label(app,text='DeviceName',font=('Times',11,'bold'),bg='#87CEFA')
label4.place(x=20,y=210)
label5=Label(app,text='Fault',font=('Times',11,'bold'),bg='#87CEFA')
label5.place(x=20,y=250)
label6=Label(app,text='ServiceReport',font=('Times',11,'bold'),bg='#87CEFA')
label6.place(x=20,y=290)
label7=Label(app,text='ServiceCharge',font=('Times',11,'bold'),bg='#87CEFA')
label7.place(x=20,y=330)
bottomlabel=Label(app,text='designBy: @mrit',font=('Times',11,'bold'),fg='#696969',bg='#87CEFA')
bottomlabel.place(x=620,y=580)

A=StringVar()
B=StringVar()
C=StringVar()
D=StringVar()
E=StringVar()
F=StringVar()
G=StringVar()
H=StringVar()

en=DateEntry(app,selectmode='day',date_pattern=("dd-mm-yyyy"),textvariable=A,width=22,justify='center')
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
btn=ttk.Button(app, text='SAVE',style="TButton", command=save)
btn.place(x=300,y=480,height=40)
btn1=ttk.Button(app,text='MODIFY', style="TButton", command=Update)
btn1.place(x=600,y=480,height=40)
btn2=ttk.Button(app,text='DELETE', style="TButton", command=delete)
btn2.place(x=900,y=480,height=40)
#photo = PhotoImage(file = r"C:\Users\amrit\Desktop\BuildingProject\cross.png")
btn3=Button(app,text='X',font=('bold'),bg='#87CEFA',fg='#B22222',activebackground='#87CEFA',relief=FLAT,command=app.destroy)
btn3.place(x=1295,y=0)




# Configure the style of Heading in Treeview widget
s.map('Treeview', background=[('selected', '#D02090')])
s.configure("Treeview",background = "#F5DEB3",foreground = "#A52A2A",fieldbackground = "skyblue")

s.configure('Treeview.Heading',font=('Times',12), background="#ADD8E6")



tv=ttk.Treeview(app,columns=(1,2,3,4,5,6,7,8,9),height=16)
tv.column('#0',width=0,stretch=NO)
tv.heading('#1',text='ID')
tv.column('#1',anchor='center',width=30)
tv.heading('#2',text='ServiceDate')
tv.column('#2',anchor='center')
tv.heading('#3',text='CustomerName')
tv.column('#3',anchor='center')
tv.heading('#4',text='CustomerAddress')
tv.column('#4',anchor='center')
tv.heading('#5',text='ContactNumber')
tv.column('#5',anchor='center')
tv.heading('#6',text='Device')
tv.column('#6',anchor='center')
tv.heading('#7',text='Fault')
tv.column('#7',anchor='center')
tv.heading('#8',text='ServiceReport')
tv.column('#8',anchor='center')
tv.heading('#9',text='ServiceCharge')
tv.column('#9',anchor='center')

tv.place(x=328,y=70,relx=-0.01,relwidth=0.75)

hsb=Scrollbar(app,orient='horizontal',command=tv.xview)
hsb.place(x=317,y=416,relwidth=.749)
tv.configure(xscrollcommand=hsb.set)

vsb=Scrollbar(app,orient='vertical',command=tv.yview)
vsb.place(x=1305,y=70,relheight=0.605)
tv.configure(yscrollcommand=vsb.set)
tv.tag_configure("evenrow", background="#B0E0E6")
tv.tag_configure("oddrow", background="#F5F5DC")
tv.bind('<Double-Button-1>', select)

view()







app.mainloop()
