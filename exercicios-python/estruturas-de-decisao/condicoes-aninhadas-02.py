''' CONDIÇÕES ANINHADAS
    # Ao invés de colocar um if aninhado ao else, pode ser usada a instrução elif

    # O comando elif só será avaliado caso a comparação da condição anterior resultar em falso, ainda se a condição
    do elif for falsa o próximo elif será avaliado e assim por diante até não ter mais elif vinculando ao if que abrir a sequência.

    # Podemos ainda usar o comando else antes de encerrar a sequência do if, esse comando else só será executado caso o if seja falso e todos os elif que seguirem também
'''

# CONDIÇÃO ANINHADA

nota = int(input('Dígite a nota do aluno: '))
if (nota >= 70):
    print('\nParábens!\n Você foi APROVADO com nota {}'.format(nota))

elif (nota >= 50):
    print('\nHum, vamos lá você tem chances na prova de EXAME, pois sua nota foi {}'.format(nota))

else:
    print('\nNão foi dessa vez, infelizmente você foi REPROVADO com nota {} \nTente novamente na próxima prova'.format(nota))

print('\n',10*'=','FIM',10*'=')
