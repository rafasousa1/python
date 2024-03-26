"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
- E estes argumentos são passados como TUPLA

**kwargs - Alem dos valores podemos passar também as respectivas chaves para cada argumento
- Os argumentos são passados como DICIONÁRIO
"""

# 1 - Soma de números
def soma(*num):
    soma_total = 0
    for n in num:
        soma_total += n
    print(f"A soma é igual a {soma_total}")

soma(7)
soma(7,9)
soma(7,9,14,12,13)
soma(4,8,7,1,45,2,9)

# 2 - Apresentação de cursos
def apresentaçao(**data):
    for key,value in data.items():
        print(f"{key} - {value}")
print("###CURSOS")
apresentaçao(nome = "Python", category = "Backend", level = "Iniciante")
apresentaçao(nome = "Ruby", category = "Backend", level = "Intermediário")