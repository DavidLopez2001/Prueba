huevos= input("Ingrese el valor de los huevos: ")
huevos= (int(huevos))
leche= (huevos *2) +4
cafe= (huevos+ leche)//5
if cafe>0 and cafe<21:
    categoria = "uno"
elif cafe>20 and cafe<30:
    categoria = "dos"
elif cafe>30 and cafe<50:
    categoria = "tres"
elif cafe>50 :
    categoria = "cuatro"
print(huevos,leche,cafe,"\n"+categoria)