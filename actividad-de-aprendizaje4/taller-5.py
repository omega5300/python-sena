""" 
TALLER 5 PYTHON
AUTOR: Julian David Cordoba Torres (omega5300)
FECHA: 05/07/2022 - 11/07/2022
"""

from datetime import date
# fecha actual
fechaHoy = date.today()
print(f'Hoy es el dia {fechaHoy}\n')
print('TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR\n')

num1 = int(input('digite el primer numero: '))
num2 = int(input('digite el segundo numero (mayor): '))

print('ciclo para el primer numero')
for i in range(num1):
    print(i)
print('fin del ciclo\n')

print('ciclo desde el primer numero hasta el segundo numero')
for i in range(num1, num2):
    print(i)
print('fin del ciclo\n')

print('ciclo desde el primero hasta el segundo numero con incremento de 2')
for i in range(num1, num2, 2):
    print(i)
print('fin del ciclo\n')

empresa = input('digite el nombre de la empresa: ')
empresa = empresa.lower()

for character in empresa:
    print(character)
print('fin del ciclo\n')

print('FIN')
