nome = input("Informe seu nome: ")
senha = input("Informe sua senha: ")

while (senha == nome):
    senha = input("A senha não pode ser igual ao nome: ")
print(f"Cadastro feito, Olá {nome} sua senha é {senha}")

numero = int(input("Informe um número de 0 a 10 para fazer sua tabuada: "))

for pares in range(0,21):
    if (pares %2 == 0):
        print(pares)
