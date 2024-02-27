# 1 - Função para imprimir Hello World
def welcome():
    print("Hello World")
welcome()

# 2 - Função para somar dois números
def soma():
    return 5 + 4
print(soma())

# 3 - Função para cadastrar um jogo
def create_game():
    name = input("Digite o nome do jogo:\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
    gamePrice = float(input("Digite o preço do jogo:\n"))
    noteRating = float(input("Digite a nota de avaliaçao do jogo\n"))
    
    print(f"{name} - R${gamePrice}")
    
create_game()
create_game()