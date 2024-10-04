import matplotlib.pyplot as plt
import numpy as np

# FUNÇÕES
def imprimirLinear(x, y):
    for i in range (99):
        plt.cla()
        plt.clf()

        x[i] = i + 1
        y[i] = i + 1
        #plt.cla()
        #plt.clf()
        plt.style.use('ggplot')
        plt.ion
        plt.plot(x,y)
        plt.pause(0.02)

    plt.ioff()
    plt.show()


def imprimirModular(x, y):
    for i in range (99):
        plt.cla()
        plt.clf()

        x[i] = i - 49
        if(x[i] < 0):
            y[i] = x[i] * (-1)
        else:
            y[i] = x[i]

        #plt.cla()
        #plt.clf()
        plt.style.use('ggplot')
        plt.ion
        plt.plot(x,y)
        plt.pause(0.02)

    plt.ioff()
    plt.show()


'''def imprimirGrafico(x, y):
    for i in range (99):
        plt.cla()
        plt.clf()

        x[i] = i + 1
        y[i] = np.random.randint(-50,50, 1)
        #plt.cla()
        #plt.clf()
        plt.style.use('ggplot')
        plt.ion
        plt.plot(x,y)
        plt.pause(0.02)

    plt.ioff()
    plt.show()'''


def imprimirMenu():
    print('''
[1] - Linear
[2] - Modular
''')
    

def imprimirGrafico(x, y):
    escolha = int(input('Qual das funções acima você quer? ')) # escolha no menu do usuário

    if(escolha == 1): # Linear
        imprimirLinear(x, y)
    elif(escolha == 2): # Modular
        imprimirModular(x, y)
    else:
        print('Parceiro, digite outro negócio aí namoral!')

    # match escolha:
    #     case 1: # Linear
    #         imprimirLinear(x, y)
    #     case 2: # Modular
    #         imprimirModular(x, y)
    #     case _:
    #         print('Muito burro!')
    

#VARIÁVEIS
x = np.arange(1, 100)
y = np.arange(1, 100)

#CORE
imprimirMenu()
imprimirGrafico(x, y)
