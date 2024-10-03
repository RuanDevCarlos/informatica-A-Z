'''
    TUPLAS

    Tuplas são estruturas de dados que uma vez criadas não podem ser alteradas, ou seja, ela é IMUTÁVEL em tempo de execução

    Ao atribuir valores a uma variável, que se encontra entre parênteses ou não, estamos definindo uma tupla, a diferença é sutil em relação as outras estruturas de dados compostas
'''

tupla = ('nome', 'idade', 'nascimento')
print(tupla)

outratupla = 'id', 'idade', 'nascimento', 'nome'
print(outratupla)

print(tupla[0]) # Acessa o primeiro elemento da tupla

print(outratupla[1]) # Acessa o segundo elemento da tupla

print(outratupla[-1]) # Acessa o último elemento da tupla e -2 acessaria o penúltimo