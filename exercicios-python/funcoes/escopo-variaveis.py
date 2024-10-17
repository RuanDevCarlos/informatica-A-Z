""" ESCOPO DE VARIÁVEIS

    Quando a variável não for definida localmente em uma função, ela assume valor local.

    Para forçar a função a usar uma variável do código main (ou seja, de modo global), deve ser utilizado o comando global dentro da função antes de empregá-la
"""

def teste():
    # global k
    k = 1111
    print(f'Variável K vale {k} dentro da função')

k = 10
print(f'Variável K vale {k} no Main')

teste()
print(f'Variável k vale {k} no Main depois do teste')