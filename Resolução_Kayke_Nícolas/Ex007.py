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

    while(True):
        notaAtual = float(input(f'Digite uma nota [ou -1 para encerrar]: '))
        if(notaAtual == -1): # Valor para encerrar
            break
        notas.append(notaAtual) # Adiciona a nota atual a lista de notas
    dict[nome] = notas # Adiciona o aluno com as notas


def escolher(opc, dict):
    match opc: # Compara as opções do menu
        case 1:
            util.imprimirDicionario(dict)
        case 2:
            adicionarAluno(dict)
        case 3:
            util.removerDicionario(dict)
        case _:
            print('Comando Inválido!')

    os.system('pause') # Pausa o terminal


#VARIÁVEIS
cabecalho = 'NOTAS DE ALUNOS' # Cabeçalho padrão
alunos = {} # Guarda as notas dos alunos
menu = ['Ver Alunos', 'Adicionar Aluno(a)', 'Remover Aluno(a)'] # Opções do menu
opc = 0 # Variável para escolher no menu

#PROCESSAMENTO
while(True):
    text.imprimirCabecalho(cabecalho)
    text.imprimirMenu(menu)
    opc = int(input('Escolha uma opção: '))
    escolher(opc, alunos)
