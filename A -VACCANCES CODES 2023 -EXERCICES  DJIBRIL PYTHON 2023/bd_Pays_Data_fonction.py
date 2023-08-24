import json
import sqlite3
import os


fichierdonnee = "Bd_PaysData_function"
conn = sqlite3.connect(fichierdonnee)
cur = conn.cursor()

cur.execute("CREATE TABLE PAYSDATA(Date TEXT,Pays TEXT,Infection TEXT,Deces TEXT,Guerisons TEXT,TauxDeces TEXT,TauxGuerison TEXT,TauxInfection TEXT)")

def remplir_bd(fichier_json):
    with open('./datas/'+fichier_json,'r')as f:
      fichier_json = json.load(f)
    for i in range(len(fichier_json['PaysData'])):
        # print(fichier_json['PaysData'][i]['Pays'])
        cur.execute(
            'INSERT INTO PAYSDATA(Date,Pays,Infection,Deces,Guerisons,TauxDeces,TauxGuerison,TauxInfection)VALUES("' + (
            fichier_json['PaysData'][i]['Date']) + '","' + str(
            fichier_json['PaysData'][i]['Pays']) + '",' + str(
            fichier_json['PaysData'][i]['Infection']) + ',' + str(
            fichier_json['PaysData'][i]['Deces']) + ',' + str(
            fichier_json['PaysData'][i]['Guerisons']) + ',' + str(
            fichier_json['PaysData'][i]['TauxDeces']) + "," + str(
            fichier_json['PaysData'][i]['TauxGuerison']) + ',' + str(
            fichier_json['PaysData'][i]['TauxInfection']) + ')')

for i in os.listdir('datas'):
    remplir_bd(i)

#for i in range(len(fichier_json['PaysData'])):
 #   if fichier_json['PaysData']!="Côte d'Ivoire":
  #      print(fichier_json['PaysData'][i]['Pays'])

conn.commit()
cur.close()
conn.close()
