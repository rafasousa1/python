gamesTuple = ("Fifa 24", "Red Dead Redemption 2", "Palworld",
              "The Last of Us", "Uncharted 4")
print(gamesTuple)
print(type(gamesTuple))
#name = ("Rafael") # Se tiver apenas UM item ele é considerado STRING
#print(type(name))

# - NÃO POSSIBLITA ADICIONAR VALORES NA TUPLA
# - NÃO POSSIBLITA REMOER VALORES NA TUPLA
# - NÃO POSSIBLITA ORDENAR VALORES NA TUPLA

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o último item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Mostra a posição do item da lista
print(gamesTuple.index("Palworld"))