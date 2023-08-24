nbre_str = '2,34 millions de km2'
print('nbre_str={0}'.format(nbre_str))
nbre_str_1 = nbre_str.replace(',','.')
print('nbre_str_1={0}'.format(nbre_str_1))
nbre_str_2 = nbre_str_1.replace('millions','000000')
print('nbre_str_2={0}'.format(nbre_str_2))
nbre_str_3 = nbre_str_2.split(' ')
print('nbre_str_3={0}'.format(nbre_str_3))
nbre_str_4 = ''.join(nbre_str_3[0:2])
print('nbre_str_4={0}'.format(nbre_str_4))
nbre_str_5 =float(nbre_str_4)
print('nbre_str_5={0}'.format(nbre_str_5))
print(type(nbre_str_5))

