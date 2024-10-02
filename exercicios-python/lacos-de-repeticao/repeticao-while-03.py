'''
    Ao usar o comando while é possível forçar a sua execução sem utilizar uma variável de controle. Contudo, para encerrar o laço de repetição o comando break se faz necessário, do contrário o algoritmo entra no chamado loop infinito.
'''

while True:
    print(12*'#', 'MENU', 12*'#')
    print("""
        [0] PARA SAIR;
        [1] PARA CONTINUAR;
    """)
    print(31*'#')
    opcao = int(input('Escolha uma opção: '))
    if (opcao == 0):
        print('SAIR selecionado')
        break
    elif (opcao == 1):
        print('Repetir laço WHILE')
    else:
        print(5*'*', 'OPÇÃO INVÁLIDA', 5*'*', '\nTENTE NOVAMENTE\n')
print('FIM DO ALGORITMO')
