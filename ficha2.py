from random import randint

#valores = {'for': 0, 'hab': 0, 'arm': 0, 'res': 0, 'men': 0, 'pdf': 0}
valores = [0, 0, 0, 0, 0, 0]

maximo = 12

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

    for c in range (0, len(valores)):
        if max(valores) >  5:
            valores[c] -= (max(valores) - 5)


print(valores)

print(max(valores))

print(sum(valores))