import sqlite3
fichiers_donnees = './bd_ip_table_global.sq3'
conn = sqlite3.connect(fichiers_donnees)
cur=conn.cursor()
#cur.execute("CREATE TABLE IP_tab(nom TEXT,ip TEXT,date TEXT,heure TEXT)")

ip_tble=[]

with open('ip.txt','r')as f:
    for i in f:
        i_split=i.split(';;')
        ip_tble.append(i_split[0:len(i_split)-1])

print(ip_tble)

#for i in ip_tble:
    #cur.execute("INSERT INTO IP_tab(nom,ip,date,heure)VALUES('"+i[0].strip()+"','"+i[1].strip()+"','"+i[2].strip()+"','"+i[3].strip()+"')")

indice =[]

cur.execute("SELECT * FROM IP_tab")
for l in cur:
    #print(l)
    #print(l[0])
    indice.append(l[0])
#print(indice)

set_indice = set(indice)
#print(set_indice,len(set_indice))
perc = []

for x in set_indice:
    n=0
    for y in indice:
        if y==x:
            n+=1
    perc.append([x,n])

#print(perc)

indice_index =[]
indice_files =[]
indice_moi =[]
indice_python =[]
indice_cfa =[]
indice_chimie =[]
indice_covid =[]
indice_p5 =[]
indice_api_euro =[]
indice_blender =[]
indice_api_dollar =[]
indice_api_cov19 =[]

for x in indice:
    if x.strip()=='index':
        indice_index.append(x)
    elif x.strip()=='files':
        indice_files.append(x)
    elif x.strip()=='moi':
        indice_moi.append(x)
    elif x.strip()=='python':
        indice_python.append(x)
    if x.strip() == 'cfa':
        indice_cfa.append(x)
    elif x.strip() == 'chimie':
        indice_chimie.append(x)
    elif x.strip() == 'covid':
        indice_covid.append(x)
    elif x.strip() == 'p5':
        indice_p5.append(x)
    elif x.strip()=='api_euro':
        indice_api_euro.append(x)
    elif x.strip()=='blender':
        indice_blender.append(x)
    elif x.strip()=='api_dollar':
        indice_api_dollar.append(x)
    elif x.strip()=='api_cov19':
        indice_api_cov19.append(x)
    else:
        pass
total_indice=len(indice_index)+len(indice_files)+len(indice_moi)+len(indice_python)+len(indice_cfa)+len(indice_chimie)+len(indice_covid)+len(indice_p5)+len(indice_api_euro)+len(indice_api_dollar)+len(indice_blender)+len(indice_api_cov19)
#print("index={0}\nfiles={1}\nmoi={2}\npython={3}\ncfa={4}\nchimie={5}\ncovid={6}\np5={7}\napi_euro={8}\nblender={9}\napi_dollar={10}\napi_cov19={11}\ntotal={12}".format(len(indice_index),len(indice_files),len(indice_moi),len(indice_python),len(indice_cfa),len(indice_chimie),len(indice_covid),len(indice_p5),len(indice_api_euro),len(indice_api_dollar),len(indice_blender),len(indice_api_cov19),total_indice))

conn.commit()
cur.close()
conn.close()
