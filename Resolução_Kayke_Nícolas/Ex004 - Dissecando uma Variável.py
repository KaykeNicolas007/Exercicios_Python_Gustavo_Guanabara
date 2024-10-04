'''Ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele.'''

algo = input('Digite qualquer coisa: ')
print(f'''O tipo primitivo desse valor é: {type(algo)}
Tem só espaços? {algo.isspace()}
É um número? {algo.isnumeric()}
Tem só letras? {algo.isalpha()}
É alfanumérico? {algo.isalnum()}
É feito de letras maiúsculas? {algo.isupper()}
Ou é de minúsculas? {algo.islower()}
Talvez seja capitalizada? {algo.istitle()}''')
