import pprint # Deixar legível na hora de executar

gamesDict = {
    "Resident Evil 2": {
        "yearLaunch": 1998,
        "classification": 9.8,
        "gender": ["ação", "aventura"]
    },
    "Red Dead Redemption 2": {
        "yearLaunch": 2018,
        "classification": 10,
        "gender": ["ação", "aventura"]
    },
    "Uncharted 4": {
        "yearLaunch": 2016,
        "classification": 9.0,
        "gender": ["ação", "aventura"]
    }
}

# Deixar legível na hora de executar
pp = pprint.PrettyPrinter(depth=4) 
pp.pprint(gamesDict)

# 1 - Buscar informações dentro de um dicionário aninhado
print(gamesDict["Uncharted 4"]["gender"])

# 2 - Adicionar um novo item
gamesDict["Uncharted 4"]["players"] = 1
print(gamesDict["Uncharted 4"])

# 3 - Excluir um dicionário
del gamesDict["Resident Evil 2"]
pp.pprint(gamesDict)