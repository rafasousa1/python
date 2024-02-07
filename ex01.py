#Desafio 1 
'''Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.'''

num1 = int(input("Digite um número: "))
print(f"O antecessor de {num1} é igual a {num1 -1} e o sucessor é {num1 +1}")

# Desafio 2 
'''Escreva um programa em Python que leia quatro números e calcule a média entre esses números.'''

num1 = float(input("Digite a primeira nota:\n"))
num2 = float(input("Digite a segunda nota:\n"))
num3 = float(input("Digite a terceira nota:\n"))
num4 = float(input("Digite a quarta nota:\n"))

media = (num1 + num2 + num3 + num4) / 4

print(f"Á média entre os números é {media}")