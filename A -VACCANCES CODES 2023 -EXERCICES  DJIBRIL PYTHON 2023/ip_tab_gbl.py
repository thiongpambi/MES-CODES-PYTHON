import sqlite3

file_data = "./ip_table_tuple.sq3"
conn = sqlite3.connect(file_data)
cur=conn.cursor()

#cur.execute("CREATE TABLE IP_tuple(nom TEXT,ip TEXT,date TEXT,heure TEXT)")

tb_l=[]

with open('ip.txt','r')as f:
    for k in f:
        #print(k)
        k_split = k.split(';;')
        #print(k_split)
        tb_l.append(k_split[0:len(k_split)-1])

#print(tb_l)
for tir in tb_l:
    cur.execute("INSERT INTO IP_tuple(nom,ip,date,heure)VALUES(?,?,?,?)",tir)

conn.commit()
cur.close()
conn.close()
