# 1 - Fatorial de um número
def fatorial(num):
    if num == 1:
        return 1
    else:
        return(num * fatorial(num -1))
    
number = int(input("Digite um número para o fatorial: "))
print(f"O fatorial de {number} é igual a {fatorial(number)}")

# 2 - Soma total de um número
def soma(num):
    if num == 1:
        return 1
    else:
        return(num + soma(num -1))
numero = int(input("Digite um número para sua soma: "))
print(f"A total do número {numero} é de {soma(numero)}")