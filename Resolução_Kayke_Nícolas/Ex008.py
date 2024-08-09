'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

#Variáveis
metro = 0 # Metros que serão convertidos
conversoesValores = [] # Array para guardar as conversões geradas
conversoesNomes = ['Km', 'Hm', 'Dam', 'M', 'Dm', 'Cm', 'Mm'] # Nomes das conversões
contador = 0.001 # Contador auxiliar

#Entrada de dados
metro = float(input("Informe quantos metros serão convertidos: ")) # Armazena a quantidade de metros

#Processamento
while(contador != 10000): # Enquanto não chegar nos milímetros
    atual = metro * contador # A conversão atual será o metro * um contador
    conversoesValores.append(atual) # Essa conversão será armazenada
    contador *= 10 # E o contador multiplicará por 10, iniciando uma nova conversão

#Saída
for i in range(len(conversoesNomes)): # Para cada valor existente
    print(f'{conversoesValores[i]:.3f}{conversoesNomes[i]}') # Exibe o valor e o nome
