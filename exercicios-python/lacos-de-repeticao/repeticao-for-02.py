'''
    Função range

    A função range() pode ser empregada apresentando 1,2, ou 3 valores como parâmetros a fim de criar uma sequência de números partindo do valor 0 (zero), caso não seja especificado o valor inicial desejado, até o valor final (não incluso). Desse modo, usar a função range nas formas a seguir produzirá o mesmo resultado:

        range(5)

        range(0,5)

    A sintaxe da função range() é:

        range(valor inicial, valor final, salto)
'''

iteracao = int(input('Quantas repetições deseja realizar: '))
for i in range(iteracao):
    print('Está é a iteração: {}'.format(i))
    print(50*'=','\nFora do Laço\n',50*'=')