entrada = input()
separado = entrada.split(',')
acumulador = 0
Resultado1 = []
Resultado2 = ''
for i in range (len(separado)):
    if(len(separado)> i+1):
        if(separado[i].upper()==separado[i+1].upper()):
            acumulador = acumulador +1
        elif(separado[i].upper()!=separado[i+1].upper()):
            Resultado2 = Resultado2+' '.join(separado[i].upper())
            Resultado1.append(acumulador+1)
            acumulador = 0   
    elif(len(separado) == i+1):
        Resultado2 = Resultado2+''.join(separado[i].upper())
        Resultado1.append(acumulador+1)
print(' '.join(map(str,Resultado2)))
print(' '.join(map(str,Resultado1)))



    

       
