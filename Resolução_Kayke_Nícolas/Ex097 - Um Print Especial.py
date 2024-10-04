'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(text, char = '-', increment = 2):
    """
    Função que recebe um texto como parâmetro e imprime bordas a mercê do tamanho do argumento.
    Args:
        text (str): texto que será impresso
        char (str): caractere que será impresso nas bordas (Default = '-')
        increment (int): um leve incremento que terá nas bordas dos nomes
    """
    print(f'{char*(len(text)+increment)}') # imprime um caractere para cada letra no texto que será impresso + incremento
    print(text.center(len(text)+increment)) # imprime o texto no centro do tamanho da palavra + incremento
    print(f'{char*(len(text)+increment)}') # os caracteres podem variar ou não


escreva('Sem nada')
escreva('Mudando a borda para "~"', char='~')
escreva('Com incremento de 50', increment=50)
escreva('Testando com uma string muito grande, um incremento muito grande e um caractere aleatório', '=', 20)
