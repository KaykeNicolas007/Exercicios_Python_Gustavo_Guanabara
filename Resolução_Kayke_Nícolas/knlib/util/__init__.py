#Funções de utilidade
def lerFloat(prompt=''):
    """
    Comando que lê apenas um número flutuante e nada mais.
        :prompt: Linha de texto com o comando para o usuário
    """
    while(True):
        try:
            n = float(input(prompt))
        except ValueError:
            print('Erro! Digite um NÚMERO FLUTUANTE!\n')
            continue
        else:
            return n


def lerInt(prompt=''):
    """
    Comando que lê apenas um número inteiro e nada mais.
        :prompt: Linha de texto com o comando para o usuário
    """
    while(True):
        try:
            n = int(input(prompt))
        except ValueError:
            print('Erro! Digite um NÚMERO INTEIRO!\n')
            continue
        else:
            return n


def calcularMedia(nums):
    soma = 0 # Soma dos números
    media = 0 # Resultado final da média
    for num in nums:
        soma += num # Soma todos os números

    media = soma/len(nums) # Calcula a média
    return media


def removerDicionario(dict):
    """
    Remove a ocorrência de um elemento de um dicionário.
        :dict: Dicionário contendo o elemento desejado
    """
    if(len(dict) == 0):
        print('Dicionário vazio! Não há o que remover!')
    else:
        try:
            key = str(input('Chave do elemento que será removido: '))
            dict.pop(key) # Rome o elemento do dicionário
        except KeyError:
            print('Nome não existente!')


def imprimirDicionario(dict):
    """
    Imprime elementos de um dicionário.
        :dict: Dicionário a ser impresso
    """
    for key, value in dict.items():
        print(f'Chave: {key}')
        print(f'Valor: {value}')
        print('')
