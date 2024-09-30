'''
if (condição)
    Bloco de instruções que serão executadas somente se a condição for verdadeira (true)

else:
    Bloco de instruções que serão executadas somente se a condição for falsa (false)

RETORNO DO FLUXO
'''

# CONDIÇÃO SIMPLES

idade = int(input('Dígite sua idade: '))
if (idade >= 18):
    print('Você é maior de idade!')
else:
    print('Você é menor de idade')
print(10*'=','Fim',10*'=')