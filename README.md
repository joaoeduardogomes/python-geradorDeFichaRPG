### Project language: 🇧🇷

---

# Gerador de fichas 3D&T Alpha

Este é um gerador de fichas simples baseado no sistema de RPg 3D&T Alpha.

Aqui, consideramos o atributo Mente para ser usado no cálculo dos PMs (pontos de magia). Enquanto que o atributo Resistência é usado para calcular os PVs (pontos de vida) e PFs (pontos de fôlego).

## Entendendo os arquivos:

### 1º arquivo — numeros.py

    Aqui são gerados os valores que serão distribuídos entre os atributos.

1. Método `gera_valores` => randomiza os 6 valores a ser distribuídos entre os atributos.
   
   1. Quando o valor total a ser distribuído for menor do que 20, um atributo não pode ter mais do que 5 pontos.

2. Método `organiza_valores` => organiza os valores randomizados em ordem decrescente. 
   
   1. Isso é feito para pegar os valores mais altos e usá-los para os atribuir de acordo com a prioridade de cada classe. Ex: um guerreiro precisa ter um valor alto para Força, enquanto que um arqueiro precisa der um valor alto para PDF.

3. Método `embaralha_valores` => randomiza os três valores mais altos da lista. Permitindo que, assim, as fichas geradas não sejam tão parecidas.
   
   1. Dessa forma, é possível ter guerreiros que priorizam Força, enquanto que outro prioriza Armadura e um terceiro prioriza Resistência.

## 2º arquivo — classes.py

    Aqui são geradas fichas que distribuem os atributos de maneira adequada à classe selecionada.

1. Método `escolhe_classe` => recebe a escolha do usuário sobre qual ficha será gerada. Também permite que ele informe o valor total a ser distribuído. Se nada for inserido, será levado em conta o padrão (12).

2. Método `executa_classe` => recebe a escolha do usuário de classe e valor total a ser distribuído. Com base nesses parâmetros, irá executar o método da classe escolhida.

3. Método `guerreiro` => gera ficha de guerreiro.

4. Método `arqueiro` => gera ficha de arqueiro.

5. Método `mago` => gera ficha de mago.

6. Método `ladino` => gera ficha de ladino.

7. Método `capanga` => gera uma ficha de capanga que, a princípio, é mais fraco — a não ser que o usuário informe um valor quando perguntado.
   
   1. Um capanga é, basicamente, um inimigo genérico que o mestre irá selecionar para situações de combate.

8. Método `aleatorio` => gera uma ficha com os valores divididos aleatoriamente entre os atributos. Como nenhum atributo é priorizado, o mestre tem a liberdade de decidir o estilo de luta deste personagem com base no resultado gerado.

## 3º arquivo — dados.py

    É o arquivo responsável por exibir os dados da ficha de personagem randomizada.

1. Método `exibe_dados` => recebe os dados da ficha gerada e os exibe no terminal.

## 4º arquivo — entrada_usuario.py

 É o arquivo com o qual o usuário deve interagir (executar).

Ele vai chamar o **classes.py**, pegar os dados retornados e passá-los como parâmetro para o método` exibe_dados` do arquivo **dados.py**.

## Licença
![MIT license](https://img.shields.io/badge/License-MIT-%20?link=https%3A%2F%2Fchoosealicense.com%2Flicenses%2Fmit%2F)

---
Este projeto também foi feito em JavaScript: [link do projeto feito em JavaScript](https://github.com/joaoeduardogomes/JavaScript-geradorDeFichaRPG)
