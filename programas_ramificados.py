from ast import If

num_1 = int(input('Escribe un entero: '))
num_2 = int(input('Escribe otro entero: '))

if num_1 > num_2:
    print('El primer numero es mayor que el segundo')
elif num_1 < num_2:
    print('El primer numero es menor que el segundo')
else:
    print('Los dos numeros son iguales')