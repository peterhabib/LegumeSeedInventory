import re
lista=set()
file=open('/home/peter/Desktop/New_App/Chickpea seed in barrels(Terbol) (1).csv','r').readlines()

for line in file:
    line=re.split(',',line)
    print(line[2])
    lista.add(line[2])


print(lista)