gameFifa = {
    "name": "Fifa 24",
    "yearLaunch": "2023",
    "gamePrice": 100.00,
    "classification": 8.5,
    "gender": ["esporte", "familia"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionário
print(gameFifa['gender'])
print(gameFifa.get('classification'))

# 2 - Recuperar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Recuperar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar itens do dicionário com chave e valor e retornam como uma tupla
print(gameFifa.items())

# 5 - Adicionar itens no diconário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizar itens do dicionário
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Remover item do dicionário
gameFifa.pop("players")
print(gameFifa)