import random
print('********************************')
print('Bem-Vindo ao Jogo de Adivinhação')
print('********************************')

num_random = random.randrange(1, 101)
num_secreto = num_random
total_de_tentativas = 0
rodada = 1
pontos = 1000


print('Qual nível de dificuldade?')
print('(1) Facil (2) Médio (3) Difícil')

nivel = int(input('Defina seu nível: '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (rodada, total_de_tentativas + 1):
    print('Tentativa: {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um numero entre 1 e 100: '))
    print('Você digitou: ', chute)

    if(chute < 1 or chute> 100):
        print('Você deve digitar um numero entre 1 e 100')
        continue

    acertou = chute == num_secreto
    maior = chute > num_secreto
    menor = chute < num_secreto

    if(acertou):
        print('Você acertou', 'e sua pontuação foi de {} pontos'.format(pontos))
        break
    else:
        if(maior):
            print('Você errou, o chute que você digitou é maior')
        if(rodada == total_de_tentativas):
            print('O numero secreto era {}. Você fez {}'.format(num_secreto, pontos))
        elif(menor):
            print('Você errou, o chute que você digitou é menor')

        pontos_perdidos = abs(num_secreto - chute)
        pontos = pontos - pontos_perdidos

print('***FIM DE JOGO ***')