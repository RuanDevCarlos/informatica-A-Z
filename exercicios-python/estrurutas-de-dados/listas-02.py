lista = ['nome', 'idade', 'nascimento']
print(f'Criação da lista -> {lista}')

# Alterando o valor de itens da lista
lista[0] = 'João Paulo Colet Orso'
lista[1] = '23/01/1989'
print(f'\nApós a alteração a nova lista é {lista}')

# Uma lista pode ter valores adicionados a sua estrutura
# lista[3] = ['novo'] | Porém desse modo não funciona, assim como nas tuplas

# Para adicionar valores ao final de uma lista usamos o metodo append
lista.append('Profissão') # A string profissão será adicionada ao final da lista
print(f'Após a alteração a nova lista é {lista}')

# Para adicionar valores em uma determinada posição de uma lista usamos o metodo insert
lista.insert(0, '0001') # A string 0001 será adicionada ao começo da lista
print(f'Após a alteração a nova lista é {lista}')

# Para eliminar elementos de uma lista podemos usar del ou usar o metodo pop para remover indicando o índice desejado
del lista[0] # O elemento na posição [0] será removido
print(f'Após del a nova lista é {lista}')
lista.pop(3) # Remove o elemento no índice [3]
print(f'Após pop a nova lista é {lista}')

# Outra forma de remover valores de uma lista, é usando o metodo remove, neste caso devemos indicar o conteúdo que desejamos remover
lista.remove('23/01/1989') # Assim é possível remover um elemento sem saber seu índice
print(f'Após remove a nova lista é {lista}')




