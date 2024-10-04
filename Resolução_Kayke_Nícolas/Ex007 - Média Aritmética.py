'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

import os
from knlib import text, util

#FUNÇÕES
def adicionarAluno(dict):
    """
    Adiciona um novo aluno e suas notas ao dicionário
        :dict: O dicionário de alunos
    """
    nome = str(input('Nome do aluno(a): '))
    notas = [] # Todas as notas do aluno
    notaAtual = 0 # Nota do aluno
    primeiraNota = True # Se é ou não a primeira nota a ser digitada

    while(notaAtual != -1 or primeiraNota):
        notaAtual = util.lerFloat(f'Digite uma nota [ou -1 para encerrar]: ')
        if(notaAtual == -1): # Valor para encerrar
            if(primeiraNota): # Força o usuário a digitar a primeira nota
                print('Você deve digitar ao menos uma nota!\n')
        else:
            notas.append(notaAtual) # Adiciona a nota atual a lista de notas
            primeiraNota = False # O próximo elemento já não é mais a primeira nota
    dict[nome] = notas # Adiciona o aluno com as notas


def imprimirDicionario(dict):
    """
    Imprime elementos de um dicionário.
        :dict: Dicionário a ser impresso
    """
    if(len(dict) == 0):
        print('Dicionário vazio! Não há o que imprimir!')
    else:
        for key, value in dict.items():
            print(f'Chave: {key}')
            print(f'Valor: {value}')
            print(f'Média: {util.calcularMedia(value):.2f}')
            print('')


def escolher(opc, dict):
    """
    Realiza as ações do menu.
        :opc: Opção definida pelo usuário
        :dict: Dicionário a ser utilizado para muitas execuções
    """
    match opc: # Compara as opções do menu
        case 1:
            imprimirDicionario(dict)
        case 2:
            adicionarAluno(dict)
        case 3:
            util.removerDicionario(dict)
        case _:
            print('Comando Inválido!')

    print('')
    os.system('pause') # Pausa o terminal


#VARIÁVEIS
cabecalho = 'NOTAS DE ALUNOS' # Cabeçalho padrão
alunos = {} # Guarda as notas dos alunos
menu = ['Ver Alunos', 'Adicionar Aluno(a)', 'Remover Aluno(a)', 'Sair'] # Opções do menu
opc = 0 # Variável para escolher no menu

#PROCESSAMENTO
while(True):
    text.imprimirCabecalho(cabecalho)
    text.imprimirMenu(menu)
    opc = util.lerInt('Escolha uma opção: ')
    if(opc == 4): # Comando de sair
        break
    
    escolher(opc, alunos)
