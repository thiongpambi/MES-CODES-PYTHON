import numpy as np
def moyenne(liste):
    return sum(liste)/(len(liste))
revenus = [1800,1500,2200,3000,2172]
moy1=moyenne(revenus)
print('moyenne=',moy1)

moy2_num=np.mean(revenus)
print('moyenne_num',moy2_num)
