gameName = "Fifa24"
gameDescription = '''
Fifa 24 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online.
'''
# 1- Retornar string em MAIÚSCULO
print(gameName.upper()) 

# 2- Retornar string em minúsculo
print(gameName.lower())

# 3- Apenas primeira letra Maiúscula
print(gameName.capitalize())
print(gameName.title())

# 4- Retorna a string centralizada com caractere de preenchimento
print(gameName.center(10, '-'))

# 5- Retorna a posição de um determinado caractere
print(gameName.find("a"))

# 6- Conta quantos caracteres de determinada letra tem na string
print(gameDescription.count("f"))

# 7- Altera um elemento por outro
print(gameDescription.replace("Fifa", "EA FC"))

# 8- Quebra a string em partes menores e ter um mapeamento melhor do texto
print(gameDescription.split(','))