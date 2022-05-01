import time

objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

start_time = time.time()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada del {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

end_time = time.time() - start_time
print(f'La ejecución demoró: {end_time}')