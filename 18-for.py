gamesList = ["Fifa", "Red Dead 2", "Spider-Man", "Uncharted"]

# 1 - For In: Iterando valores de uma lista, retorna no TERMINAL os valores um embaixo do outro.
for game in gamesList:
    print(game)
    
# 2 - Quando a condição for atendida, o Loop será encerrado
    for game in gamesList: # O 'break', faz com que a condição encerre o loop
        if game == "Red Dead 2":
            break
        print(game)
    
# 3 - Quando a condição for atendida, o Loop vai para a próxima interação
    for game in gamesList: # O 'continue', faz com que a condição seja pulada
        if game == "Red Dead 2":
            continue
        print(game)
        
# 4 - Avaliação do Jogo, o 'range' define um valor limite, Ex: 5 aparecerá 5 'Hello World' na tela.
gameName = input("Digite o nome do jogo:\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))

sum = 0 # Incrementa os valores das notas
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo:\n"))
    sum += note
print(f"A média de avaliação do jogo {gameName} é de {sum/gameRating :.2f}")