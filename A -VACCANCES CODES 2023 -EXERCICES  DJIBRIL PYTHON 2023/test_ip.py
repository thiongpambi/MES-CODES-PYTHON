import sqlite3
import json
donneefichier="./bata_test.sq3"
conn=sqlite3.connect(donneefichier)
cur = conn.cursor()
#cur.execute("CREATE TABLE ip_data(appli TEXT,ip TEXT,date TEXT,heure )")
#cur.execute("INSERT INTO ip_data(appli ,ip,date,heure)VALUES('index','34.224.224.87',' 2020-11-11 ','01:50:54 ')")

def ecrire_fichier_json(fichier_json,dictionnaire):
    with open(fichier_json,'w')as f:
        json.dump(dictionnaire,f,indent=5)

struct_ch = ""

with open('ip.txt','r')as f:
    ligne=f.readlines()
    for i in ligne:
        #print(i)
        struct_ch=struct_ch+i

struct_ch_split = struct_ch.split(';;')

#print(set(struct_ch_split))

structures = struct_ch_split
fructs = tuple(struct_ch.split(';;'))
fichier_json = './structure.json'
fichier_json_1='./struct_bis.json'
fichier_json_2='./truc.json'
fichier_json_3='./fruct.json'

ecrire_fichier_json(fichier_json,structures)
ecrire_fichier_json(fichier_json_1,structures)
ecrire_fichier_json(fichier_json_2,structures)
ecrire_fichier_json(fichier_json_3,fructs)


"""        
data = [('index','24.35.124.55','2020-11-23','01:45:35'),('covid','24.35.124.55','2020-11-23','01:45:35'),('files','24.35.124.55','2020-11-23','01:45:35')]
for tu in data:

    cur.execute("INSERT INTO ip_data(appli,ip,date,heure)VALUES(?,?,?,?)",tu)
cur.execute("SELECT * FROM ip_data")
for l in cur:
    print(l)"""
conn.commit()
cur.close()
conn.close()