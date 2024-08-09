'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

#Variáveis
nota1 = 0 # Primeira nota do(a) aluno(a)
nota2 = 0 # Segunda nota
media = 0 # Média final

#Leitura de dados
nota1 = float(input("Informe a sua primeira nota: ")) # Armazena a primeira nota
nota2 = float(input("Informe a sua segunda nota: ")) # Armazena a seunda nota

#Processamento
media = (nota1+nota2)/2 # Cálculo da média

#Saída
print(f"Considerando as notas {nota1} e {nota2}, a média resultou: {media:.2f}") # Exibe a media
