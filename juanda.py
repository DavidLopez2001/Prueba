
productos = []
precios = []
cantidades = []
precioA = 0
precioAI = 0
for p in range (3):
    producto = input("Digite el nombre del producto "+str(p+1)+": ")
    productos.append(producto)
    preciou = input("Digite valor del producto "+str(p+1)+": ")
    preciou = int (preciou)
    precios.append(preciou)
    cantidad = input("Digite cantidad del producto "+str(p+1)+": ")
    cantidad = int (cantidad)
    cantidades.append(cantidad)
    precioA = precioA + (cantidad * preciou) 
    precioAI = precioAI + (cantidad * preciou) + (cantidad * preciou * 0.19)
print("Te mostraré los productos que ingresaste: ")
for i in range (3):
    print("Producto: "+productos[i] +" Cantidad: " +str (cantidades[i])+ " Precio Unitario: "+ str(precios[i])+"Valor Total: "+ str(precios[i] * cantidades[i])+" Valor iva:"+ str((precios[i] * cantidades[i]) * 0.19))

print ("Varlor Total: "+ str (precioA))
print ("Varlor Total IVA INCLUIDA: "+ str (precioAI))



