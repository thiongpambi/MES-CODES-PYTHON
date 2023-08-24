import sqlite3
fichiers_donnees = './IP_bd_test.sq3'
conn = sqlite3.connect(fichiers_donnees)
cur = conn.cursor()

#cur.execute("CREATE TABLE IP_stockage(nom TEXT,ip TEXT ,date TEXT ,heure TEXT)")

ip_tb = []
with open('ip.txt','r')as f:
    for i in f:
        i_split=i.split(';;')
        ip_tb.append(tuple(i_split[0:len(i_split)-1]))
print(ip_tb)

data = ip_tb
#for ligne in data:
   #cur.execute("INSERT INTO IP_stockage(nom,ip,date,heure)VALUES(?,?,?,?)",ligne)

indice=[]
cur.execute("SELECT * FROM IP_stockage")

for l in cur:
    #print(l)
    #print(l[0])
    indice.append(l[0])

#print(indice)
set_indice=set(indice)
#print(set_indice)
#print(indice)

perc=[]
for x in set_indice:
    n=0
    for y in indice:
        if x==y :
            n+=1
    perc.append([x,n])
#print(perc)

indice_index =[]
for x in indice:
    if x.strip()=='index':
        indice_index.append(x)

#print(indice_index,len(indice_index))
indice_files = []
for x in indice:
    if x.strip()=='files':
            indice_files.append(x)

#print(indice_files,len(indice_files))

conn.commit()
cur.close()
conn.close()