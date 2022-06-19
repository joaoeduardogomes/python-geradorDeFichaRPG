from random import randint
from random import shuffle


def gera_valores(num = 12, embaralha_numeros = 3):
    '''
    -> gera valores para os atributos de uma ficha de rpg
    : param num: quantidade de pontos a serem distribuídos (12 por padrão)
    '''

    valores = [0, 0, 0, 0, 0, 0]

    maximo = num

    cont = 0

    while sum(valores) < maximo:

        rand = randint(0, 5)
        valores[cont] += rand

        cont += 1

        if cont > 5:
            cont = 0



        if sum(valores) > maximo:
            for i in range (0, len(valores)):
                if valores[i] == max(valores):
                    valores[i] -= (sum(valores) - maximo)

        if maximo <= 20:
        # se for menor ou igual a 20, um atributo não pode passar de 5
            for c in range (0, len(valores)):
                if max(valores) >  5:
                    valores[c] -= (max(valores) - 5)

    print(valores)
    organiza_valores(valores)
    print(valores)
    embaralha_valores(valores, embaralha_numeros)

    print(valores)

    print(max(valores))

    print(sum(valores))
    return valores


def organiza_valores(valores):
    '''
    -> organiza os valores gerados em ordem decrescente
    '''
    valores.sort(reverse=True)

def embaralha_valores(valores, embaralha_numeros):
    '''
    -> embaralha 'n' elementos para gerar personagens menos previsíveis em qual atributo recebe o maior valor
    : param embaralha_numeros: quantas posições da lista de valores gerados serão embaralhadas.
    '''
    embaralha = valores [0:embaralha_numeros] #serve pra pegar os 3 primeiros valores da lista 'valores' e embaralhar
    shuffle(embaralha) #Aqui embaralhamos os três elementos retirados

    # Aqui eles são reatribuídos na lista de acordo com a ordem depois de embaralhados
    for cont in range (0, embaralha_numeros):
        valores[cont] = embaralha[cont]


# Teste:
#gera_valores()

'''gera_valores()


print(valores)

print(max(valores))

print(sum(valores))

print()

organiza_valores()
print(valores)

embaralha_valores()

print(valores)'''

# lembrar de fazer o cálculo de PV, PF e PM