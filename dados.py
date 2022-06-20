def exibe_dados(atributos_sorteados):
    #soma = sum(atributos_sorteados.values())
    #print(f"Total de pontos distribuídos: {soma}")

    for k, v in atributos_sorteados.items():
        if k in ('PV', 'PF', 'PM'):
            print(f"{k.upper()}: {v}")
        else:
            
            print(f"{k.title()}: {v}")


'''def exporta_dados():
    with open('ficha.txt', 'w') as f:
        print(f"Ficha de {classes_exibicao[escolha - 1]}: ", file=f)
        for k, v in atributos.items():
            print(f"{k.title():^14}: {v}", file=f)
        #print(atributos, file=f)
    f.close()'''