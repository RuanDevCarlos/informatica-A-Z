""" RETORNO DE FUNÇÕES

    Uma função pode ter ou não retorno.

    Funções sem retorno executam as operações internamente e podem imprimir na tela o resultado.

    Por outro lado, caso tenha interesse em usar o resultado de uma função em outras operações, deve ser usado o comando return na função. Nesse caso, ao chamar a função ela deve ser atribuída a uma variável.
"""

#fatorial recursivo
def fat(x):
    resultado = 0
    if (x == 1 or x == 0):
        return 1
    else:
        return x * fat(x - 1)