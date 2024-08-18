'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

import os
from knlib import text, util

#FUNÇÕES
def imprimirLista(lista):
    """
    Imprime uma lista.
        :lista: Lista a ser impressa
    """
    for item in lista:
        print(f'{item}, ', flush=True)


def imprimirDicionario(dict):
    """
    Imprime os alunos e suas notas na tela.
        :dict: Dicionário de alunos a ser impresso
    """
    for item, keyArray in dict.items():
        print(f'{item} : {imprimirLista(keyArray)}')



def adicionarAluno(dict):
    nome = str(input('Digite o nome do aluno: '))
    notas = [] # Array de notas
    notaAtual = 0 # Nota atual do aluno

    #Pega as notas do aluno
    while(True):
        notaAtual = (float(input('Digite uma nota do aluno [ou 999 parar encerrar]: ')))
        if(notaAtual == 999):
            break
        notas.append(notaAtual) # Adiciona uma nota
    dict[nome] = notas # Adiciona as notas


def escolher(opc, dict):
    """
    Realiza alguma ação com o menu.
        :opc: Opção escolhida pelo usuário
        :dict: Dicionário de alunos
    """
    match opc:
        case 1:
            imprimirDicionario(dict)
            os.system('pause')
        case 2:
            adicionarAluno(dict)


#VARIÁVEIS
cabecalho = 'CÁLCULO DE MÉDIAS' # Nome padrão do cabeçalho
menu = ['Ver Alunos', 'Adicionar Aluno', 'Sair'] # Menu de opções
alunos = {'Teste' : [1.8]} #Guarda informações dos alunos e das notas
media = 0 # Média final
opc = 0 # Armazena as opções de escolha do usuário

while(True):
    #ENTRADA
    text.imprimirCabecalho(cabecalho)
    text.imprimirMenu(menu)
    opc = int(input('Digite um número: '))

    if(opc == 3):
        break

    escolher(opc, alunos)
