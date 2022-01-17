from random import randint

def gera_atributos():
    escolha = {1: guerreiro(), 2: arqueiro(), 3: mago(), 4: ladino()}
    escolha[int(input("""
    Escolha um tipo de personagem para randomizar: 
        [1] guerreiro
        [2] arqueiro
        [3] mago
        [4] ladino
        sua escolha: """))]
    global atributos
    atributos = dict(zip(atributos_lista, valores))

def guerreiro():
    global valores
        #           FORÇA      HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE           PDF
    valores = [randint(2, 5), randint(0, 3), randint(2, 5), randint(1, 5), randint(0, 3), randint(0, 3)]
    
def arqueiro():
    global valores
        #           FORÇA      HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE           PDF
    valores = [randint(0, 3), randint(2, 5), randint(0, 3), randint(0, 4), randint(0, 4), randint(2, 5)]

def mago():
    global valores
        #           FORÇA      HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE           PDF
    valores = [randint(0, 3), randint(1, 5), randint(0, 3), randint(0, 3), randint(2, 5), randint(0, 4)]

def ladino():
    global valores
        #           FORÇA      HABILIDADE      ARMADURA      RESISTÊNCIA       MENTE           PDF
    valores = [randint(0, 3), randint(3, 5), randint(0, 3), randint(1, 3), randint(1, 3), randint(1, 4)]


atributos_lista = ['força', 'habilidade', 'armadura', 'resistência', 'mente', 'poder de fogo']

gera_atributos()
print(atributos)




#atributos = {'força': 0, 'habilidade': 0, 'armadura': 0, 'resistência': 0, 'mente': 0, 'poder de fogo': 0}