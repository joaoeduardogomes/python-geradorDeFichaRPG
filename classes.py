import numeros

def guerreiro():
    numeros.gera_valores()
    numeros.organiza_valores()

    global atributos_guerreiro
    atributos_guerreiro = atributos.copy()

    numeros.embaralha_valores(3) # embaralha os 3 primeiros valores (pos 0, 1 e 2)

    atributos_guerreiro['força'] = valores_importados[0]
    atributos_guerreiro['armadura'] = valores_importados[1]
    atributos_guerreiro['resistência'] = valores_importados[2]
    atributos_guerreiro['habilidade'] = valores_importados[3]
    atributos_guerreiro['mente'] = valores_importados[4]
    atributos_guerreiro['poder de fogo'] = valores_importados[5]
    
    print(atributos_guerreiro)


def arqueiro():
    numeros.gera_valores()
    numeros.organiza_valores()

    global atributos_arqueiro
    atributos_arqueiro = atributos.copy()

    numeros.embaralha_valores(2)

    atributos_arqueiro['poder de fogo'] = valores_importados[0]
    atributos_arqueiro['habilidade'] = valores_importados[1]
    atributos_arqueiro['armadura'] = valores_importados[2]
    atributos_arqueiro['resistência'] = valores_importados[3]
    atributos_arqueiro['mente'] = valores_importados[4]
    atributos_arqueiro['força'] = valores_importados[5]

    print(atributos_arqueiro)


def mago():
    numeros.gera_valores()
    numeros.organiza_valores()

    global atributos_mago
    atributos_mago = atributos.copy()

    numeros.embaralha_valores(2)

    atributos_mago['mente'] = valores_importados[0]
    atributos_mago['habilidade'] = valores_importados[1]
    atributos_mago['resistência'] = valores_importados[2]
    atributos_mago['armadura'] = valores_importados[3]
    atributos_mago['força'] = valores_importados[4]
    atributos_mago['poder de fogo'] = valores_importados[5]

    print(atributos_mago)


def ladino():
    numeros.gera_valores()
    numeros.organiza_valores()

    global atributos_ladino
    atributos_ladino = atributos.copy()

    numeros.embaralha_valores(2)

    atributos_ladino['habilidade'] = valores_importados[0]
    atributos_ladino['resistência'] = valores_importados[1]
    atributos_ladino['força'] = valores_importados[2]
    atributos_ladino['poder de fogo'] = valores_importados[3]
    atributos_ladino['armadura'] = valores_importados[4]
    atributos_ladino['mente'] = valores_importados[5]

    print(atributos_ladino)

def capanga():
    numeros.gera_valores(6)
    numeros.organiza_valores()

    global atributos_capanga

    numeros.embaralha_valores(6)

    atributos_capanga = dict(zip(atributos, valores_importados))

    print(atributos_capanga)


def aleatorio():
    numeros.gera_valores()
    numeros.organiza_valores()

    global atributos_aleatorio

    numeros.embaralha_valores(6)

    atributos_aleatorio = dict(zip(atributos, valores_importados))

    print(atributos_aleatorio)


atributos = {'força': 0, 'habilidade': 0, 'armadura': 0, 'resistência': 0, 'mente': 0, 'poder de fogo': 0}

#valores_importados = numeros.valores
'''valores_guerreiro = numeros.valores
print(valores_guerreiro)

numeros.gera_valores()
print(valores_guerreiro)

numeros.organiza_valores()
print(valores_guerreiro)

numeros.embaralha_valores(4)
print(valores_guerreiro)

print(max(valores_guerreiro))
print(sum(valores_guerreiro))'''

valores_importados = numeros.valores
#valores_guerreiro = numeros.valores


guerreiro() # O papel das classes é só mudar os valores embaralhados e a atribuição no dicionário
arqueiro()
mago()
ladino()
capanga()
aleatorio()








