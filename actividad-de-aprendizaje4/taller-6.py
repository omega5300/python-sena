""" 
TALLER 6 PYTHON
AUTOR: Julian David Cordoba Torres (omega5300)
FECHA: 05/07/2022 - 11/07/2022
"""

from datetime import date
# fecha actual
fechaHoy = date.today() 
print(f'Hoy es el dia {fechaHoy}\n')

print('TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE\n')

num1 = int(input('digite un numero: '))
print('***Ciclo controlado por contador')
i= 1
while i <= num1:
    print(i)
    i += 1
print('fin del ciclo\n')

print('***Ciclo controlado por evento')
i = 1
numero1 = 5
numero2 = int(input('Digite un numero de 1 a 10: '))

while numero2 != numero1:
    i += i
    numero2 = int(input('Digite un numero de 1 a 10: '))
print('Acertaste en el intento No.', i)
print('fin del ciclo\n')

print('***Ciclo abortado con la sentencia break')
amistad = input('digire nombre de una amistad: ')
amistad = amistad.upper()

for character in amistad:
    print(character)
    if character == 'A':
        break
print('fin del ciclo\n')

print('FIN')
