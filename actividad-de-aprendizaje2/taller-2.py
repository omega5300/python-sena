"""
TALLER 1 PYTHON
AUTOR(A): Julian David Cordoba Torres (omega5300)
FECHA: 13/06/2022 - 20/06/2022
"""

# importat el modulo datetime
from datetime import date

fechaHoy = date.today()

# imprimir fecha actual
print('Hoy es el dia:', fechaHoy)

# digitar numeros
num1 = int(input('digite el primer número: '))
num2 = int(input('digite el segundo número: '))
num3 = int(input('digite el tercer número: '))

# arreglo de numeros
x = [num1, num2, num3]

# operaciones con arreglos
print('El valor maximo es:', max(x))
print('El valor minimo es:', min(x))
print('La suma de los tres números es:', sum(x), '\n')

# redondear cifras
z = float(input('digite un numero con decimales: '))
redondo = round(z)

print(f'el valor de {z} redondeado es: {redondo}\n')

frase = input('digite una oración: ')

print('La frase en mayuscula es:', frase.upper())
print('La frase en minuscula es:', frase.lower())
print('La frase con mayuscula inicial es:', frase.capitalize())
print('La frase con palabras en mayusculas es:', frase.title())
print(f'La longitud de la frase es: {len(frase)} caracteres \n\nFIN')
