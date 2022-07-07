"""
TALLER 1 PYTHON
AUTOR(A): Julian David Cordoba Torres (omega5300)
FECHA: 13-06-2022 - 20-06-2022
"""

# importar el modulo datetime
from datetime import date

# imprime la fecha actual
fechaHoy = date.today()
print('hoy es el dia', fechaHoy)

# operaciones
num1 = int(input('digite el primer número: '))
num2 = int(input('digite el segundo número: '))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2

# imprimir operaciones
print('La suma es =', suma)
print('La resta es =', resta)
print('el producto es =', producto)
print('La division es =', division, '\nfin')
