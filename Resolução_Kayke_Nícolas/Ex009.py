'''Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.'''

#Variáveis
num = 0 # Número à escolha do usuário

#Entrada
num = int(input("Digite um número inteiro: ")) # Armazena o número do usuário

#Saída
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}") # Exibe a saída da tabuada
