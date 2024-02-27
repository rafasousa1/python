'''
Escreva um programa que, ao iniciar gera un valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se a chute foi acima, abaixo ou igual ao valor aleatório gerado no inicio do programa.

Método SQ's para montar un algoritimo:

Analise criticamente o problema e descubra:

(Tente explicar este problema para você mesmo en voz alta e peca mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
 - valor aleatório de 1 a 10
 - chute do usuário
2. O que devo fazer con estes dados?
- Comparar o chute com o valor aleatório gerado, e dizer se o chute foi maior menor ou igual ao valor
3. Quais são as restrições deste problema?
- Apenas um valor de 1 a 10
4. Qual resultado esperado?
- Se o valor gerado foi acima, abaixo ou igual ao valor aleatório gerado no inicio do programa.
5. Qual é sequência de passos ser feitas para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
    print(chutou alto)
if chute < valor_aleatorio
    print(chutou baixo)
if chute = valor_aleatorio
    print(acertou)
'''

import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input("Chute um valor de 1 a 10: "))
    if chute > valor_aleatorio:
        print("Chutou muito alto")
    elif chute < valor_aleatorio:
        print("Chutou muito baixo")
    elif chute == valor_aleatorio:
        acertou = True
        print("ACERTOU!")