gameDescription = '''
Fifa 24 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online.
'''

gameName = "Fifa"
gameVersion = " 24"
line = "="

# 1- Operação de concatenação de strings
print(line * 25)
gameFullName = gameName + gameVersion
print(gameFullName)

# 2- Operação de multiplicação de strings
print(line * 25)

# 3- Procurar palavra dentro de um texto
print("Fifa" in gameDescription)
print("futebol" in gameDescription)