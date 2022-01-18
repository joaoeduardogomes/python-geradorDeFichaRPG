from random import randint
from time import sleep

def gera_atributos():
    global classes_exibicao
    classes_exibicao = ('[1] guerreiro', '[2] arqueiro', '[3] mago', '[4] ladino', '[5] capanga', '[6] aleatório')
    for cont in range (0, len(classes_exibicao)):
        print(classes_exibicao[cont].title())
    global escolha
    escolha = int(input("Escolha uma das classes (1 a 6): "))

    classes_execucao = {1: guerreiro(), 2: arqueiro(), 3: mago(), 4: ladino(), 5: capanga(), 6: aleatorio()}
    classes_execucao[escolha]

    valores_lista = [valores_guerreiro, valores_arqueiro, valores_mago, valores_ladino, valores_capanga, valores_aleatorio]
    valores = valores_lista[escolha - 1]

    global atributos
    atributos = dict(zip(atributos_lista, valores))

    print(f"\n Gerando os atributos para: {classes_exibicao[escolha - 1]}...\n")
    sleep(1)

def guerreiro():
    global valores_guerreiro
                #           FORÇA        HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE          PDF
    valores_guerreiro = [randint(2, 5), randint(0, 3), randint(2, 5), randint(1, 5), randint(0, 3), randint(0, 3)]
    
def arqueiro():
    global valores_arqueiro
                #           FORÇA        HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE          PDF
    valores_arqueiro = [randint(0, 3), randint(2, 5), randint(0, 3), randint(0, 4), randint(0, 4), randint(2, 5)]

def mago():
    global valores_mago
                #           FORÇA        HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE          PDF
    valores_mago = [randint(0, 3), randint(1, 5), randint(0, 3), randint(0, 3), randint(2, 5), randint(0, 4)]

def ladino():
    global valores_ladino
                #           FORÇA        HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE          PDF
    valores_ladino = [randint(0, 3), randint(3, 5), randint(0, 3), randint(1, 3), randint(1, 3), randint(1, 4)]

def capanga():
    global valores_capanga
                #           FORÇA        HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE          PDF
    valores_capanga = [randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2)]

def aleatorio():
    global valores_aleatorio
                #           FORÇA        HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE          PDF
    valores_aleatorio = [randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)]

def resultado():
    with open('ficha.txt', 'w') as f:
        print(f"Ficha de {classes_exibicao[escolha - 1]}: ", file=f)
        for k, v in atributos.items():
            print(f"{k.title():^14}: {v}", file=f)
        #print(atributos, file=f)
    f.close()


atributos_lista = ['força', 'habilidade', 'armadura', 'resistência', 'mente', 'poder de fogo']

gera_atributos()
#print(atributos)

for k, v in atributos.items():
    print(f"{k.title():^14}: {v}")

resultado()


#atributos = {'força': 0, 'habilidade': 0, 'armadura': 0, 'resistência': 0, 'mente': 0, 'poder de fogo': 0}