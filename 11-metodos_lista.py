gamesList = ["Palworld", "Spider-Man 2", "The Last of Us", "The Legend of Zelda", "Uncharted 4", "The Last of Us"]

# 1 - Identica quantos itens tem na lista
print(len(gamesList))

# 2 - Mostra a posição do iten da lista
print(gamesList.index("Palworld"))

# 3 - Adicionar item ao final da lista
gamesList.append("Spider-Man 2")
print(gamesList)

# 4 - Ordenar a lista na ordem que estava
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra, pegas os itens da gameslist e jogar na rest
gameReset = gamesList.copy()
gameReset.remove("The Legend of Zelda") # Remover item da lista
print(gameReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)