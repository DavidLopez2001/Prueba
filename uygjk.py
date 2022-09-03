import json
listado = input()
jugadores = input()
jugadores = list(jugadores)
dicccionario = json.loads(listado)
Resultado2 = ''
acum = 0
for a in range(len(jugadores)):
    if(jugadores[a] in dicccionario):
        Resultado2 = Resultado2+' '.join(jugadores[a])
        acum= acum + dicccionario.get(jugadores[a])
print(acum)
print(' '.join(map(str,Resultado2)))

