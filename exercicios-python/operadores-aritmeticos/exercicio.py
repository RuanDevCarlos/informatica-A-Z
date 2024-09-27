#operadores Aritméticos

print('='*50)
a = int(input('Dígite o primeiro valor: '))
b = int(input('Dígite o segundo valor: '))

print('Operação Soma, temos a={} + b={}, assim, {} + {} = {}'.format(a,b,a,b,a+b))

print('Operação Subtração, temos a={} - b={}, assim, {} - {} = {}'.format(a,b,a,b,a-b))

print('Operação Multiplicação, temos a={} x b={}, assim, {} * {} = {}'.format(a,b,a,b,a*b))

print('Operação Divisão, temos a={} / b={}, assim, {} / {} = {}'.format(a,b,a,b,a/b))

print('Operação Potência, temos a={} ** b={}, assim, {} ** {} = {}'.format(a,b,a,b,a**b))

print('Operação Divisão Inteira, temos a={} // b={}, assim, {} // {} = {}'.format(a,b,a,b,a//b))

print('Operação Resto da Divisão Inteira, temos a={} MOD b={}, assim, {} % {} = {}'.format(a,b,a,b,a%b))

#FORMATANDO A SAÍDA

x = 2/3

print('Divisão de 2/3 é ponto flutuante = {}'.format(x))
print('Divisão de 2/3 com apenas 3 casas decimais = {:.3f}'.format(x))