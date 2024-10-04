'''
    Podemos colocar variáveis dentro de uma posição de uma lista. Neste caso, a variável também pode ser uma lista, ou seja, uma lista de lista
'''

# Listas de Listas
print('\n\n\n')
print(50*'#')

people = [['João', 31],['Pedro', 25],['Ana', 31]]
print(f'Lista people {people}')
print(f'Lista people {people[1][0]}')

for i in people:
    print(f'Nome: {i[0]}, idade: {i[1]}')

print(50*'#')
print('\n\n\n')

print('\n\n\n')
print(50*'#')

aluno = ['Nome', '1 Bim', '2 Bim', '3 Bim', '4 Bim']
turma = []
turma.append(aluno[:])
del aluno
aluno = []

while True:
    print(50*'-')
    print('{:^50}'.format("MENU"))
    print(50*'-')
    print('[0] Sair\n[1] Adicionar Novo Aluno')
    op = int(input('Opção: '))
    if op == 0:
        break
    else:
        aluno.append(input('Nome: '))
        aluno.append(int(input('Nota 1° Bim: ')))
        aluno.append(int(input('Nota 2° Bim: ')))
        aluno.append(int(input('Nota 3° Bim: ')))
        aluno.append(int(input('Nota 4° Bim: ')))
        turma.append(aluno[:])

print('FORA')
for i in turma:
    print(i)
    #print(turma)

print(50*'#')
print('\n\n\n')