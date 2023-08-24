import sqlite3
fichiersDonnees ="./bd_test.sq3"
conn=sqlite3.connect(fichiersDonnees)
cur=conn.cursor()
#cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)")
#cur.execute("INSERT INTO membres (age ,nom ,taille)VALUES(21,'Dupont',1.83)")
#cur.execute("INSERT INTO membres (age ,nom ,taille)VALUES(15,'Blumar',1.83)")
#cur.execute("INSERT INTO membres (age ,nom ,taille)VALUES(21,'Dupont',1.83)")
cur.execute("SELECT*FROM membres")
for l in cur:
    print(l)
conn.commit()
cur.close()
conn.close()