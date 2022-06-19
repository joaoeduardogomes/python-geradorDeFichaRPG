import numeros

def escolhe_classe(num_escolha):
    escolha_classe = ''
    num = 12
    embaralha_numeros = 2
    global atributo_valores #aqui inicializamos a variável que vai guardar os valores de 'numeros.py'
    
    match num_escolha:
        case num_escolha if num_escolha == 1:
            print("Escolha: guerreiro")
            atributo_valores = numeros.gera_valores(num = num, embaralha_numeros = 3) # aqui recebemos e guardamos os valores gerados em 'numeros.py' 
            return guerreiro() # aqui retornamos o resultado do dicionário com os atributos e seus respectivos valores
        case num_escolha if num_escolha == 2:
            print("Escolha: arqueiro")
            atributo_valores = numeros.gera_valores(num = num, embaralha_numeros = embaralha_numeros)
            return arqueiro()
        case num_escolha if num_escolha == 3:
            print("Escolha: mago")
            atributo_valores = numeros.gera_valores(num = num, embaralha_numeros = embaralha_numeros)
            return mago()
        case num_escolha if num_escolha == 4:
            print("Escolha: ladino")
            atributo_valores = numeros.gera_valores(num = num, embaralha_numeros = embaralha_numeros)
            return ladino()
        case num_escolha if num_escolha == 5:
            print("Escolha: capanga")
            atributo_valores = numeros.gera_valores(num = 6, embaralha_numeros = 6)
            return capanga()
        case num_escolha if num_escolha == 6:
            print("Escolha: aleatório")
            atributo_valores = numeros.gera_valores(num = num, embaralha_numeros = 6)
            return aleatorio()
        case default:
            print("Opção inválida")
            
    #escolha_classe = {1: guerreiro(), 2: arqueiro(), 3: mago(), 4: ladino(), 5: capanga(), 6: aleatorio()}

def guerreiro():
    atributos_guerreiro = atributos.copy()

    atributos_guerreiro['força'] = atributo_valores[0]
    atributos_guerreiro['armadura'] = atributo_valores[1]
    atributos_guerreiro['resistência'] = atributo_valores[2]
    atributos_guerreiro['habilidade'] = atributo_valores[3]
    atributos_guerreiro['mente'] = atributo_valores[4]
    atributos_guerreiro['poder de fogo'] = atributo_valores[5]
    
    print(atributos_guerreiro)
    return atributos_guerreiro


def arqueiro():
    atributos_arqueiro = atributos.copy()

    atributos_arqueiro['poder de fogo'] = atributo_valores[0]
    atributos_arqueiro['habilidade'] = atributo_valores[1]
    atributos_arqueiro['armadura'] = atributo_valores[2]
    atributos_arqueiro['resistência'] = atributo_valores[3]
    atributos_arqueiro['mente'] = atributo_valores[4]
    atributos_arqueiro['força'] = atributo_valores[5]

    print(atributos_arqueiro)
    return atributos_arqueiro


def mago():
    atributos_mago = atributos.copy()

    atributos_mago['mente'] = atributo_valores[0]
    atributos_mago['habilidade'] = atributo_valores[1]
    atributos_mago['resistência'] = atributo_valores[2]
    atributos_mago['armadura'] = atributo_valores[3]
    atributos_mago['força'] = atributo_valores[4]
    atributos_mago['poder de fogo'] = atributo_valores[5]

    print(atributos_mago)
    return atributos_mago


def ladino():
    atributos_ladino = atributos.copy()

    atributos_ladino['habilidade'] = atributo_valores[0]
    atributos_ladino['resistência'] = atributo_valores[1]
    atributos_ladino['força'] = atributo_valores[2]
    atributos_ladino['poder de fogo'] = atributo_valores[3]
    atributos_ladino['armadura'] = atributo_valores[4]
    atributos_ladino['mente'] = atributo_valores[5]

    print(atributos_ladino)
    return atributos_ladino

def capanga():
    atributos_capanga = atributos.copy()
    atributos_capanga = dict(zip(atributos_capanga, atributo_valores))

    print(atributos_capanga)
    return atributos_capanga

def aleatorio():
    atributos_aleatorio = atributos.copy()
    atributos_aleatorio = dict(zip(atributos_aleatorio, atributo_valores))

    print(atributos_aleatorio)
    return atributos_aleatorio


atributos = {'força': 0, 'habilidade': 0, 'armadura': 0, 'resistência': 0, 'mente': 0, 'poder de fogo': 0}



# Importação da lista de 6 espaços
#valores_importados = numeros.valores


atributos_sorteados = escolhe_classe(int(input("""
    Escolha sua classe pelo número indicado:
    [1] = Guerreiro
    [2] = Arqueiro
    [3] = Mago
    [4] = Ladino
    [5] = Capanga
    [6] = Aleatório

    Sua escolha: """)))

for k, v in atributos_sorteados.items():
    print(f"{k.title()}: {v}")











