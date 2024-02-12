# # 1 - Cálculo de Distância

distance = float(input("Quantos Km deseja percorrer?\n"))

if distance <= 200:
    passage = distance * 0.50
    print(f"O preço da passagem é de R${passage}")
else:
    passage = distance * 0.35

# 2 - Aumento de salário do funcionário 

salary = float(input("Digite o seu salário:\n"))
perc_increase = 0.15

if salary > 1250:
    perc_increase = 0.10
increase = salary * perc_increase
print(f"Seu aumento será de {increase:.2f}")