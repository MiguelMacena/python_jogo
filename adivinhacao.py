import random
#importaçoes

# começo-painel

print("*****************************************")
print("*********Adivinhe o número!!*************")
print("*****************************************")

numero_secreto = random.randrange(1, 21)
total_de_tentativas = 0
pontos = 1000

print("*Qual Dificuldade você deseja escolher?**")
print("*****************************************")
print("***(1) Facíl  (2) Médio  (3) Difícil  ***")

nivel = int(input(" Defina o nível:"))

if ( nivel == 1):
        total_de_tentativas = 10
elif (nivel==2):
        total_de_tentativas = 5
else:
    total_de_tentativas = 3

# fim- painel

# começo-jogo

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))

    palpite_str = input(" Digite um número entre 1 e 20:")
    print("Voce digitou", palpite_str)
    palpite= int(palpite_str)

    acerto = palpite == numero_secreto
    maior = palpite > numero_secreto
    menor = palpite < numero_secreto

    if ( palpite < 1 or palpite >20):
        print("Você deve digitar um número maior que 1 e menor que 20")
        continue

    if acerto:
        print("Parabens, você acertou e fez {} !!" .format(pontos))
        break
    else:
        if maior:
            print("Você errou, o seu chute foi maior do que o numero secreto")
        elif menor:
            print("Você errou e colocou um numero menor do que o numero secereto")

        pontos_perdidos = abs(numero_secreto) - palpite
        pontos = pontos - pontos_perdidos




# final-jogo