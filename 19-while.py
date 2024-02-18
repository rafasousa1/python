gameName = input("Digite o nome do jogo:\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while(rating != -1): # Enquanto a nota não for -1 vai pedir para informar a nota toda hora, e quando informar -1 ele divide as 4 notas por 4
    rating = float(input("Informe a nota do jogo:\n"))
    if(rating != -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
print(f"A média da avaliação do jogo {gameName} é {average :.2f}")