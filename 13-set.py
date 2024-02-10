gameSet = {"Fifa 24", "Red Dead Redemption 2", "Palworld",
              "The Last of Us", "Uncharted 4"}
print(gameSet)
# - NÃO POSSIBILITA RECUPERAR VALORES VIA FATIAMENTO OU SLICE

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 24", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 - Remover um item do set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)