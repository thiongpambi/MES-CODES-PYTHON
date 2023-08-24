import json
import sqlite3
import os


fichierdonnee = "Bd_PaysData_funct_var"
conn = sqlite3.connect(fichierdonnee)
cur = conn.cursor()

cur.execute("CREATE TABLE PAYS_DATAS(Date TEXT,Pays TEXT,Infection TEXT,Deces TEXT,Guerisons TEXT,TauxDeces TEXT,TauxGuerison TEXT,TauxInfection TEXT)")

def remplir_bd(fichier_json):
    with open('./datas/'+fichier_json,'r')as f:
      fichier_json = json.load(f)

    for i in range(len(fichier_json['PaysData'])):
        # print(fichier_json['PaysData'][i]['Pays'])
        Date = fichier_json['PaysData'][i]['Date']
        Pays = fichier_json['PaysData'][i]['Pays']
        Infection = fichier_json['PaysData'][i]['Infection']
        Deces = fichier_json['PaysData'][i]['Deces']
        Guerisons = fichier_json['PaysData'][i]['Guerisons']
        TauxDeces = fichier_json['PaysData'][i]['TauxDeces']
        TauxGuerison = fichier_json['PaysData'][i]['TauxGuerison']
        TauxInfection = fichier_json['PaysData'][i]['TauxInfection']
        cur.execute(
            'INSERT INTO PAYS_DATAS(Date,Pays,Infection,Deces,Guerisons,TauxDeces,TauxGuerison,TauxInfection)VALUES("' + (Date) + '","' + str(Pays) + '",' + str(Infection) + ',' + str(Deces) + ',' + str(Guerisons) + ','
            + str(TauxDeces) + "," + str(TauxGuerison) + ',' + str(TauxInfection) + ')')

for i in os.listdir('datas'):
    remplir_bd(i)

#for i in range(len(fichier_json['PaysData'])):
 #   if fichier_json['PaysData']!="Côte d'Ivoire":
  #      print(fichier_json['PaysData'][i]['Pays'])

conn.commit()
cur.close()
conn.close()
