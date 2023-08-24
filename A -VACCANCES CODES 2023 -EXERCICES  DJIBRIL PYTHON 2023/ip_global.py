import sqlite3
donnees_fichiers = "./ip_global.sq3"
conn=sqlite3.connect(donnees_fichiers)
cur = conn.cursor()
#cur.execute("CREATE TABLE IP_GLOBAL(page TEXT,ip TEXT,date TEXT,heure TEXT)")

ip_list_tb = []

with open('ip.txt','r')as f:
    for i in f:
        i_split=i.split(';;')
        ip_list_tb.append(tuple(i_split[0:len(i_split)-1]))

#print(ip_list_tb)

data = ip_list_tb
#for i in data:
 #   cur.execute("INSERT INTO IP_GLOBAL(page,ip,date,heure)VALUES(?,?,?,?)",i)
indice = []
cur.execute("SELECT * FROM IP_GLOBAL")
for i in cur:
    #print(i)
    indice.append(i[0])
#print(indice)
set_indice =set(indice)
#print(set_indice)
perc_indice = []
for x in set_indice:
    n=0
    for y in indice:
        if x==y:
            n=n+1
    perc_indice.append([x,n])

print(perc_indice)

conn.commit()
cur.close()
conn.close()
