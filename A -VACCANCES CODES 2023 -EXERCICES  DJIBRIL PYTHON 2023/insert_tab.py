import sqlite3
conn=sqlite3.connect("IP.bd")
cur=conn.cursor()
#cur.execute("CREATE TABLE IP(nom TEXT,ip INTEGER,date REAL,heure REAL)")
cur.execute("SELECT * FROM IP")
data = [('Durand',192168110,21003120,810),('Sand',192168134,213127,910),('Asan',20014,3654,1424)]
for tu in data:
    cur.execute("INSERT INTO IP(nom,ip,date,heure)VALUES(?,?,?,?)",tu)
conn.commit()
cur.close()
conn.close()
