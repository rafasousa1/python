name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = input("Está incluso em um plano mensal?\n")

print('###Dados do Jogo###')
print('===================')
print("Nome do Jogo: ", name)
print("Ano de lançamento", yearLaunch)
print("Preço do jogo:", gamePrice)
print(planIncluded, "está incluso em um plano mensal")

print('###Dados do Jogo###')
print('===================')

# Alternativa 1
# print("Nome do Jogo: ", name)
# print("Ano de lançamento", yearLaunch)
# print("Preço do jogo:", gamePrice)
# print(planIncluded, "está incluso em um plano mensal")

# Alternativa 2
# print("Nome do Jogo:", name, "\n Ano de Lançamento:", yearLaunch, "\n Preço do Jogo:", gamePrice, "\n Está incluso em um plano?", planIncluded)

# Alternativa 3
print(f"Nome do Jogo: {name} \nAno de Lançamento {yearLaunch} \nPreço do Jogo {gamePrice} \nEstá Incluso em um plano? {planIncluded}")