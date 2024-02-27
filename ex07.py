'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou um multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravissima"

Analise criticamente o problema e descubra:

(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- Velocidade do usuário
2. O que devo fazer com estes dados?
- Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravissima"
3. Quais são as restrições deste problema?
 -
4. Qual é o resultado esperado?
- Exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa 
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input velocidade
velocidade_maxima = 80
   if velocidade <= velocidade_max:
    print('Não levou multa')
elif velocidade > velocidade_max and velocidade <= velocidade_max +10:
    print('Levou multa leve')
elif velocidade > velocidade_max + 11 and velocidade <= velocidade_max + 20:
    print('Levou multa grave')
elif velocidade > velocidade_max + 20:
    print("Levou multa gravíssima")
'''

velocidade = int(input("Digite sua velocidade: "))
velocidade_max = 80

if velocidade <= velocidade_max:
    print('Não levou multa')
elif velocidade > velocidade_max and velocidade <= velocidade_max +10:
    print('Levou multa leve')
elif velocidade > velocidade_max + 11 and velocidade <= velocidade_max + 20:
    print('Levou multa grave')
elif velocidade > velocidade_max + 20:
    print("Levou multa gravíssima")