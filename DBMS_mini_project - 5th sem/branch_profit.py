from matplotlib import pyplot as plt

import pandas as pd
import mysql.connector as mysql

def pro():
    con = mysql.connect(host="localhost", user="root", password="", database='dbms')
    cursor = con.cursor()
    cursor.execute("select Bid,sum(profit) from account group by Bid ")
    r = cursor.fetchall()


    profit = []

    loc = ['Sadashivnagar', 'Rajajinagar', 'Malleshwaram', 'Jayanagar', 'Banashankari']

    for i in range(5):

        a = r[i][1]
        profit.append(a)


    colors = ['#ff9999', '#c2d6d1', '#f0f5f4', '#94b8af', '#9efae3']
    explode = (0.1, 0, 0, 0,0)
    plt.pie(profit, explode=explode, labels=loc, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

    df = pd.DataFrame(list(zip(loc,profit)),
               columns =['Location', 'profit'])
    print(df)



