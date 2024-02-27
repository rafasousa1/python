'''
Crie um programa que recebe um número e imprima o seu fatorial.

Método 5Q's para montar um algoritmo:

Analise criticamente o problme a e descubra:
(Tentar explicar o problema em voz alta e pedir mais informaççoes até compreender completamente.)

1. Quais são os dados necessários?
- numero
2. O que devo fazer com estes dados?
- Calcular o fatorial desse número que for passado para o programa e exibir na tela.
3. Quais sao as restrições deste problema?
- O número deve ser um valor positivo
- O número deve ser um valor inteiro
4. Qual é o resultado esperado?
- O resultado esperado é que o fatorial do número seja exibido
5. Qual a sequeência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop 1 a numero
    fatorial *= numero
print(fatorial)
'''

numero = int(input("Digite um número para calcular seu fatorial: "))

if numero > 0:
   fatorial = 1
   for item in range(1, numero +1):
       fatorial *= item
print(fatorial)
