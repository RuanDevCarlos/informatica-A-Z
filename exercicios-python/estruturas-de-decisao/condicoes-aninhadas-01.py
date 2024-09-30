''' CONDIÇÕES ANINHADAS
    Também chamadas de condições compostas, presentes em outras linguagens com SWITHC usamos o elif:
'''

# CONDIÇÃO ANINHADA

nota = int(input('Dígite a nota do aluno: '))
if (nota >= 70):
    print('\nParabéns!\n Você foi APROVADO com nota {}'.format(nota))
else:
    if (nota >= 50):
        print('\nHum, vamos lá você ainda em chances na prova de EXAME, pois sua nota foi {}'.format(nota))
    else:
        print('\nNão foi dessa vez, infelizmente você foi REPROVADO com nota {} \nTente novamente na próxima prova'.format(nota))
print('\n',10*'=','FIM',10*'=')
