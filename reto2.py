from ctypes import sizeof
Pedro= input()
Pedro = list(Pedro)
Nestor = input()
Nestor = list(Nestor)
Jurado = input()
Jurado = list(Jurado)
auxpuntosPedro=0
auxpuntosNestor= 0
Resultado2 = ''
for i in range(len(Jurado)):
    for a in range (len(Pedro)):
        if(Jurado [i] == Pedro[a]):
            auxpuntosPedro = auxpuntosPedro +1
            break
    for b in range(len(Nestor)):
        if(Jurado [i]== Nestor[b]):
            auxpuntosNestor = auxpuntosNestor +1
            break
    if(auxpuntosNestor == auxpuntosPedro):
            Resultado2 = Resultado2+''.join('L')
    elif(auxpuntosNestor > auxpuntosPedro):
            Resultado2 = Resultado2+''.join('K')
    elif(auxpuntosNestor < auxpuntosPedro):
            Resultado2 = Resultado2+''.join('J')
print(Resultado2)

        
        




