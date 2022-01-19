from random import randint
from random import shuffle


def gera_valores(num = 12):

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

def organiza_valores():
    valores.sort(reverse=True)

def embaralha_valores():
    embaralha = valores [0:3] #serve pra pegar os 3 primeiros valores da lista 'valores' e embaralhar
    shuffle(embaralha) #Aqui embaralhamos os três elementos retirados
    print(embaralha)

    # Aqui eles são reatribuídos na lista de acordo com a ordem depois de embaralhados
    valores[0] = embaralha[0]
    valores[1] = embaralha[1]
    valores[2] = embaralha[2]

valores = [0, 0, 0, 0, 0, 0]


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