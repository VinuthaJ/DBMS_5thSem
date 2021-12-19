from matplotlib import pyplot as plt
import pandas as pd
import mysql.connector as mysql

def show():
    con = mysql.connect(host="localhost", user="root", password="", database='dbms_project')
    cursor = con.cursor()
    cursor.execute(" (select Sid,Sname, sum(quantities_sold) from account  GROUP BY Sid) ORDER BY sum(quantities_sold) desc limit 0,10 ")
    r = cursor.fetchall()



    sid = []
    sname = []
    qo= []

    for i in range(0,10):
        a = r[i][0]
        sid.append(a)
        b = r[i][1]
        sname.append(b)
        c = r[i][2]
        qo.append(c)

    colors = ['#ff9999', '#c2d6d1', '#f0f5f4', '#94b8af', '#9efae3', '#ff6347', '#bcc9d6', '#ebeff2', '#cacbcc', '#d9fadc']

    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    plt.pie(qo, explode=explode, labels=sid, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

    
    df = pd.DataFrame(list(zip(sid,sname,qo)),
               columns =['sid', 'sname','quantities_sold'])
    print(df)


show()