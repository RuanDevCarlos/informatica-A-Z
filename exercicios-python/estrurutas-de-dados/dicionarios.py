""" Dicionários
    São estruturas de dados compostas que utilizam índices descritivos para indicar uma posição, ao invés de apenas números como no caso das Lista e Tuplas

    Um dicionário pode ser declarado com a função dict() ou com o uso de {} chaves, conforme o exemplo de código a seguir.
"""

dicionario = dict()
dicionario = {'nome':'João Paulo Colet Orso', 'idade':31}
print(f'Nome é: {dicionario['nome']}')
print(f'Idade é: {dicionario['idade']}')

# O código acima cria um dicionário chamado dicionario com 2 dados, sendo nome o índice para o primeiro registro que contém 'João Paulo Colet Orso' e idade o índice para o segundo registro que contém '31'.

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

# O método keys() retorna quais são os índices presentes no dicionário
# O método values() retorna os valores armazenados no dicionário, perceba qua tratam-se internamente de listas, que podem ser identificadas pelo uso de colchetes
# O método items() retorna tanto os valores como os índices do dicionário

for p, r in dicionario.items():
    print(f'{p} = {r}')

# A importância desses métodos é para manipular melhor a estrutura de dados como o for da linha 13 e 14 que possui forma própria que permite usar duas variáveis de controle vinculadas aos itens do dicionário. É como se analisasse duas listas simultaneamênte, de modo que pega a primeira posição de cada, depois a segunda e assim por diante.

dicionario['idade'] = 33
print(f'Nome é: {dicionario['nome']}')
print(f'Idade é: {dicionario['idade']}')

# Alterando valores

dicionario['altura'] = 1.81
print(dicionario)
for p, r in dicionario.items():
    print(f'{p} = {r}')

# Na linha 33 temos a atribuição de um valor float 1.81 a um índice que não existe no dicionário. Isso faz com que ele seja criado na última posição do dicionário

