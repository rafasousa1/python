# 1 - Crie uma função que receba dois argumentos: primeiro nome e o segundo nome.
def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")
    
full_name("Rafael", "Sousa")

# 2 - Crie uma função que some dois números via parâmetros
def soma(a,b):
    return a + b

print(soma(10,10))

# 3 - Argumentos default numa função
def endereço(país="Brasil"):
    print(f"Eu moro no {país}")
    
endereço()
endereço("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo: ")
    soma = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota do jogo: "))
        soma += note
    print(f"Média de avaliação do jogo {game_name} é de: {soma / qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer: "))
rating_game(rating)