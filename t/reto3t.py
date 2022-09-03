a= int(input())
lista_resultados = []
for i in range(a):
    validar = True
    ejePedalier, bielas, sillin, manillar, precio = input().split()
    ejePedalier = int(ejePedalier)
    bielas = int(bielas)
    sillin = int(sillin)
    manillar = int(manillar)
    precio = int(precio)
    if(ejePedalier < 240 or ejePedalier>300):
        validar = False
    if(bielas < 160 or bielas>180):
        validar = False
    if(sillin < 240 or sillin>275):
        validar = False
    if(manillar>50):
        validar = False
    if(validar == True):
        lista_resultados.append(precio)
        print("agregar")
if(len(lista_resultados)>=1):
    print(''.join(map(str, lista_resultados)))
else:
    print("NO DISPONIBLE")


    

