from ctypes import Structure
import numeros

def escolhe_classe(escolha):
    match escolha:
        case escolha if escolha == 1:
            print("Escolha: guerreiro")
            guerreiro()
        case escolha if escolha == 2:
            print("Escolha: arqueiro")
            arqueiro()
        case escolha if escolha == 3:
            print("Escolha: mago")
            mago()
        case escolha if escolha == 4:
            print("Escolha: ladino")
            ladino()
        case escolha if escolha == 5:
            print("Escolha: capanga")
            capanga()
        case escolha if escolha == 6:
            print("Escolha: aleatório")
            aleatorio()
        case default:
            print("Opção inválida")

    #escolha_classe = {1: guerreiro(), 2: arqueiro(), 3: mago(), 4: ladino(), 5: capanga(), 6: aleatorio()}

def guerreiro():
    global atributos_guerreiro
    atributos_guerreiro = atributos.copy()


    atributos_guerreiro['força'] = valores_importados[0]
    atributos_guerreiro['armadura'] = valores_importados[1]
    atributos_guerreiro['resistência'] = valores_importados[2]
    atributos_guerreiro['habilidade'] = valores_importados[3]
    atributos_guerreiro['mente'] = valores_importados[4]
    atributos_guerreiro['poder de fogo'] = valores_importados[5]
    
    print(atributos_guerreiro)


def arqueiro():
    global atributos_arqueiro
    atributos_arqueiro = atributos.copy()


    atributos_arqueiro['poder de fogo'] = valores_importados[0]
    atributos_arqueiro['habilidade'] = valores_importados[1]
    atributos_arqueiro['armadura'] = valores_importados[2]
    atributos_arqueiro['resistência'] = valores_importados[3]
    atributos_arqueiro['mente'] = valores_importados[4]
    atributos_arqueiro['força'] = valores_importados[5]

    print(atributos_arqueiro)


def mago():
    global atributos_mago
    atributos_mago = atributos.copy()


    atributos_mago['mente'] = valores_importados[0]
    atributos_mago['habilidade'] = valores_importados[1]
    atributos_mago['resistência'] = valores_importados[2]
    atributos_mago['armadura'] = valores_importados[3]
    atributos_mago['força'] = valores_importados[4]
    atributos_mago['poder de fogo'] = valores_importados[5]

    print(atributos_mago)


def ladino():
    global atributos_ladino
    atributos_ladino = atributos.copy()


    atributos_ladino['habilidade'] = valores_importados[0]
    atributos_ladino['resistência'] = valores_importados[1]
    atributos_ladino['força'] = valores_importados[2]
    atributos_ladino['poder de fogo'] = valores_importados[3]
    atributos_ladino['armadura'] = valores_importados[4]
    atributos_ladino['mente'] = valores_importados[5]

    print(atributos_ladino)

def capanga():
    global atributos_capanga


    atributos_capanga = dict(zip(atributos, valores_importados))

    print(atributos_capanga)


def aleatorio():
    global atributos_aleatorio


    atributos_aleatorio = dict(zip(atributos, valores_importados))

    print(atributos_aleatorio)


atributos = {'força': 0, 'habilidade': 0, 'armadura': 0, 'resistência': 0, 'mente': 0, 'poder de fogo': 0}



# Importação da lista de 6 espaços
#valores_importados = numeros.valores




valores_importados = numeros.gera_valores()


escolhe_classe(int(input("""
    Escolha sua classe pelo número indicado:
    [1] = Guerreiro
    [2] = Arqueiro
    [3] = Mago
    [4] = Ladino
    [5] = Capanga
    [6] = Aleatório

    Sua escolha: """)))







#guerreiro() # O papel das classes é só mudar os valores embaralhados e a atribuição no dicionário










