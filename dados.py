def exporta():
    with open('ficha.txt', 'w') as f:
        print(f"Ficha de {classes_exibicao[escolha - 1]}: ", file=f)
        for k, v in atributos.items():
            print(f"{k.title():^14}: {v}", file=f)
        #print(atributos, file=f)
    f.close()