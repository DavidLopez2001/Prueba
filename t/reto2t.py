Distancia, VelocidadMaxima, TiempoEnSegundos = input().split()
VelocidadMaxima= float(VelocidadMaxima)
Distancia = float(Distancia)
TiempoEnSegundos = float(TiempoEnSegundos)
Distancia = Distancia/1000
TiempoEnMinutos = (TiempoEnSegundos/60)
TiempoEnHoras = (60/TiempoEnMinutos)
VelocidadAlcanzada = TiempoEnHoras * Distancia 
Diferencia = VelocidadAlcanzada - VelocidadMaxima
Porcentaje = VelocidadMaxima * 0.2 
if(Distancia<0  ):
    print('ERROR')
elif(VelocidadMaxima<0):
    print('ERROR')
elif(TiempoEnSegundos<0):
    print('ERROR')
else:
    if(VelocidadAlcanzada > VelocidadMaxima):
        if(Diferencia >= Porcentaje):
            print("CURSO SENSIBILIZACION")
        else:
            print("MULTA")
    else:
        print("OK")
