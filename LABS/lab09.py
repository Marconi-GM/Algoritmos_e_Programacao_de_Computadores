primeira_passagem = False

def main() -> None:
    N = int(input())

    ambiente, tamanho_linha = cria_ambiente(N)

    mostra_ambiente(ambiente, tamanho_linha, 0)

    escaneamento(ambiente, tamanho_linha)


def escaneamento(matriz: list[str], tamanho_linha: int) -> None:
    posicao_inicial = [None, None]
    posicao_final = [None, None]

    for linha in range(len(matriz)):
        posicao_inicial[0] = linha
        if linha % 2 == 0:
            for coluna in range(tamanho_linha):
                posicao_inicial[1] = coluna
                # se na proxima posicao tiver sujeira, apenas ande
                # se nao verifica remove
                if tem_sujeira_na_proxima_posicao(matriz, tamanho_linha, linha, coluna):
                    apenas_andar(matriz, tamanho_linha, linha, coluna)

                else: 
                    posicao_final[0], posicao_final[1] = verifica_remove_sujeira(matriz, tamanho_linha, linha, coluna)
                    voltar_a_posicao_inicial(posicao_inicial, posicao_final, matriz, tamanho_linha)

                
                andar_em_linha_par(matriz, linha, coluna, tamanho_linha)


        else:
            for coluna in range(tamanho_linha - 1, -1, -1):
                posicao_inicial[1] = coluna
                if tem_sujeira_na_proxima_posicao(matriz, tamanho_linha, linha, coluna):
                    apenas_andar(matriz, tamanho_linha, linha, coluna)

                else:
                    posicao_final[0], posicao_final[1] = verifica_remove_sujeira(matriz, tamanho_linha, linha, coluna)
                    voltar_a_posicao_inicial(posicao_inicial, posicao_final, matriz, tamanho_linha)

                if linha == len(matriz) - 1 and coluna == 0:
                    chegou_ao_fim(matriz, tamanho_linha, linha)

                else:
                    andar_em_linha_impar(matriz, linha, coluna)


                if posicao_final[1] != posicao_inicial[1] -1:
                    mostra_ambiente(matriz, tamanho_linha, linha)


def andar_em_linha_par(matriz, linha, coluna, tamanho_linha):
    
    if linha == len(matriz) - 1 and coluna == tamanho_linha - 1:
        matriz[linha][coluna] = 'r'
                
    else:
        matriz[linha][coluna] = '.'
                
        if coluna < tamanho_linha - 1:
            matriz[linha][coluna + 1] = 'r'
                    
        elif coluna == tamanho_linha - 1 and linha != len(matriz) - 1:
            matriz[linha+1][coluna] = 'r'

        mostra_ambiente(matriz, tamanho_linha, linha)
    

def andar_em_linha_impar(matriz, linha, coluna):
    matriz[linha][coluna] = '.'

    if coluna != 0:
        matriz[linha][coluna - 1] = 'r'

    if coluna == 0 and linha != len(matriz) - 1:
        matriz[linha][coluna] = '.'
        matriz[linha+1][coluna] = 'r'


def chegou_ao_fim(matriz, tamanho_linha, linha):
    k = 0
    while k < tamanho_linha - 1:
        matriz[linha][k] = '.'
        matriz[linha][k+1] = 'r'
        k += 1

        if k < tamanho_linha - 1:
            mostra_ambiente(matriz, tamanho_linha, linha)


def apenas_andar(matriz: list[str], tamanho_linha: int,
                 linha: int, coluna: int) -> None:

    if linha % 2 == 0:
        if coluna == tamanho_linha - 1:
            matriz[linha][coluna] = '.'
            matriz[linha + 1][coluna] = 'r'

        else:
            matriz[linha][coluna] = '.'
            matriz[linha][coluna + 1] = 'r'


    else:
        if coluna == 0:
            matriz[linha][coluna] = '.'
            matriz[linha + 1][coluna] = 'r'

        else:
            matriz[linha][coluna] = '.'
            matriz[linha - 1][coluna] = 'r'


def tem_sujeira_na_proxima_posicao(matriz: list[str], tamanho_linha: int,
                                   linha: int, coluna: int) -> bool:
    tem_sujeira = False

    if linha % 2 == 0:
        if coluna == tamanho_linha - 1:
            if linha != (len(matriz) -1) and matriz[linha + 1][coluna] == 'o':
                tem_sujeira = True

        else:
            if matriz[linha][coluna + 1] == 'o':
                tem_sujeira = True

    else:
        if coluna == 0:
            if linha != len(matriz) -1 and matriz[linha + 1][coluna] == 'o':
                tem_sujeira = True

        else:
            if linha != (len(matriz) -1) and matriz[linha][coluna - 1] == 'o':
                tem_sujeira = True

    return tem_sujeira



def verifica_remove_sujeira(matriz: list[str], tamanho_linha: int,
                            linha: int, coluna: int) -> tuple:

    esquerda = verifica_arredores(matriz, tamanho_linha, linha, coluna, 'esquerda')
    cima = verifica_arredores(matriz, tamanho_linha, linha, coluna, 'cima')
    direita = verifica_arredores(matriz, tamanho_linha, linha, coluna, 'direita')
    baixo = verifica_arredores(matriz, tamanho_linha, linha, coluna, 'baixo')

    if esquerda and matriz[linha][coluna - 1] == 'o':
        matriz[linha][coluna] = '.'
        matriz[linha][coluna - 1] = 'r'

        mostra_ambiente(matriz, tamanho_linha, linha)
        return verifica_remove_sujeira(matriz, tamanho_linha, linha, coluna - 1)

    elif cima and matriz[linha - 1][coluna] == 'o':
        matriz[linha][coluna] = '.'
        matriz[linha - 1][coluna] = 'r'

        mostra_ambiente(matriz, tamanho_linha, linha)
        return verifica_remove_sujeira(matriz, tamanho_linha, linha - 1, coluna)

    elif direita and matriz[linha][coluna + 1] == 'o':
        matriz[linha][coluna] = '.'
        matriz[linha][coluna + 1] = 'r'

        mostra_ambiente(matriz, tamanho_linha, linha)
        return verifica_remove_sujeira(matriz, tamanho_linha, linha, coluna + 1)

    elif baixo and matriz[linha + 1][coluna] == 'o':
        matriz[linha][coluna] = '.'
        matriz[linha + 1][coluna] = 'r'

        mostra_ambiente(matriz, tamanho_linha, linha)
        return verifica_remove_sujeira(matriz, tamanho_linha, linha + 1, coluna)
    
    return (linha, coluna)


def voltar_a_posicao_inicial(posicao_inicial: list[int], 
                             posicao_final: tuple[int], 
                             matriz: list[str], 
                             tamanho_linha: int) -> None:

    linha_final = posicao_final[0]
    coluna_final = posicao_final[1]

    linha_inicial = posicao_inicial[0]
    coluna_inicial = posicao_inicial[1]

    if coluna_final != coluna_inicial:
        voltar_coluna_inicial(coluna_final, coluna_inicial, linha_inicial, linha_final, matriz, tamanho_linha)

    if linha_final != linha_inicial:
        voltar_linha_inicial(linha_final, linha_inicial, coluna_inicial , matriz, tamanho_linha)

        
def voltar_coluna_inicial(coluna_final: int, 
                          coluna_inicial: int, linha_inicial: int, 
                          linha_final: int, 
                          matriz: list[str], tamanho_linha: int):
 
    if coluna_final > coluna_inicial:
        
        coluna = coluna_final
        for k in range(coluna_final - coluna_inicial):
            posicao_atual = (linha_final, coluna)  
            posicao_final = verifica_remove_sujeira(matriz, tamanho_linha, linha_final, coluna)
            voltar_a_posicao_inicial(posicao_atual, posicao_final, matriz, tamanho_linha)

            matriz[linha_final][coluna] = '.'
            matriz[linha_final][coluna - 1] = 'r'
            coluna -= 1
                
            mostra_ambiente(matriz, tamanho_linha, linha_inicial)


    elif coluna_inicial > coluna_final:

        coluna = coluna_final
        for k in range(coluna_inicial - coluna_final):
            posicao_atual = (linha_final, coluna)  
            posicao_final = verifica_remove_sujeira(matriz, tamanho_linha, linha_final, coluna)
            voltar_a_posicao_inicial(posicao_atual, posicao_final, matriz, tamanho_linha)

            matriz[linha_final][coluna] = '.'
            matriz[linha_final][coluna + 1] = 'r'
            coluna += 1

            mostra_ambiente(matriz, tamanho_linha, linha_inicial)


def voltar_linha_inicial(linha_final: int, 
                         linha_inicial: int, 
                         coluna_inicial: int, 
                         matriz: list[str], tamanho_linha: int):
    
    if linha_final > linha_inicial:
        linha = linha_final

        for k in range(linha_final - linha_inicial):
            posicao_atual = (linha, coluna_inicial)  
            posicao_final = verifica_remove_sujeira(matriz, tamanho_linha, linha, coluna_inicial)
            voltar_a_posicao_inicial(posicao_atual, posicao_final, matriz, tamanho_linha)

            matriz[linha][coluna_inicial] = '.'
            matriz[linha - 1][coluna_inicial] = 'r'
            linha -= 1

            mostra_ambiente(matriz, tamanho_linha, linha_inicial)


    elif linha_final < linha_inicial:
        linha = linha_final

        for k in range(linha_inicial - linha_final):
            posicao_atual = (linha, coluna_inicial)  
            posicao_final = verifica_remove_sujeira(matriz, tamanho_linha, linha, coluna_inicial)
            voltar_a_posicao_inicial(posicao_atual, posicao_final, matriz, tamanho_linha)

            matriz[linha][coluna_inicial] = '.'
            matriz[linha + 1][coluna_inicial] = 'r'
            linha += 1

            mostra_ambiente(matriz, tamanho_linha, linha_inicial)


def verifica_arredores(matriz: list[str], tamanho_linha: int, 
                       linha: int, coluna: int, 
                       posicao: str):
    
    if posicao == 'esquerda':
        if coluna == 0:
            return False
        
        else:
            return True
        
    elif posicao == 'cima':
        if linha == 0:
            return False
        
        else:
            return True
        
    elif posicao == 'direita':
        if coluna == tamanho_linha - 1:
            return False
        
        else:
            return True
        
    elif posicao == 'baixo':
        if linha == len(matriz) - 1:
            return False
        
        else:
            return True


def mostra_ambiente(matriz: list[str], tamanho_linha: int, linha: int) -> None:
    global primeira_passagem

    for linha in range(len(matriz)):
        for coluna in range(tamanho_linha):
            if coluna < tamanho_linha - 1:
                print(matriz[linha][coluna], end=' ')

            else:
                print(matriz[linha][coluna])


    if linha % 2 == 0:
        if matriz[len(matriz) -1][tamanho_linha -1] == 'r' and not primeira_passagem:
            primeira_passagem = True
            print()

        elif not (matriz[len(matriz) -1][tamanho_linha -1] == 'r' and primeira_passagem):
            print()


    else:
        if matriz[len(matriz) -1][tamanho_linha -1] == 'r' and not primeira_passagem:
            primeira_passagem = True
            print()

        elif not (matriz[len(matriz) -1][tamanho_linha -1] == 'r' and primeira_passagem):
            print()


def cria_ambiente(N: int) -> tuple:
    """Cria o ambiente com N linhas

    A função recebe o número N de linhas para então splitar cada elemento 
    da linha para formar colunas 

    """
    ambiente = list()

    for i in range(N):
        linha = input().split(' ')
        tamanho_da_linha = len(linha)
        ambiente.append(linha)

    return (ambiente, tamanho_da_linha)


if __name__ == '__main__':
    main()