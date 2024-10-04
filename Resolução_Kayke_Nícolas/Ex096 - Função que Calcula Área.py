'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno'''

def area(base, alt):
    """
    Função que calcula a área de um quadrilátero
    Args:
        base (float): Base do quadrilátero
        alt (float): Altura do quadrilátero
    
    Returns:
        base * alt (float)
    """
    return base * alt # A área é calculada como base * altura


#VARIÁVEIS
largura = 0 # Largura do terreno
comprimento = 0 # Comprimento do terreno

#ENTRADA DE DADOS
print('Vamos calcular a área do terreno que você comprou!!!') # Introdução
largura = int(input('Informe a largura do terreno (em metros): ')) # Prompt
comprimento = int(input('Informe o comprimento do terreno (em metros): ')) # Prompt

#SAÍDA
print(f'A área total do terreno é: {area(largura, comprimento)}m')
