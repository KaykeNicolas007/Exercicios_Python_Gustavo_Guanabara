'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta ncecessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².'''

from knlib import text

#CABEÇALHO
text.imprimirCabecalho('PINTURA DE PAREDE')
print('Você vai dizer a largura e a altura de uma parede. Com isso, saberá a quantidade de tinta necessária para pintá-la')

#INICIAlIZAÇÂO
largura = 0 # Largura da parede
altura = 0 # Altura da parede
area = 0 # Área total da parede
qntdTinta = 0 # Quantidade de tinta necessária para pintar (em litros)

#ENTRADA DE DADOS
largura = float(input('Informe a largura da parede (em metros): '))
altura = float(input('Informe a altura da parede (em metros): '))

#PROCESSAMENTO
area = largura * altura # A área de um quadrilátero é a sua base multiplicado pela altura. Tomemos largura e base como iguais.
qntdTinta = area/2 # Quantidade de litros de tinta é a divisão a área total da parede pela quantidade de área que cada litro consegue pintar

#Saída
print(f'Para pintar uma parede de {area:.1f}m², você precisará de aproximadamente {qntdTinta:.1f} litros de tinta, considerando que cada litro pinta 2m².')