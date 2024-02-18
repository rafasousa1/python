# 1 - Liste Valores de 0 a 10 que sejam menor do que 4
# Ao invés de:
# for i in range(10):
#     if i < 4:
#         print(i)

# Melhor
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["God of War", "Red Dead 2",
             "Spider-Man Miles Morales", "Pokémon Sun"]

# 2 - Jgos que tenham apenas a letra A
newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gamesList if x != "God of War"]
print(gamesFinished)