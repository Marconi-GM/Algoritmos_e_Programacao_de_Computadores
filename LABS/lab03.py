numeros_jogadores = int(input())
numeros_retirados = list(map(int, input().split()))
numeros_sorteados = list(map(int, input().split())) #converte a lista de strings para uma lista de inteiros

if (numeros_jogadores % 2) != 0:
    metade = int(numeros_jogadores/2) + 1

else:
    metade = int(numeros_jogadores/2)

k = 1 #k e j ajudarão a percorrer a lista de numeros sorteados
j = 0

pontuacao = (numeros_sorteados[k] - numeros_sorteados[j]) * numeros_retirados[0]
empate = False
vencedor = 1

for i in range(metade): 
    maior = (numeros_sorteados[k] - numeros_sorteados[j]) * numeros_retirados[i]
    if maior > pontuacao:
        pontuacao = maior
        vencedor = i + 1
    
    elif maior == pontuacao and i != 0:  #i != 0 me certifica que não considerarei empate entre a primeira posicao e ela mesma
        empate = True

    k += 2
    j += 2

for i in range(metade, numeros_jogadores):
    maior = (numeros_sorteados[k] - numeros_sorteados[j]) + numeros_retirados[i]
    if maior > pontuacao:
        pontuacao = maior
        vencedor = i + 1

    elif maior == pontuacao:
        empate = True
    
    k += 2
    j += 2

if empate:
    print('Rodada de cerveja para todos os jogadores!')

else:
    print(f'O jogador número {vencedor} vai receber o melhor bolo da cidade pois venceu com {pontuacao} ponto(s)!')