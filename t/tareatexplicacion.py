Horas, valorHora = ("49 1000").split() # Aca llame a los valores de hora y de valor hora separados por un espacio
Horas = int(Horas) # Convierto a entero(numerico) el dato de texto 
valorHora = float(valorHora)# Convierto a float(decimal) el dato de texto 

if(Horas < 40):# Valido si el numero de horas es menor a 40
    print("El valor hora es de: ",Horas* valorHora ) # Si es menor multiplico el valor de horas por el numero de horas al no tener extras
elif(Horas < 48): # valido si es menor a 48 horas
    horaExtra =  Horas - 40 # Miro cuantas horas extras genero al quitarle las 40 normales
    print("El valor hora es de: ", ((40 * valorHora) + (horaExtra * (valorHora*2))) )#Hago lo de arriba y ademas las extras las multiplico por el doble del precio
else: # Si no son menores a 40, ni menores a 48 ya entran las horas extras que pagan el triple
    horaExtraTriple = Horas - 48 # miro cuantas horas extras del triple gano
    horaExtraDoble = (Horas - horaExtraTriple) - 40 #miro cuantas horas extras del doble del precio hizo
    print("El valor hora es de: ", ((40 * valorHora)+(horaExtraTriple * (valorHora *3))+(horaExtraDoble * (valorHora * 2)))  )
    # Hago la operacion de multiplicar el numero de horas extras normales, horas extras triples y las horas trabajadas