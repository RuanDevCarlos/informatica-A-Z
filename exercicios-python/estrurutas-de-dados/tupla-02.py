tupla = ('nome', 'idade', 'nascimento')
print('A variável tupla é:', tupla)

outratupla = 'id', 'idade', 'nascimento', 'nome'
print('A variável outratupla é:', outratupla)

print('\nA tupla {} tem como primeiro valor "{}"'.format(tupla,tupla[0]))
print('A tupla {} tem como segundo valor "{}"'.format(tupla,tupla[1]))
print('A tupla {} tem como último valor "{}"'.format(tupla,tupla[-1]))

print('\nIntervalo de uma tupla outratupla[:2] é', outratupla[:2]) # Serão lidos 2 valores, mas o valor [2] não será impresso
print('Intervalo de uma tupla outratupla[1:3] é', outratupla[1:3]) # Serão lidos 2 valores, começando do [1] até o [2], [0] e [3] não serão lidos
print('Intervalo de uma tupla outratupla[1:] é', outratupla[1:]) # Serão lidos todos os valores a partir de [1], ou seja [0] não será lido

''' Concatenação de Tuplas '''

X = (3, 5, 7)
Y = 1, 2, 4
Z = X + Y
print(f'\nA tupla Z {Z} é uma concatenação das tuplas X = {X} com Y = {Y}')