import tkinter as tk
import tkinter.messagebox as ms
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql

def insertc():
    name = NameEntryTabOne.get()
    Phone = PhoneEntryTabOne.get()

    if (name=="" or Phone==""):
        ms.showinfo("insert status", "all field are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("INSERT INTO customer (Cname,Phone) VALUES('" + name + "','" + Phone + "')")
        cursor.execute("commit")
        CIDEntryTabOne.delete(0,'end')
        NameEntryTabOne.delete(0, 'end')
        PhoneEntryTabOne.delete(0, 'end')
        ms.showinfo("insert status", "inserted successfully");
        con.close();

def inserto():
    oid = OIDEntryTabTwo.get()
    bid = BIDEntryTabTwo.get()
    mid = MIDEntryTabTwo.get()
    sid = SIDEntryTabTwo.get()
    qo = NumberEntryTabTwo.get()
    if (bid == "" or mid == "" or sid == "" or qo == ""):
        ms.showinfo("insert status", "all field are required")
    elif (int(qo) < 10):
        ms.showinfo("insert staatus","minimum order not satisfied")

    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("INSERT INTO branch_manu (Bid,Mid,Sid,quantities_order) VALUES('" + bid + "','" + mid + "','" + sid + "','" + qo + "')")
        cursor.execute("commit")

        BIDEntryTabTwo.delete(0, 'end')
        MIDEntryTabTwo.delete(0, 'end')
        SIDEntryTabTwo.delete(0, 'end')
        NumberEntryTabTwo.delete(0, 'end')
        ms.showinfo("insert status", "inserted successfully");
        con.close();

def inserta():
    bid = BIDEntryTabFour.get()
    sid = SIDEntryTabFour.get()
    sname = SnameEntryTabFour.get()
    cp = CPEntryTabFour.get()
    sp = SPEntryTabFour.get()
    qs = QSEntryTabFour.get()
    if (bid == "" or sid == "" or sname == "" or cp == "" or sp == "" or qs == ""):
        ms.showinfo("insert status", "all field are required")
    else:
        pro = "0"
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO account VALUES('" + bid + "','" + sid + "','" + sname + "','" + cp + "','" + sp + "','" + qs + "','" + pro + "')")
        cursor.execute("commit")

        BIDEntryTabFour.delete(0, 'end')
        SIDEntryTabFour.delete(0, 'end')
        SnameEntryTabFour.delete(0, 'end')
        CPEntryTabFour.delete(0, 'end')
        SPEntryTabFour.delete(0, 'end')
        QSEntryTabFour.delete(0, 'end')

        ms.showinfo("insert status", "inserted successfully");
        con.close();


def inserts():

    bid = BIDEntryTabThree.get()
    cid = CIDEntryTabThree.get()
    sid = SIDEntryTabThree.get()
    qb = NumberEntryTabThree.get()
    if (bid == "" or cid == "" or sid == "" or qb == ""):
        ms.showinfo("insert status", "all field are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("INSERT INTO branch_customer VALUES('" + bid + "','" + cid + "','" + sid + "','" + qb + "')")

        cursor.execute("commit")

        BIDEntryTabThree.delete(0, 'end')
        CIDEntryTabThree.delete(0, 'end')
        SIDEntryTabThree.delete(0, 'end')
        NumberEntryTabThree.delete(0, 'end')


        ms.showinfo("insert status", "inserted successfully");
        con.close();





def deletec():
    Name = NameEntryTabOne.get()
    if(Name==""):
        ms.showinfo("delete status","Name required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("delete from customer where Cname = '"+ Name +"' ")
        cursor.execute("commit")

        CIDEntryTabOne.delete(0,'end')
        NameEntryTabOne.delete(0, 'end')
        PhoneEntryTabOne.delete(0, 'end')
        ms.showinfo("Delete status", "Deleted successfully");
        con.close();

def deleteo():
    OID = OIDEntryTabTwo.get()
    if(OID==""):
        ms.showinfo("delete status","OID required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("delete from branch_manu where oid = '"+ OID +"' ")
        cursor.execute("commit")

        OIDEntryTabTwo.delete(0, 'end')
        ms.showinfo("Delete status", "Deleted successfully");
        con.close();


def deletes():
    Cid = CIDEntryTabThree.get()
    if(Cid ==""):
        ms.showinfo("delete status", "CID required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("delete from branch_customer where Cid = '" + Cid + "' ")
        cursor.execute("commit")

        CIDEntryTabThree.delete(0, 'end')
        ms.showinfo("Delete status", "Deleted successfully");
        con.close();


def deletea():
    Bid = BIDEntryTabFour.get()
    Sid = SIDEntryTabFour.get()
    if(Bid=="" or Sid==""):
        ms.showinfo("delete status", "Bid and Sid required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("delete from account where Sid = '" + Sid + "' and Bid = '"+Bid+"' ")
        cursor.execute("commit")

        BIDEntryTabFour.delete(0, 'end')
        SIDEntryTabFour.delete(0,'end')
        ms.showinfo("Delete status", "Deleted successfully");
        con.close();


def updatec():
    cid = CIDEntryTabOne.get()
    name = NameEntryTabOne.get()
    Phone = PhoneEntryTabOne.get()

    if (cid=="" or name == "" or Phone == "" ):
        ms.showinfo("Update status", "all field are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("update customer  set Cname = '" + name + "' , Phone = '" + Phone + "' where cid = '" + cid +"' ")
        cursor.execute("commit")

        CIDEntryTabOne.delete(0,'end')
        NameEntryTabOne.delete(0, 'end')
        PhoneEntryTabOne.delete(0, 'end')
        ms.showinfo("Update status", "Updated successfully");
        con.close();



def updateo():
    oid = OIDEntryTabTwo.get()
    bid = BIDEntryTabTwo.get()
    mid = MIDEntryTabTwo.get()
    sid = SIDEntryTabTwo.get()
    qo = NumberEntryTabTwo.get()
    if (oid =="" or bid == "" or mid == "" or sid == "" or qo == ""):
        ms.showinfo("Update status", "all field are required")

    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("Update branch_manu set Bid ='"+bid+"',Mid ='"+mid+"',sid = '"+sid+"',quantities_order= '"+qo+"' where oid = '"+oid+"'")
        cursor.execute("commit")

        BIDEntryTabTwo.delete(0, 'end')
        MIDEntryTabTwo.delete(0, 'end')
        SIDEntryTabTwo.delete(0, 'end')
        NumberEntryTabTwo.delete(0, 'end')
        ms.showinfo("Update status", "updated successfully");
        con.close();



def updates():
    bid = BIDEntryTabThree.get()
    cid = CIDEntryTabThree.get()
    sid = SIDEntryTabThree.get()
    qb = NumberEntryTabThree.get()
    if (bid == "" or cid == "" or sid == "" or qb == ""):
        ms.showinfo("insert status", "all field are required")

    else:
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("Update branch_customer set Cid = '"+cid+"',Sid ='"+sid+"',Quantities_bought ='"+qb+"' where Bid = '"+bid+"'")
        cursor.execute("commit")

        BIDEntryTabThree.delete(0, 'end')
        CIDEntryTabThree.delete(0, 'end')
        SIDEntryTabThree.delete(0, 'end')
        NumberEntryTabThree.delete(0, 'end')
        ms.showinfo("update status", "updated successfully");
        con.close();


def updatea():
    bid = BIDEntryTabFour.get()
    sid = SIDEntryTabFour.get()
    sname = SnameEntryTabFour.get()
    cp = CPEntryTabFour.get()
    sp = SPEntryTabFour.get()
    qs = QSEntryTabFour.get()
    if (bid == "" or sid == "" or sname == "" or cp == "" or sp == "" or qs == ""):
        ms.showinfo("Update status", "all field are required")
    else:
        pro = "0"
        con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
        cursor = con.cursor()
        cursor.execute("update account set Sid = '"+sid+"' ,Sname = '"+sname+"',Cp = '"+cp+"',sp = '"+sp+"', quantities_sold='"+qs+"' where Bid ='"+bid+"'")
        cursor.execute("commit")

        BIDEntryTabFour.delete(0, 'end')
        SIDEntryTabFour.delete(0, 'end')
        SnameEntryTabFour.delete(0, 'end')
        CPEntryTabFour.delete(0, 'end')
        SPEntryTabFour.delete(0, 'end')
        QSEntryTabFour.delete(0, 'end')

        ms.showinfo("Update status", "updated successfully");
        con.close();

def showc():
    list =Listbox(root)
    list.place(x=500,y=50,width=450,height=400)
    con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
    cursor = con.cursor()
    cursor.execute("select * from customer  ")
    rows = cursor.fetchall()

    list.insert("end","CID    Name            Phone")
    list.insert("end","-------------------------------------------------------------------------------------")
    for r in rows:

        a = str(r[0])+"         "+str(r[1])+"             "+str(r[2])

        list.insert("end",a)

    con.close();

def showo():
    list =Listbox(root)
    list.place(x=500,y=50,width=450,height=400)
    con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
    cursor = con.cursor()
    cursor.execute("select * from branch_manu ")
    rows = cursor.fetchall()
    list.insert("end", "OID     BID     MID      SID      quantities_ordered")
    list.insert("end","-------------------------------------------------------------------------------------")

    for r in rows:

        a = str(r[4])+"           "+str(r[0])+"          "+str(r[1])+"          "+str(r[2])+"            "+str(r[3])

        list.insert("end",a)

    con.close();


def shows():
    list =Listbox(root)
    list.place(x=500,y=50,width=450,height=400)
    con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
    cursor = con.cursor()
    cursor.execute("select * from branch_customer")
    rows = cursor.fetchall()
    list.insert("end", "BID     CID      SID      Quantities_bought")
    list.insert("end","-------------------------------------------------------------------------------------")
    for r in rows:
        a = str(r[0])+"           "+str(r[1])+"          "+str(r[2])+"                  "+str(r[3])
        list.insert("end",a)
    con.close();

def showa():
    list =Listbox(root)
    list.place(x=500,y=50,width=450,height=400)
    con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
    cursor = con.cursor()
    cursor.execute("select * from account ")
    rows = cursor.fetchall()
    list.insert("end", "BID       SID          Sname       \t      CP           \t SP          \t   quantities_sold            profit")
    list.insert("end","-------------------------------------------------------------------------------------")
    for r in rows:
        a = str(r[0])+"         "+str(r[1])+"      \t       "+str(r[2])+"          \t    "+str(r[3])+"    \t         "+str(r[4])+"            "+str(r[5])+ "                     "+str(r[6])
        list.insert("end",a)

    con.close()


def search():
    list = Listbox(root)
    list.place(x=500, y=50, width=450, height=400)
    mid = MNameEntryTabFive.get()
    con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
    cursor = con.cursor()
    cursor.callproc('manu_spare',(mid,))
    list.insert("end","SID \t       \t Sname")
    list.insert("end","----------------------------------------------")


    for r in cursor.stored_results():
        a = r.fetchall()

        print(a)
        for aa in a:
            s = str(aa[0])+ "              " +str(aa[1])
            list.insert("end",s)

    con.close()




root = tk.Tk()
root.title("Spare parts database")
root.geometry("1500x1300")
tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 =ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Customer    ")
tab_parent.add(tab2, text="Order    ")
tab_parent.add(tab3, text="Sales   ")
tab_parent.add(tab4, text="Account   ")
tab_parent.add(tab5, text="Search")

# === WIDGETS FOR TAB ONE
CIDLabelTabOne = tk.Label(tab1, text ="CID:")
NameLabelTabOne = tk.Label(tab1, text="Name:")
PhoneLabelTabOne = tk.Label(tab1, text="Phone:")

CIDEntryTabOne = tk.Entry(tab1)
NameEntryTabOne = tk.Entry(tab1)
PhoneEntryTabOne = tk.Entry(tab1)

buttonInsert = tk.Button(tab1, text="Insert", command=insertc)
buttonDelete = tk.Button(tab1, text="Delete",command =deletec)
buttonUpdate = tk.Button(tab1, text="Update",command =updatec)
buttonShow = tk.Button(tab1, text="Show",command = showc)

# === ADD WIDGETS TO GRID ON TAB ONE
CIDLabelTabOne .grid(row=0, column=0, padx=15, pady=15)
CIDEntryTabOne .grid(row=0, column=1, padx=15, pady=15)

NameLabelTabOne .grid(row=1, column=0, padx=15, pady=15)
NameEntryTabOne .grid(row=1, column=1, padx=15, pady=15)

PhoneLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
PhoneEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

buttonInsert.grid(row=3, column=0, padx=15, pady=15)
buttonUpdate.grid(row=3, column=1, padx=15, pady=15)
buttonDelete.grid(row=3, column=2, padx=15, pady=15)
buttonShow.grid(row=3, column=10, padx=15, pady=15)


# === WIDGETS FOR TAB TWO
OIDLabelTabTwo = tk.Label(tab2, text ="OID:")
BIDLabelTabTwo = tk.Label(tab2, text="BID:")
MIDLabelTabTwo = tk.Label(tab2, text="MID:")
SIDLabelTabTwo = tk.Label(tab2, text="SID:")
NumberLabelTabTwo = tk.Label(tab2, text="Quantities ordered")


OIDEntryTabTwo = tk.Entry(tab2)
BIDEntryTabTwo = tk.Entry(tab2)
MIDEntryTabTwo = tk.Entry(tab2)
SIDEntryTabTwo = tk.Entry(tab2)
NumberEntryTabTwo = tk.Entry(tab2)

buttonInsert = tk.Button(tab2, text="Insert",command = inserto)
buttonDelete = tk.Button(tab2, text="Delete", command =deleteo)
buttonUpdate = tk.Button(tab2, text="Update",command = updateo)
buttonShow = tk.Button(tab2, text="Show",command =showo)

# === ADD WIDGETS TO GRID ON TAB TWO

OIDLabelTabTwo.grid(row=0, column=0, padx=15, pady=15)
OIDEntryTabTwo.grid(row=0, column=1, padx=15, pady=15)

BIDLabelTabTwo.grid(row=1, column=0, padx=15, pady=15)
BIDEntryTabTwo.grid(row=1, column=1, padx=15, pady=15)

MIDLabelTabTwo.grid(row=2, column=0, padx=15, pady=15)
MIDEntryTabTwo.grid(row=2, column=1, padx=15, pady=15)

SIDLabelTabTwo.grid(row=3, column=0, padx=15, pady=15)
SIDEntryTabTwo.grid(row=3, column=1, padx=15, pady=15)

NumberLabelTabTwo.grid(row=4, column=0, padx=15, pady=15)
NumberEntryTabTwo.grid(row=4, column=1, padx=15, pady=15)


buttonInsert.grid(row=5, column=0, padx=15, pady=15)
buttonUpdate.grid(row=5, column=1, padx=15, pady=15)
buttonDelete.grid(row=5, column=2, padx=15, pady=15)
buttonShow.grid(row=5, column=4, padx=15, pady=15)


# === WIDGETS FOR TAB THREE
BIDLabelTabThree = tk.Label(tab3, text="BID:")
CIDLabelTabThree = tk.Label(tab3, text="CID:")
SIDLabelTabThree = tk.Label(tab3, text="SID:")
NumberLabelTabThree = tk.Label(tab3, text="Quantities bought")


BIDEntryTabThree = tk.Entry(tab3)
CIDEntryTabThree = tk.Entry(tab3)
SIDEntryTabThree = tk.Entry(tab3)
NumberEntryTabThree = tk.Entry(tab3)

buttonInsert = tk.Button(tab3, text="Insert",command =inserts)
buttonDelete = tk.Button(tab3, text="Delete",command =deletes)
buttonUpdate = tk.Button(tab3, text="Update",command =updates)
buttonShow = tk.Button(tab3, text="Show",command=shows)


# === ADD WIDGETS TO GRID ON TAB THREE
BIDLabelTabThree.grid(row=0, column=0, padx=15, pady=15)
BIDEntryTabThree.grid(row=0, column=1, padx=15, pady=15)

CIDLabelTabThree .grid(row=1, column=0, padx=15, pady=15)
CIDEntryTabThree .grid(row=1, column=1, padx=15, pady=15)

SIDLabelTabThree.grid(row=2, column=0, padx=15, pady=15)
SIDEntryTabThree.grid(row=2, column=1, padx=15, pady=15)

NumberLabelTabThree.grid(row=3, column=0, padx=15, pady=15)
NumberEntryTabThree.grid(row=3, column=1, padx=15, pady=15)


buttonInsert.grid(row=4, column=0, padx=15, pady=15)
buttonUpdate.grid(row=4, column=1, padx=15, pady=15)
buttonDelete.grid(row=4, column=2, padx=15, pady=15)
buttonShow.grid(row=4, column=3, padx=15, pady=15)

# === WIDGETS FOR TAB FOUR
BIDLabelTabFour = tk.Label(tab4, text="BID:")
SIDLabelTabFour = tk.Label(tab4, text="SID:")
SnameLabelTabFour = tk.Label(tab4, text="Sname:")
CPLabelTabFour = tk.Label(tab4, text="Cost price:")
SPLabelTabFour = tk.Label(tab4, text="Selling price:")
QSLabelTabFour = tk.Label(tab4, text="Quantites sold")


BIDEntryTabFour = tk.Entry(tab4)
SIDEntryTabFour = tk.Entry(tab4)
SnameEntryTabFour = tk.Entry(tab4)
CPEntryTabFour = tk.Entry(tab4)
SPEntryTabFour = tk.Entry(tab4)
QSEntryTabFour = tk.Entry(tab4)


buttonInsert = tk.Button(tab4, text="Insert",command =inserta)
buttonDelete = tk.Button(tab4, text="Delete", command = deletea)
buttonShow = tk.Button(tab4, text="Show",command=showa)


# === ADD WIDGETS TO GRID ON TAB FOUR
BIDLabelTabFour.grid(row=0, column=0, padx=15, pady=15)
BIDEntryTabFour.grid(row=0, column=1, padx=15, pady=15)

SIDLabelTabFour .grid(row=1, column=0, padx=15, pady=15)
SIDEntryTabFour .grid(row=1, column=1, padx=15, pady=15)

SnameLabelTabFour.grid(row=2, column=0, padx=15, pady=15)
SnameEntryTabFour .grid(row=2, column=1, padx=15, pady=15)

CPLabelTabFour.grid(row=3, column=0, padx=15, pady=15)
CPEntryTabFour.grid(row=3, column=1, padx=15, pady=15)

SPLabelTabFour.grid(row=4, column=0, padx=15, pady=15)
SPEntryTabFour.grid(row=4, column=1, padx=15, pady=15)

QSLabelTabFour.grid(row=5, column=0, padx=15, pady=15)
QSEntryTabFour.grid(row=5, column=1, padx=15, pady=15)


buttonInsert.grid(row=6, column=0, padx=15, pady=15)

buttonDelete.grid(row=6, column=1, padx=15, pady=15)
buttonShow.grid(row=6, column=2, padx=15, pady=15)


# === WIDGETS FOR TAB Five

MNameLabelTabFive = tk.Label(tab5, text="MName:")

MNameEntryTabFive = tk.Entry(tab5)

buttonsearch = tk.Button(tab5, text="search",command =search)

MNameLabelTabFive.grid(row=0, column=0, padx=15, pady=15)
MNameEntryTabFive.grid(row=0, column=1, padx=15, pady=15)



buttonsearch.grid(row=2, column=0, padx=15, pady=15)



tab_parent.pack(expand=1, fill='both')

root.mainloop()


