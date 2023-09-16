class Carta:
    """CARTA, POSSUI UMA REPRESENTAÇÃO (NÚMERO E NAIPE) E UM VALOR

    Diretamente da ajuda do pessoal da monitoria/pad/ped a ideia de 
    criar uma classe carta, para ajudar na ordenação das mãos dos jogadores
    essa ideia ajudou demais o desenvolvimento.
    Valeu demais rapaziada!!

    A carta possui sua representação, que no caso é o número e o naipe, como
    por exemplo '7P'.
    Além disso, também possui um valor de maneira que cada carta do baralho
    tenha um único valor.
    """
    def __init__(self, representacao):
        self.repr = representacao
        self.valor = valor_da_carta(representacao)

    def __str__(self):
        print(f'Representação: {self.repr}')
        print(f'Valor: {self.valor}')      


def valor_da_carta(carta: Carta) -> int:
    """CALCULA O VALOR QUE CADA CARTA POSSUI

    O calculo funciona dando um valor pro número/letra e somando-o com o valor
    do naipe

    Parâmetros:

    carta --> string representando o número e o naipe da carta
    """
    valor = valor_do_numero(carta) + valor_do_naipe(carta)

    return valor


def valor_do_numero(carta: Carta) -> int:
    """CALCULA O VALOR DE CADA NÚMERO/LETRA DA CARTA

    O valor que cada número recebe é o próprio número multiplicado por 10.
    Já o valor que as letras recebem são únicos para cada letra.

    Parâmetros:

    carta --> string representando o número e o naipe da carta
    """
    if carta[0] == 'A':
        return 10

    elif carta[0] == '1' and carta[1] == '0':
        return 100

    elif carta[0] == 'J':
        return 125

    elif carta[0] == 'Q':
        return 150

    elif carta[0] == 'K':
        return 175

    else:
        return int(carta[0]) * 10


def valor_do_naipe(carta: Carta) -> int:
    """CALCULA O VALOR DO NAIPE

    O valor cada naipe é único.
    A função começa verificando se o número é o 10. Isso para que não haja a
    tentativa de uma posição onde o naipe não se encontra. Por exemplo, se eu
    apenas verificasse a posição carta[1] das cartas, se a carta fosse '10P',
    a posição carta[1] teria um número e não uma letra.

    *Obs: poderia ter usado slice no condicional mas só percebi depois, então
    não alterei esse condicional. Já em outras partes do código a mudança foi 
    feita.

    Paramêtros:

    carta --> string representando o número e o naipe da carta
    """
    if carta[0] == '1' and carta[1] == '0':
        if carta[2] == 'O':
            return 1
            
        elif carta[2] == 'E':
            return 3
            
        elif carta[2] == 'C':
            return 5
            
        elif carta[2] == 'P':
            return 7
    

    elif carta[1] == 'O':
        return 1
        
    elif carta[1] == 'E':
        return 3
        
    elif carta[1] == 'C':
        return 5
        
    elif carta[1] == 'P':
        return 7


class Jogador:
    """CLASSE JOGADOR, ONDE CADA JOGADOR POSSUI UMA MÃO DE CARTAS

    Jogador é uma classe, onde cada jogador possui sua mão.
    """
    def __init__(self, cartas):
        self.mao = cartas

    
    @property
    def mao(self):
        return self._mao
    
    @mao.setter
    def mao(self, cartas):
        mao = list()
        for carta in cartas:
            mao.append(Carta(carta))

        self._mao = mao


def main() -> None:
    pilha_descarte = list() # pilha das cartas descartadas
    jogadores = list() # lista de jogadores

    J = int(input()) # Numero de jogadores

    for i in range(J): # Armazena a mão de cada jogador
        cartas = input().split(', ')
        jogadores.append(Jogador(cartas))
        ordena_a_mao(jogadores[i])

    N = int(input()) # Numero de jogadas até o dúvido
    for i in range(J):
        imprime_mao(jogadores[i], i)

    imprime_pilha(pilha_descarte)
    jogo(jogadores, pilha_descarte, N) # COMEEEEÇA O JOGO


def ordena_a_mao(jogador: Jogador) -> None:
    """ORDENA A MÃO DE UM JOGADOR POR VEZ

    A função faz uso de uma ordenação por seleção para ordenar a mão de cada
    jogador.
    A ordenação ocorre pelos valores de cada carta, onde cada carta do baralho
    possui um valor inteiro correspondente à carta.

    Paramêtros:

    jogador --> Jogador que terá a mão ordenada
    """
    N = len(jogador.mao)

    for i in range(N - 1):
        maior = i 
        for j in range(i + 1, N):
            if jogador.mao[j].valor > jogador.mao[maior].valor:
                maior = j

        aux = jogador.mao[i]
        jogador.mao[i] = jogador.mao[maior]
        jogador.mao[maior] = aux


def jogo(jogadores: Jogador, pilha_descarte: list[str], N: int) -> None:
    """O DECORRER DO JOGO

    Nesta função é onde o jogo acontece.

    A função começa com um laço que só terminará quando houver um jogador.

    Após entrar no laço a verificamos se o jogador terá que blefar ou não.
    Dependendo da necessidade, ou não, do blefe as próximas medidas são
    tomadas.

    > verifica-se a próxima carta a se jogar
    > verifica-se a quantidade de cartas iguais a ela para que as descarte
    > descarta-se as cartas
    > imprime-se a pilha
    > após N 'rodadas' o próximo jogador duvida
    > ocorrido a duvida verifica-se se o jogador anterior blefou ou não
    > dependendo do resultado da dúvida, medidas são tomadas
    > verifica-se se há um vencedor
    > em caso negativo, recomeça-se os passos em nova rodada

    Parâmetros:

    jogadores --> lista com os jogadores
    pilha_descarte --> pilha com as cartas descartadas
    N --> número de rodadas antes do 'DUVIDO'
    """
    i = 0
    k = 1
    qtde_jogadores = len(jogadores)
    ha_um_vencedor = False
    cartas_descartadas = list()
    ultima_carta = jogadores[i].mao[-1] # ULTIMA CARTA JOGADA, SEJA POR BLEFANTES OU NÃO
    ultima_carta_da_seq = jogadores[i].mao[-1] # ULTIMA CARTA JOGADA QUE RESPEITA A SEQUENCIA, UNICAMENTE PROS BLEFANTES 
    # a váriavel ultima carta da sequencia se faz necessaria para que,
    # alem de verificar a necessidade do blefe, ajude os blefantes na hora de 
    # falar qual carta está "jogando"


    while not ha_um_vencedor:
        cartas_descartadas = list()

        if tem_que_blefar(jogadores[i], ultima_carta_da_seq):
            carta_do_blefe = verifica_qual_carta_jogar(ultima_carta, jogadores[i], tem_que_blefar(jogadores[i], ultima_carta_da_seq))
            ultima_carta = carta_do_blefe
            qtde = quantas_cartas_serao_descartadas(ultima_carta, jogadores[i])

            if ultima_carta_da_seq.repr[:2] == '10':
                print(f'[Jogador {i + 1}] {qtde} carta(s) {ultima_carta_da_seq.repr[:2]}')
            else:
                print(f'[Jogador {i + 1}] {qtde} carta(s) {ultima_carta_da_seq.repr[0]}')

            descarta_cartas(carta_do_blefe, cartas_descartadas, pilha_descarte, jogadores[i])
            imprime_pilha(pilha_descarte)

        else:
            carta_jogada = verifica_qual_carta_jogar(ultima_carta_da_seq, jogadores[i], tem_que_blefar(jogadores[i], ultima_carta_da_seq))
            ultima_carta = carta_jogada
            ultima_carta_da_seq = ultima_carta
            qtde = quantas_cartas_serao_descartadas(ultima_carta, jogadores[i])

            if ultima_carta.repr[:2] == '10':
                print(f'[Jogador {i + 1}] {qtde} carta(s) {ultima_carta_da_seq.repr[:2]}')
            else:
                print(f'[Jogador {i + 1}] {qtde} carta(s) {ultima_carta_da_seq.repr[0]}')
            descarta_cartas(carta_jogada, cartas_descartadas, pilha_descarte, jogadores[i])
            imprime_pilha(pilha_descarte)

        if k == N :
            jogador_duvidoso = i + 1 #ÍNDICES DE CADA JOGADOR
            jogador_duvidado = i

            if i == len(jogadores) - 1:
                jogador_duvidoso = 0

            duvidaram(jogador_duvidoso, jogador_duvidado, pilha_descarte, cartas_descartadas, ultima_carta_da_seq, jogadores)
            if len(pilha_descarte) == 0: # SE HOUVE DUVIDA, A PILHA FOI ZERADA E ENTÃO REINICIA-SE AS CARTAS JOGADAS
                ultima_carta = jogadores[jogador_duvidoso].mao[-1]
                ultima_carta_da_seq = jogadores[jogador_duvidoso].mao[-1]


        k += 1
        i += 1
        if i == qtde_jogadores:
            i = 0

        if k > N:
            k = 1


        ha_um_vencedor, vencedor = alguem_ganhou(jogadores)

        
    print(f'Jogador {vencedor + 1} é o vencedor!')


def quantas_cartas_serao_descartadas(ultima_carta: Carta, 
                                     jogador: Jogador) -> int:
    """CALCULA QUANTAS CARTAS DEVEM SER DESCARTADAS

    No caso em que na mão do jogador há mais de uma carta com mesmo número 
    da carta que será descartada, essa função calcula quanta cartas serão
    descartadas

    Paramêtros:

    ultima_carta --> ultima carta descartada, no caso a carta que será
    descartada e deseja-se verificar quantas mais serão junto com ela

    jogador --> o jogador em específico, para avaliar a mão do jogador
    """
    qtde = 0
    for i in range(len(jogador.mao)):
        if jogador.mao[i].repr[0] == ultima_carta.repr[0]:
            qtde += 1

    return qtde


def duvidaram(duvidoso: int, duvidado: int, pilha_descarte: list[str], 
              cartas_descartadas: list[str], ultima_carta_da_seq: Carta, 
              jogadores: list[Jogador]) -> None:
    """VERIFICA O BLEFE APÓS ALGUEM DUVIDAR

    A função verifica, após alguem duvidar, se o jogador passado blefou ou não.
    Se sim o jogador que blefou recolhe as cartas, se não o jogador que 
    duvidou recolhe as cartas.
    Após isso feito, imprime-se as mãos dos jogadores

    Parâmetros:

    duvidoso --> índice do jogador, na lista de jogadores, que duvidou
    duvidado --> índice do jogador, na lista de jogadores, que foi recebeu a
    duvida
    pilha_descarte --> pilha com as cartas descartadas
    cartas_descartadas --> lista com as cartas recem descartadas
    ultima_carta_da_seq --> ultima carta que, ao menos, deveria estar na pilha
    de cartas recém descartadas. Se o jogador blefou então ela não se encontra
    lá.
    jogadores --> lista com os jogadores
    """
    print(f'Jogador {duvidoso + 1} duvidou.')

    jogador_duvidado_blefou = verifica_blefe(ultima_carta_da_seq, cartas_descartadas)

    if jogador_duvidado_blefou:
        recolhe_a_pilha(duvidado, pilha_descarte, jogadores)


    else:
        recolhe_a_pilha(duvidoso, pilha_descarte, jogadores)

    for i in range(len(jogadores)):
        imprime_mao(jogadores[i], i)
    imprime_pilha(pilha_descarte)


def recolhe_a_pilha(jogador: Jogador, pilha_descarte: list[str], 
                    jogadores: list[Jogador]) -> None:
    """RECOLHE AS CARTAS DA PILHA DE DESCARTA PARA A MÃO DO JOGADOR

    A função recebe o jogador que terá que recolher as cartas.
    Então percorre-se a pilha, removendo as cartas e colocando-as na mão do 
    jogador.
    Após, feito, ordena-se a mão do jogador.

    Parâmetros:

    jogador --> jogador que receberá as cartas
    pilha_descarte --> pilha com as cartas descartadas
    jogadores --> lista com os jogadores
    """
    for i in range(len(pilha_descarte)):
        carta = pilha_descarte.pop()
        jogadores[jogador].mao.append(carta)

    
    ordena_a_mao(jogadores[jogador])


def verifica_blefe(ultima_carta: Carta, cartas_descartadas: list[str]) -> bool:
    """VERIFICA SE O JOGADOR BLEFOU OU NÃO

    A função recebe a última carta da sequência, ou seja, a carta que os
    jogadores estão se baseando para blefar ou não.
    Por exemplo, se a carta mais alta lançada até o momento é um 9,
    mas o jogador lançou 3 números 2 (ou seja ele blefou),
    então a lista de cartas descartadas terá 3 números 2.
    Mas a carta que ele deveria ter lançado era, no mínimo, um 9.
    Como ele blefou as cartas que estão na lista de cartas descartadas tem,
    obrigatoriamente, valor menor que a ultima carta da sequência.
    Dessa maneira verifica-se o blefe.
    """
    for i in range(len(cartas_descartadas)):
        if cartas_descartadas[i].valor < ultima_carta.valor:
            return True
        
    # CASO NENHUMA CARTA TENHA VALOR MENO QUE A ULTIMA CARTA, ENTÃO NÃO É BLEFE
    return False


def descarta_cartas(carta_descartada: Carta, cartas_descartadas: list[Carta], 
                    pilha_descarte: list[str], jogador: Jogador) -> None:
    tamanho_da_mao = len(jogador.mao)
    i = tamanho_da_mao - 1 
    while i > -1:
        if jogador.mao[i].repr[0] == carta_descartada.repr[0]:
            pilha_descarte.append(jogador.mao[i])
            cartas_descartadas.append(jogador.mao[i])
            jogador.mao.pop(i)
            tamanho_da_mao -= 1

        i -= 1


def verifica_qual_carta_jogar(ultima_carta: Carta, jogador: Jogador, 
                              tem_que_blefar: bool) -> Carta:
    """DEVOLVE A CARTA QUE SERÁ UTILIZADA NA PRÓXIMA JOGADA

    Caso o jogador tenha que blefar, então a carta devolvida é a de menor valor
    e como a mão do jogador está ordenada, ela se encontra na última posição
    da sua mão.

    Caso contrário verifica-se se há carta de mesmo número que a ultima jogada
    e se não houver a função devolve a próxima carta na ordem de força
    """
    if tem_que_blefar:
        return jogador.mao[-1]

    else:
        for i in range(len(jogador.mao) - 1, -1, -1):
            if jogador.mao[i].repr[0] == ultima_carta.repr[0]:
                return jogador.mao[i]

            elif jogador.mao[i].valor >= ultima_carta.valor:
                return jogador.mao[i]


def alguem_ganhou(jogadores: list[Jogador]) -> tuple:
    """VERIFICA SE HÁ VENCEDOR
    
    Caso a mão de algum jogador esteja vazia, mesmo após alguem duvidar,
    então ele ganhou
    """
    for i in range(len(jogadores)):
        if len(jogadores[i].mao) == 0:
            return (True, i)
        
    return (False, None)


def imprime_mao(jogador: Jogador, i: int) -> None:
    """IMPRIME A MÃO DO JOGADOR
    """
    print(f'Jogador {i + 1}')
    if len(jogador.mao) > 0:
        print('Mão:', end=' ')

    else:
        print('Mão: ')
    
    for k in range(len(jogador.mao)):
        if k < len(jogador.mao) - 1:
            print(jogador.mao[k].repr, end=' ') 

        else:
            print(jogador.mao[k].repr)


def imprime_pilha(pilha_descarte: list[str]) -> None:
    """IMPRIME A PILHA DAS CARTAS DESCARTADAS
    """
    if len(pilha_descarte) != 0:
        print('Pilha:', end=' ')
        for i in range(len(pilha_descarte)):
            if i < len(pilha_descarte) - 1:
                print(pilha_descarte[i].repr, end=' ')

            else:
                print(pilha_descarte[i].repr)

    else:
        print('Pilha:')


def tem_que_blefar(jogador: Jogador, ultima_carta: Carta) -> bool:
    """VERIFICA SE O JOGADOR PRECISARÁ BLEFAR OU NÃO

    A função analisa a mão do jogador e verifica se há carta de mesmo número,
    ou maior, do que a ultima carta jogada.
    Em caso positivo, o blefe não se faz necessário.
    Em caso negativo, se faz.

    Parâmetros:

    jogador --> jogador que terá a mão analisada
    ultima_carta --> ultima carta que foi jogada
    """
    precisa_blefar = True
    tamanho_da_mao = len(jogador.mao)
    
    for i in range(tamanho_da_mao - 1, -1, -1):
        if jogador.mao[i].repr[0] == ultima_carta.repr[0]:
            return not precisa_blefar

        elif jogador.mao[i].valor >= ultima_carta.valor:
            return not precisa_blefar
            
    # SE NÃO ENCONTROU NENHUMA CARTA NA MÃO DELE COM VALOR MAIOR OU 
    # IGUAL À ÚLTIMA CARTA JOGADA, ENTÃO PRECISA BLEFAR   
    return precisa_blefar


if __name__ == '__main__':
    main()