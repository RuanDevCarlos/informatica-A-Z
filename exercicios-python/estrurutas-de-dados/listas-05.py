'''
    Fique atento ao atribuir uma lista a outra variável, pois corre-se o risco de criar um ponteiro para a mesma lista, isto é, ter 2 nomes para a mesma lista. Para copiar o conteúdo de uma lista para uma outra variável, deve-se descrever todo o conteúdo da lista, veja o exemplo a seguir:
'''

# Criar Cópias de Lista

# Cuidado
comprar = ['banana', 'Maçã', 'Batata', 'Limão']
comp = comprar # Ao fazer uma lista receber outra, na verdade foi criado um ponteiro que aponta para a mesma lista
print(f'Lista Comprar {comprar}')
print(f'Lista Comp {comp}')

comp.append('Melão')
print(f'Lista Comprar {comprar}')
print(f'Lista Comp {comp}')

comprar.append('Jaca')
print(f'Lista Comprar {comprar}')
print(f'Lista Comp {comp}')

# Para criar uma lista podemos criar outra forçando a varredura da primeira
foi = comp[:]

foi.append('Chocolate')
print(f'Lista Comprar {comprar}')
print(f'Lista Comp {comp}')
print(f'Lista Foi {foi}')