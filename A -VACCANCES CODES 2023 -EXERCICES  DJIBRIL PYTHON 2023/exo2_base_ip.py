import sqlite3
import os

conn=sqlite3.connect("base_ip.db")
cur=conn.cursor()
cur.execute("SELECT * FROM IP")
list_ip_split = ""
list_ip = []

with open("ip.txt",'r')as f:
    ip=f.readlines()
    for l in ip:
        #list_ip.append(l)
        list_ip_split=list_ip_split+l
    print(list_ip_split)



    #lst_set=set(list_ip_split_new)
    #print(lst_set)
    #for t in list_ip_split_new:
     #   list_ip.append(t)
    #lst_ip=set(list_ip)
    #print(lst_ip)
        #cur.execute("INSERT INTO IP (nom,ip,date,heure)VALUES(?,?,?,?)")

conn.commit()
