import sqlite3
conn=sqlite3.connect("donne_ip.db")
cur=conn.cursor()
#cur.execute("CREATE TABLE tableIP(dossier TEXT,ip TEXT,date TEXT,heure TEXT)")
cur.execute("SELECT * FROM tableIP")
cur.execute("INSERT INTO tableIP(dossier,ip,date,heure)VALUES('index','34.224.224.87','2020-11-11','01:50:54')")
cur.execute("INSERT INTO tableIP(dossier,ip,date,heure)VALUES('files','41.82.110.191','2020-11-11','01:56:51')")
cur.execute("INSERT INTO tableIP(dossier,ip,date,heure)VALUES('moi','41.82.110.191','2020-11-11','01:57:31')")
cur.execute("INSERT INTO tableIP(dossier,ip,date,heure)VALUES('python','41.82.110.191','2020-11-11','01:57:59')")
conn.commit()
cur.close()
conn.close()

