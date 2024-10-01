'''

    REPITA ATÉ (for)

    A linguagem Python foi pensada para ser uma linguagem mais simples, dentre outros recursos o laço de repetição "for" foi adaptado para trabalhar com listas e tuplas. O princípio de um laço de repetição é repetir uma mesma ação tantas vezes quanto for necessário, e para saber em que momento deve parar de executar as iterações uma comparação é realizada antes de executar cada interação.

    Como o "for" é projetado para listas a variável de controle (tradicionalmente usa-se a variável "i", embora possa ser outra) assume o valor dos elementos da lista, começando pelo primeiro elemento e a cada interação assumindo o valor do próximo.

    COMO O CÓDIGO A SEGUIR FUNCIONA:

        - O valor de i passa a valer 1 na primeira iteração, assim ao executar o bloco de comando do laço (no caso apenas a linha 2 do código) o print imprime o valor 1

        - Na sequência o comando volta a analisar a linha 1, de modo que i agora recebe o valor 2, imprime o número 2 no terminal e volta para a linha 1.

        - A repetição irá continuar elemento a elemento da lista até que o valor de i passe a ser 5 o último da lista. Neste caso como o valor de i ainda faz parte da lista, a linha 2 deverá ser executada.

        - Ao voltar para a linha 1, o laço identifica que não há mais elementos na lista para atribuir ao i, então encerra o bloco indo para a linha 3, que até então não tinha sido executada.
'''

for i in {1,2,3,4,5}:
    print(i)
print(5*'*','FIM',5*'*')