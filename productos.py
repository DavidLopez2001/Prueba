

def grupos(lista):
    lista_resultados = []
    for i in lista:
        if i not in lista_resultados:
            lista_resultados.append(i)

    return(lista_resultados) 


def necesito_del_grupo (lista_indices, lista, grupo):
    gruponecesario = []
    for i in lista_indices:
        if(grupo == lista[i]):
                gruponecesario.append(i)

    return gruponecesario

def sirven_a_marta (Lista1, lista2):
    Sirve_marta=  []
    for i in Lista1:
        if i not in lista2:
            Sirve_marta.append(i)
    return Sirve_marta

def cuantas_cambian(lista_marta, lista_maria):
    cambia_maria = []
    cambia_marta = []
    for i in lista_maria: 
        if i not in lista_marta: 
            cambia_maria.append(i)
    for j in lista_marta: 
        if j not in lista_maria: 
            cambia_marta.append(j)
    minimo = min(len(cambia_marta),len(cambia_maria))   
    return minimo