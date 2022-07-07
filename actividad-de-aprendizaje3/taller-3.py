""" 
TALLER 3 PYTHON
AUTOR: Julian David Cordoba Torres (omega5300)
FECHA: 28/06/2022 - 04/07/2022
"""

from datetime import date

fechaHoy = date.today()
print('hoy es el dia:', fechaHoy)
a = int(input('Digite el valor de A: '))
b = int(input('Digite el valor de B: '))

resultado = 'A es mayor o igual a B' if a>=b  else 'B es mayor o igual a A'

print(resultado, '\n')

curso1 = 'Requerimientos'
curso2 = 'Algoritmos'

if curso1 == 'Requerimientos' and curso2 == 'Algoritmos':
    print('Usted estudia Programación de Software\n')
else:
    print('Usted estidia otro program diferente a Programación de Software\n')

print('*** Final del Programa de Formación SENA ***\n')

frase = input('digite una oracion: ')
print(f'la frase en es: {frase.upper()}')

longitud = len(frase)
print(f"la longitud de la frase es: {longitud} caracteres")

if longitud>10:
    print('la frase contiene mas de 10 caracteres\n')
else:
    print('la frase contiene menos de 10 caracteres\n')

print('FIN')
