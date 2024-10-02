'''
    Enquanto (while)

    Há momento em que não temos um número definido de iterações, para isso usa-se o comando while.

    Um laço de repetição while irá repetir o bloco de comandos até que a condição apresentada se torne falsa
'''

opcao = 1

while opcao != 0:
    print(12*'#', 'MENU', 12*'#')
    print("""
        [0] para sair;
        [1] para continuar;
    """)
    print(31*'#')
    opcao = int(input('Dígite sua opção: '))
    if (opcao == 0):
        print('Sair Selecionado!\n\n')
    elif (opcao == 1):
        print('Repetir laço WHILE')
    else:
        print(5*'*', 'Opção Inválida', 5*'*', '\nTente Novamente\n')

print('\nFIM DO ALGORITMO\n')