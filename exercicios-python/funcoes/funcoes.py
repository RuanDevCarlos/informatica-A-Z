"""
    Funções são estruturas que realizam uma tarefa executada várias vezes.

    Algumas funções já foram empregadas, como input ou mesmo o print, elas são chamadas de funções built-in, isto é, incorporadas à linguagem.

    É possível passar parâmetros em outra ordem desde que sejam identificados.

    Python permite empacotar parâmetros.

    Python usa a passagem de parâmetros por referência.

    Para usar parâmetros opcionais, basta zerar os parâmetros dentro da função.

    Uma função pode chamar outra função.

    Uma vez que a linguagem Python é interpretada, torna-se essencial declarar/definir as funções antes que elas sejam executadas/chamadas no código. Uma prática habitual é definir as funções no começo do arquivo main, antes do início do bloco principal de código.

    Quando o número de funções é muito grande, ou mesmo constituem funções que possam ser reutilizadas em outras estruturas de código, é comum colocá-las em outros arquivos, criando as chamadas bibliotecas. Assim como é importante declarar uma função antes de seu uso, é necessário importar uma biblioteca, ou pelo menos a parte que será usada, antes de seu uso.
"""

def Menu(text,tam):
    print(tam*'=')
    x = (tam-len(text))/2
    print(int(x)*' ', text.upper())
    print(tam*'=')

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
#fib(12000)

Menu('opções',50)
Menu(tam=30, text='Menu do Sistema') # É possível passar os parâmetros em outra ordem desde que sejam identificados 