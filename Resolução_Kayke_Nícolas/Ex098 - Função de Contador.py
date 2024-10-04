'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

def contador(inicio, fim, passo):
    """
    Função que copia a execução do "for", realizando uma contagem.
    Args:
        inicio (int): número em que a contagem irá iniciar
        fim (int): número o qual a contagem terminará
        passo (int): de quanto em quanto a sequência seguirá
    """
    for i in range(inicio, fim+1, passo): # O término da função é incrementado para aparecer o último número
        print(f'{i} ', end='') # imprime os resultados na mesma linha


#VARIÁVEIS
inicio = 0 # determina onde a contagem inicia
fim = 0 # determina onde a contagem acaba
passo = 0 # determina de quanto em quanto a contagem vai ser realizada

#ENTRADA DE DADOS
inicio = int(input('Qual é o início da contagem? '))
fim = int(input('Qual número irá finalizar a contagem? '))
passo = int(input('De quanto em quanto a contagem será realizada? '))

#SAÍDA
contador(inicio, fim, passo) # resultado final da contagem
