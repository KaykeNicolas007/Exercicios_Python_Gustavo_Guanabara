'''Crie um algoritmo que leia um número e mostre seu dobro, triplo e
raiz quadrada.'''

from math import sqrt

n = int(input('Informe um número: '))
print(f'''O dobro de {n} é: {n*2}
O triplo: {n*3}
Sua raiz quadrada é: {sqrt(n)}
E elevado ao quadrado: {n*n}''')
