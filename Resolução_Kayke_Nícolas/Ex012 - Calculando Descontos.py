'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

def calcularDesconto(preco, taxa):
    """
    Função que calcula o desconto a ser colocado encima de um produto.
    Args:
        preco (float): preço inicial do produto
        taxa (float): taxa de desconto sobre o produto (em porcentagem)
    
    Returns:
        novoPreco (float): um novo preço com desconto
    """
    return preco * ((100-taxa)/100)


# VARIÁVEIS
preco = 0 # preço do produto que será inserido
novoPreco = 0 # preço final após desconto
desconto = 5 # porcentagem do desconto que será aplicado

# ENTRADA DE DADOS
preco = float(input('Informe o preço do produto desejado: '))

# PROCESSAMENTO
novoPreco = calcularDesconto(preco, desconto)

# SAÍDA
print(f'O preço inicial do produto é R${preco:.2f}. Com {desconto}% de desconto, temos o valor final de R${novoPreco:.2f}')
