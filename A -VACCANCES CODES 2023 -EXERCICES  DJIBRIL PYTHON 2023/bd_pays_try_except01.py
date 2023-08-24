import json
import sqlite3
try:
    fichierdonnee = "Bd_PaysData_try"
    conn = sqlite3.connect(fichierdonnee)
    cur = conn.cursor()

    cur.execute("CREATE TABLE PAYSDATA(Date TEXT,Pays TEXT,Infection TEXT,Deces TEXT,Guerisons TEXT,TauxDeces TEXT,TauxGuerison TEXT,TauxInfection TEXT)")

    with open('./datas/coronavirus.politologue.com-data-2021-01-26.json','r')as f:
      fichier_json = json.load(f)

    #for i in range(len(fichier_json['PaysData'])):
     #   if fichier_json['PaysData']!="Côte d'Ivoire":
      #      print(fichier_json['PaysData'][i]['Pays'])

    for i in range(len(fichier_json['PaysData'])):
            #print(fichier_json['PaysData'][i]['Pays'])
            cur.execute('INSERT INTO PAYSDATA(Date,Pays,Infection,Deces,Guerisons,TauxDeces,TauxGuerison,TauxInfection)VALUES("'+(fichier_json['PaysData'][i]['Date'])+'","'+str(fichier_json['PaysData'][i]['Pays'])+'",'+str(fichier_json['PaysData'][i]['Infection'])+','+str(fichier_json['PaysData'][i]['Deces'])+','+str(fichier_json['PaysData'][i]['Guerisons'])+','+str(fichier_json['PaysData'][i]['TauxDeces'])+","+str(fichier_json['PaysData'][i]['TauxGuerison'])+','+str(fichier_json['PaysData'][i]['TauxInfection'])+')')
except sqlite3.Error as error:
    print('Error occuried-',error)
finally:
    if conn:
        conn.commit()
        cur.close()
        conn.close()
