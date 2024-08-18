#Biblioteca pessoal para funções de texto frequentemente utilizadas

import os

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