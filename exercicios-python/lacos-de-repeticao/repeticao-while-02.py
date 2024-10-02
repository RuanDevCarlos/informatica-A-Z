'''
    A seguir um exemplo de algoritmo ilustrando uma aplicação prática do while, nele o usuário pode calcular a soma de 2 valores, o fatorial de um número ou multiplicar 2 valores
'''
from traceback import print_tb

opcao = 1
while opcao != 0:
    print(12*'#', 'MENU', 12*'#')
    print(''' 
        [0] para sair;
        [1] para somar;
        [2] para fatorar;
        [3] para multiplicar;\n
    ''')
    opcao = int(input('Escolha a opção: '))
    if (opcao == 0):
        print('BYE BYE!\n\n')
    elif (opcao == 1):
        a = int(input('Insíra o primeiro valor: '))
        b = int(input('Insira o segundo valor: '))
        print('O resultado de {} + {} é {}\n\n'.format(a,b,a+b))
    elif (opcao == 2):
        s = int(input('Dígite o valor de n: '))
        fator = 1
        i = 1
        for i in range(s):
            #print('n: ', s)
            #print('i: ', i)
            fator = fator + fator*i
        #i = i + 1
        print("\n\nO valor de \n %d! =\n\n" %s, fator)
    elif (opcao == 3):
        a = int(input('Insira o primeiro valor: '))
        b = int(input("Insira o segundo valor: "))
        print('Resultado de {} x {} = {}\n\n'.format(a,b,a*b))
    else:
        print(5*'*','OPÇÃO INVÁLIDA', 5*'*','\nTENTE NOVAMENTE\n')
print('\nFIM DO ALGORITMO\n')
