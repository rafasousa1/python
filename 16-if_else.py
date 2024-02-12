name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
classification = float(input("Digite a nota de classificação do jogo:\n"))

# Os operadores lógicos: 'and, 'or' ou 'not' permite que coloque mais um if dentro de um.

# O 'and' pede para que os dois sejam atendidos
# O 'or' para que um dos dois sejam atendidos

if classification > 7.5 or yearLaunch > 2015:
    print(f"o jogo {name} é muito bom, recomendo a gameplay")
else:
    print(f"o jogo {name} não é tão bom.")