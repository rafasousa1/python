num1 = float(input("Digite um número:\n"))
num2 = float(input("Digite outro número:\n"))
operation = input("Digite qual operação deseja (+ - * /):\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0
print(f"O resultado é igual a {result:.2f}") # ":.2f limita as casas decimais para no máximo 2 depois do ponto"