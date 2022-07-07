""" 
TALLER 4 PYTHON
AUTOR: Julian David Cordoba Torres (omega5300)
FECHA: 28/06/2022 - 04/07/2022
"""

from datetime import date

fechaHoy = date.today()
print(f'hoy es el dia: {fechaHoy}\n')
print('EJERCICIO DE LAS CLASES DE TRIANGULOS\n')

a = int(input('digite el valor de A: '))
b = int(input('digite el valor de B: '))
c = int(input('digite el valor de C: '))

if a ==b and a==c and b==c:
    print('EL TRIANGULO ES EQUILATERO\n')
else:
    if a==b or b==c or a==c:
        print('EL TRIANGULO ES ISOCELES\n')
    else:
        print('EL TRIANGULO ES ESCALENO\n')

animal = input('digite un animal: ')
animal = animal.upper()

if animal == 'PERRO':
    print(f'Este animal es el mejor amigo del hombre: {animal}\n')
elif animal == 'GATO':
    print(f'Este animal persigue a los ratones: {animal}\n')
elif animal == 'OSO':
    print(f'Este animal vive en el polonorte: {animal}\n')
else:
    print(f'No es PERRO, no es GATO, ni es OSO es: {animal}\n')

print('FIN')