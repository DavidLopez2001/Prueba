from itertools import count
baldosas, sensor = "7 2".split()
baldosas_revisadas = "1 1 1 1 1 1 1".split()
baldosas_revisadas = list(baldosas_revisadas)
baldosas = int(baldosas)
sensor = int(sensor)
aux = 0
lista =[]
lista2 =[]
lista3 =[]
lista4 =[]
lista5 =[]
for i in range (0,baldosas):
    if not(baldosas_revisadas[i] in lista2): 
        lista2.append(baldosas_revisadas[i])
for p in range (0, len(lista2)):
    aux = aux + (baldosas_revisadas.count(str(lista2[p]))-1)
for i in range (sensor):
        lista3.append(baldosas_revisadas[i])
        if(lista3[i] == lista3[i-1] and sensor>=2 and i != 0):
            lista5.append(lista3)
lista4.append(baldosas_revisadas[sensor])
for p in range (baldosas-sensor):
    if(lista4[0] in lista3):
        lista5.append(lista4)  
    lista3.append(lista4[0])
    if(p+sensor+1 < len(baldosas_revisadas)):
        lista4.append(baldosas_revisadas[p+sensor+1])
    lista4.pop(0)
    lista3.pop(0)
print(aux,len(lista5),baldosas)
        