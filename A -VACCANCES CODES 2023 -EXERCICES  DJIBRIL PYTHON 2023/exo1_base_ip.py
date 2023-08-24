import sqlite3
conn=sqlite3.connect("base_ip.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IP(nom TEXT,ip INTEGER,date REAL,heure REAL)")
conn.commit()
cur.close()
conn.close()
