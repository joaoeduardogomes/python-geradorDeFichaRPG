from random import randint
from time import sleep
import atributos





atributos_lista = ['força', 'habilidade', 'armadura', 'resistência', 'mente', 'poder de fogo']

lista = atributos.valores

#testando:
atributos.gera_valores()

print(lista)

atributos.organiza_valores()

print(lista)

atributos.embaralha_valores()

print(lista)

print(sum(lista))
print(max(lista))

atributos = dict(zip(atributos_lista, lista))
print(atributos)