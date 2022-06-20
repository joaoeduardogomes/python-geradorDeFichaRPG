import numeros
from time import sleep

def escolhe_classe():
    '''
    -> Fornece ao usuário um menu de seleção de classe para gerar uma ficha de personagem. Ao final, chama a função "executa_classe" passando a escolha como parâmetro.
    '''
    num_escolha = int(input("""
    Escolha sua classe pelo número indicado:
    [1] = Guerreiro
    [2] = Arqueiro
    [3] = Mago
    [4] = Ladino
    [5] = Capanga
    [6] = Aleatório

    Sua escolha: """))

    return executa_classe(num_escolha)

def executa_classe(num_escolha):
    '''
    -> Executa o método da classe escolhida, fazendo a distribuição dos valores de maneira mais coerente.
    :param num_escolha: é o valor escolhido no método "escolhe_classe", que será usado no pattern matching.
    '''
    num = 12 # var de pontos a serem distribuídos (padrão: 12)
    embaralha_numeros = 2 # var de elementos a serem embaralhados (padrão: 2)

    atributos_nomes = {'força': 0, 'habilidade': 0, 'armadura': 0, 'resistência': 0, 'mente': 0, 'poder de fogo': 0, 'PV': 0, 'PF': 0, 'PM': 0} # define o dicionário com os atributos
    
    match num_escolha:
        case 1:
            escolha_classe = 'guerreiro' # indicação para o usuário da classe da ficha a ser gerada.
            atributos_valores = numeros.gera_valores(num = num, embaralha_numeros = 3) # aqui recebemos e guardamos os valores gerados em 'numeros.py' 
            atributos_classe = guerreiro(atributos_nomes, atributos_valores) # aqui retornamos o resultado do dicionário com os atributos e seus respectivos valores
        case 2:
            escolha_classe = 'arqueiro'
            atributos_valores = numeros.gera_valores(num = num, embaralha_numeros = embaralha_numeros)
            atributos_classe = arqueiro(atributos_nomes, atributos_valores)
        case 3:
            escolha_classe = 'mago'
            atributos_valores = numeros.gera_valores(num = num, embaralha_numeros = embaralha_numeros)
            atributos_classe = mago(atributos_nomes, atributos_valores)
        case 4:
            escolha_classe = 'ladino'
            atributos_valores = numeros.gera_valores(num = num, embaralha_numeros = embaralha_numeros)
            atributos_classe = ladino(atributos_nomes, atributos_valores)
        case 5:
            escolha_classe = 'capanga'
            atributos_valores = numeros.gera_valores(num = 6, embaralha_numeros = 6)
            atributos_classe = capanga(atributos_nomes, atributos_valores)
        case 6:
            escolha_classe = 'personagem aleatório'
            atributos_valores = numeros.gera_valores(num = num, embaralha_numeros = 6)
            atributos_classe = aleatorio(atributos_nomes, atributos_valores)
        case default:
            print("Opção inválida")
            
    print(f"\nGerando ficha de {escolha_classe.capitalize()}:")
    sleep(2)

    atributos_classe['PV'] = atributos_classe['resistência'] * 5
    atributos_classe['PF'] = atributos_classe['resistência'] * 5
    atributos_classe['PM'] = atributos_classe['mente'] * 5
    return atributos_classe

def guerreiro(atributos_nomes, atributos_valores):
    '''
    -> Gera uma ficha de classe Guerreiro.
    :param atributos_nomes: recupera o dicionário com os nomes dos atributos e os valores iniciais (0)
    :param atributos_valores: recupera os valores gerados no pattern matching do método "executa_classe" através do método importado "numeros.gera_valores"
    '''
    atributos_guerreiro = atributos_nomes.copy()

    atributos_guerreiro['força'] = atributos_valores[0]
    atributos_guerreiro['armadura'] = atributos_valores[1]
    atributos_guerreiro['resistência'] = atributos_valores[2]
    atributos_guerreiro['habilidade'] = atributos_valores[3]
    atributos_guerreiro['mente'] = atributos_valores[4]
    atributos_guerreiro['poder de fogo'] = atributos_valores[5]
    
    #print(atributos_guerreiro)
    return atributos_guerreiro


def arqueiro(atributos_nomes, atributos_valores):
    '''
    -> Gera uma ficha de classe Arqueiro.
    :param atributos_nomes: recupera o dicionário com os nomes dos atributos e os valores iniciais (0)
    :param atributos_valores: recupera os valores gerados no pattern matching do método "executa_classe" através do método importado "numeros.gera_valores"
    '''
    atributos_arqueiro = atributos_nomes.copy()

    atributos_arqueiro['poder de fogo'] = atributos_valores[0]
    atributos_arqueiro['habilidade'] = atributos_valores[1]
    atributos_arqueiro['armadura'] = atributos_valores[2]
    atributos_arqueiro['resistência'] = atributos_valores[3]
    atributos_arqueiro['mente'] = atributos_valores[4]
    atributos_arqueiro['força'] = atributos_valores[5]

    #print(atributos_arqueiro)
    return atributos_arqueiro


def mago(atributos_nomes, atributos_valores):
    '''
    -> Gera uma ficha de classe Mago.
    :param atributos_nomes: recupera o dicionário com os nomes dos atributos e os valores iniciais (0)
    :param atributos_valores: recupera os valores gerados no pattern matching do método "executa_classe" através do método importado "numeros.gera_valores"
    '''
    atributos_mago = atributos_nomes.copy()

    atributos_mago['mente'] = atributos_valores[0]
    atributos_mago['habilidade'] = atributos_valores[1]
    atributos_mago['resistência'] = atributos_valores[2]
    atributos_mago['armadura'] = atributos_valores[3]
    atributos_mago['força'] = atributos_valores[4]
    atributos_mago['poder de fogo'] = atributos_valores[5]

    #print(atributos_mago)
    return atributos_mago


def ladino(atributos_nomes, atributos_valores):
    '''
    -> Gera uma ficha de classe Ladino.
    :param atributos_nomes: recupera o dicionário com os nomes dos atributos e os valores iniciais (0)
    :param atributos_valores: recupera os valores gerados no pattern matching do método "executa_classe" através do método importado "numeros.gera_valores"
    '''
    atributos_ladino = atributos_nomes.copy()

    atributos_ladino['habilidade'] = atributos_valores[0]
    atributos_ladino['resistência'] = atributos_valores[1]
    atributos_ladino['força'] = atributos_valores[2]
    atributos_ladino['poder de fogo'] = atributos_valores[3]
    atributos_ladino['armadura'] = atributos_valores[4]
    atributos_ladino['mente'] = atributos_valores[5]

    #print(atributos_ladino)
    return atributos_ladino

def capanga(atributos_nomes, atributos_valores):
    '''
    -> Gera uma ficha de classe Capanga, que serve para fornecer inimigos de menor dificuldade.
    :param atributos_nomes: recupera o dicionário com os nomes dos atributos e os valores iniciais (0)
    :param atributos_valores: recupera os valores gerados no pattern matching do método "executa_classe" através do método importado "numeros.gera_valores"
    '''
    atributos_capanga = atributos_nomes.copy()
    atributos_capanga = dict(zip(atributos_capanga, atributos_valores))

    #print(atributos_capanga)
    return atributos_capanga

def aleatorio(atributos_nomes, atributos_valores):
    '''
    -> Gera uma ficha sem classe definida; sendo sua distribuição completamente aleatória.
    :param atributos_nomes: recupera o dicionário com os nomes dos atributos e os valores iniciais (0)
    :param atributos_valores: recupera os valores gerados no pattern matching do método "executa_classe" através do método importado "numeros.gera_valores"
    '''
    atributos_aleatorio = atributos_nomes.copy()
    atributos_aleatorio = dict(zip(atributos_aleatorio, atributos_valores))

    #print(atributos_aleatorio)
    return atributos_aleatorio



'''atributos_sorteados = escolhe_classe(int(input("""
    Escolha sua classe pelo número indicado:
    [1] = Guerreiro
    [2] = Arqueiro
    [3] = Mago
    [4] = Ladino
    [5] = Capanga
    [6] = Aleatório

    Sua escolha: """)))'''



'''atributos_sorteados = escolhe_classe()

for k, v in atributos_sorteados.items():
    if k in ('PV', 'PF', 'PM'):
        print(f"{k.upper()}: {v}")
    else:
        
        print(f"{k.title()}: {v}")
'''