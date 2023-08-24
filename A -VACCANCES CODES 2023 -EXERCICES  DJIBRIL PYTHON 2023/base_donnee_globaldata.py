import sqlite3
import os
import json

fichiersDonnees = "./bd_GlobalData.sq3"
conn = sqlite3.connect(fichiersDonnees)
cur = conn.cursor()

#cur.execute("CREATE TABLE GlobalData(Date TEXT,Infection TEXT,Deces TEXT,Guerisons TEXT,TauxDeces TEXT,TauxGuerison TEXT,TauxInfection TEXT)")

#print(os.listdir('datas'))

def remplir_globaldata(fichier_json):
    with open('./datas/'+fichier_json,'r')as f:
        fichier_json = json.load(f)
    #print(fichier_json['GlobalData'][0],' et longueur globaldata=',len(fichier_json['GlobalData']))
   # for i in range(len(fichier_json['GlobalData'])):
    #    cur.execute("INSERT INTO GlobalData(Date,Infection,Deces,Guerisons,TauxDeces,TauxGuerison,TauxInfection)VALUES('"+(fichier_json['GlobalData'][i]['Date'])+"','"+str((fichier_json['GlobalData'][i]['Infection']))+"','"+str((fichier_json['GlobalData'][i]['Deces']))+"','"+str((fichier_json['GlobalData'][i]['Guerisons']))+"','"+str((fichier_json['GlobalData'][i]['TauxDeces']))+"','"+str((fichier_json['GlobalData'][i]['TauxGuerison']))+"','"+str((fichier_json['GlobalData'][i]['TauxInfection']))+"')")

for i in os.listdir('datas'):
    #print(i,type(i))
    remplir_globaldata(i)
    
cur.execute("SELECT * FROM GlobalData")
for ln in cur:
    print(ln)

conn.commit()
cur.close()
conn.close()

