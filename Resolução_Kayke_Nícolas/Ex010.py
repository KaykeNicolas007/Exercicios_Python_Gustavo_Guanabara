'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''
import os

#FUNÇÕES
def imprimirCabecalho(nome):
    """
    Imprime um cabeçalho simples.
        :nome: String a ser impressa na tela
    """
    tam = len(nome) # Tamanho do nome passado como parâmetro
    os.system('cls') # Limpa o terminal
    print(f'-'*(tam*2))
    print(f'{nome.center(tam*2)}')
    print(f'-'*(tam*2))


def imprimirMenu(menu):
    """
    Imprime na tela um menu simples.
        :menu: Array com opções
    """
    # Imprime uma opção para cada elemento do menu
    for i in range(len(menu)):
        print(f'{i+1} - [{menu[i]}]')


def converter(esc1, esc2, valor, cambios):
    """
    Converte as moedas selecionadas
        :esc1: Moeda que será convertida
        :esc2: Objetivo da conversão
        :valor: O valor a ser convertido
        :cambios: Matriz contendo as taxas de câmbio
    """
    linha = 0 # Moeda que será convertida
    coluna = 0 # Posição da taxa de câmbio de destino
    final = 0 # Valor final obtido
    fator = 0 # Fator de conversão da moeda
    simbolo = '' # Símbolo da moeda
    match esc1: # Busca a linha da matriz
        case 1: # Real
            linha = 0
        case 2: # Dólar
            linha = 1
    
    match esc2: #Busca a coluna da matriz
        case 1: # Real
            coluna = 0
            simbolo = 'R$'
        case 2: # Dólar
            coluna = 1
            simbolo = 'U$'
    
    fator = cambios[linha][coluna] # O fator de conversão será a taxa de câmbio desejada
    final = fator * valor 
    return final, simbolo


#VARIÁVEIS
#Matriz que armazena as taxas de câmbio
#               R$    U$              
taxasCambio = [[1   , 5.47], # R$
               [0.18, 1   ]] # U$

cabecalho = 'CONVERSOR DE MOEDAS' # String padrão de cabeçalho
valor = 0 # Valor a ser convertido
resultado = 0 # Valor final
simbolo = '' # Simbolo da moeda (Variável auxiliar)
escolha1 = 0 # Seleciona a moeda que será convertida
escolha2 = 0 # Seleciona o fator de conversão
menu = ['R$ Real', 'U$ Dólar'] # Opções presentes no menu

#ENTRADA
imprimirCabecalho(cabecalho)
imprimirMenu(menu)
escolha1 = int(input('Digite a moeda a ser convertida: ')) # Percorre o menu
valor = float(input('Digite o valor: ')) #Armazena o valor que será convertido

#PROCESSAMENTO
imprimirCabecalho(cabecalho)
imprimirMenu(menu)
escolha2 = int(input(('Digite a moeda de destino: '))) # Armazena a moeda final

#SAÍDA
resultado, simbolo = converter(escolha1, escolha2, valor, taxasCambio) # Exibe a saída final
print(f'{simbolo}{resultado:.2f}') # Exibe a saída formatada