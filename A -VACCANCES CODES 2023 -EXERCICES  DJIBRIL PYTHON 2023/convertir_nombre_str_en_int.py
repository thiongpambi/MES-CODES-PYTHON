nbre_str='2,34 millions de km2'
nbre_str_1=nbre_str.replace(',','.')
#print(nbre_str_1)
nbre_str_2=nbre_str_1.split('millions')
print(nbre_str_2)
a=nbre_str_2[0]
b=nbre_str_2[1]
#print(a,'et',b)
c=float(a)*1000000
print(c*1000)
#d=str(c)+b
#print(d)
# e=str(c)
# print(e)
