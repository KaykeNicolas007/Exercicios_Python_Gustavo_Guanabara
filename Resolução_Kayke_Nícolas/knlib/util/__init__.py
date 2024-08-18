#Funções de utilidade
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
    key = str(input('Chave do elemento que será removido: '))
    dict.pop(key) # Rome o elemento do dicionário


def imprimirDicionario(dict):
    """
    Imprime elementos de um dicionário.
        :dict: Dicionário a ser impresso
    """
    for key, value in dict.items():
        print(f'Chave: {key}')
        print(f'Valor: {value}')
        print('')
