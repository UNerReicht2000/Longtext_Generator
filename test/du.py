# -*- coding: utf-8 -*-
from os import path

file = r'C:\Users\dunger\Documents\BBS\01_Projekte\00_Langtext\Langtext_Generator\test\data.txt'

importdat = open(file,'r')
data = importdat.read()
importdat.close()
result = data.split("\n")
data = result

for index in range(len(data)):
    data[index] = data[index].split('=')[0].strip() + '='


with open(file, 'w') as importdat:
    importdat.write("\n".join(data))
print(data)