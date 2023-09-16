def main():
    global g_referencia
    g_referencia = list(input().upper()) #genoma de referencia
    comando = ['iniciando']

    while comando[0] != 'sair':
        comando = input().lower().split()

        if comando[0] == 'reverter':
            reverter(int(comando[1]), int(comando[2]))

        elif comando[0] == 'transpor':
            transpor(int(comando[1]), int(comando[2]), int(comando[3]))

        elif comando[0] == 'combinar':
            combinar(str(comando[1]), int(comando[2]))

        elif comando[0] == 'concatenar':
            concatenar(str(comando[1]))

        elif comando[0] == 'remover':
            remover(int(comando[1]), int(comando[2]))

        elif comando[0] == 'transpor_e_reverter':
            transpor_e_reverter(int(comando[1]), int(comando[2]), int(comando[3]))

        elif comando[0] == 'buscar':
            genoma = ''
            for x in range(len(g_referencia)):
                genoma += g_referencia[x]

            print(buscar(genoma, comando[1].upper())) 

        elif comando[0] == 'buscar_bidirecional':
            genoma = ''
            for x in range(len(g_referencia)):
                genoma += g_referencia[x]

            genoma_reverso = ''
            for x in range(len(g_referencia) -1 , -1, -1):
                genoma_reverso += g_referencia[x]

            print(buscar_bidirecional(genoma, comando[1].upper()) +
                  buscar_bidirecional(genoma_reverso, comando[1].upper()))

        elif comando[0] == 'mostrar':
            mostrar(g_referencia)


def reverter(i: int, j: int) -> None:
    """Reverte a sequência do genoma
    
    """
    if i > len(g_referencia):
        pass #nõa haverá reversão pois os indíces são incompatíveis

    elif j > len(g_referencia):
        j = len(g_referencia)
        lista_aux = []
        for x in range(j - 1, i-1, -1):
            lista_aux.append(g_referencia[x]) #invertendo o genoma e guardando em uma lista

        k = i
        count = 0
        for x in range(i, j):
            g_referencia[k] = lista_aux[count] #faz a troca dos genes
            k += 1
            count += 1

    else:
        lista_aux = []
        for x in range(j, i-1, -1):
            lista_aux.append(g_referencia[x]) #invertendo o genoma e guardando em uma lista

        k = i
        count = 0
        for x in range(i, j+1):
            g_referencia[k] = lista_aux[count] #faz a troca dos genes
            k += 1
            count += 1


def transpor(i: int, j: int, k: int) -> None:
    """troca a posição de sequências de genes

    """
    global g_referencia

    if i > len(g_referencia) or j > len(g_referencia):
        pass
    
    else:
        if k > len(g_referencia):
            k = len(g_referencia)

        lista_nova = []
        
        for x in range(i): #lista nova recebe todos os elementos até i
            lista_nova.append(g_referencia[x])

        for x in range(j+1, k+1): #após i a lista nova recebe todos os elementos de j+1 até k
            lista_nova.append(g_referencia[x])

        for x in range(i, j+1):
            lista_nova.append(g_referencia[x])

        for x in range(k+1, len(g_referencia)):
            lista_nova.append(g_referencia[x])

        g_referencia = lista_nova


def combinar(g: str,  i: int) -> None:
    """acrescenta o genoma g na posição i
    
    """
    global g_referencia
    g_informado = list(g.upper())
    lista_aux = list()

    for x in range(i, len(g_referencia)):
        lista_aux.append(g_referencia[x])

    if i == 0:
        lista_nova = list()
        for x in range(len(g_informado)):
            lista_nova.append(g_informado[x])

        for x in range(len(lista_aux)):
            lista_nova.append(lista_aux[x])
        
        g_referencia = lista_nova
            
    else:
        k = 0
        for x in range(i, len(g_referencia) + 1):
            if x < len(g_referencia):
                g_referencia[x] = g_informado[k]

            else:
                g_referencia.append(g_informado[k])

            k += 1

        for x in range(0, len(lista_aux)):
            g_referencia.append(lista_aux[x])


def concatenar(g: str) -> None:
    g_informado = list(g.upper())
    tamanho = len(g_informado)

    for x in range(tamanho):
        g_referencia.append(g_informado[x])


def remover(i: int, j: int) -> None:
    global g_referencia

    lista_aux = []
    for x in range(len(g_referencia)):
        if x <= j and x >= i :
            pass
        
        else:
            lista_aux.append(g_referencia[x])

    g_referencia = lista_aux


def transpor_e_reverter(i:int, j:int, k:int) -> None:
    transpor(i, j, k)
    reverter(i, k)


def buscar(g: str, sequencia: str) -> int:
    ocorrencias = 0
    tamanho = len(sequencia)
    k = 0
    while k < len(g):
        if g[k] == sequencia[0]:
            if verifica_proximos(g, tamanho, k, sequencia) and k < len(g) - tamanho + 1:
                ocorrencias += 1
                k += tamanho

            else:
                k += 1

        else: k += 1

    return ocorrencias

    """
    global g_referencia
    tamanho = len(g)
    lista_aux = list(g.upper())
    ocorrencias = 0

    k = 0
    while k < len(g):
        if g_referencia[k] == lista_aux[0]:
            if verifica_proximos(lista_aux, tamanho, k) and k < len(g_referencia) - 1:
                ocorrencias += 1
                k += tamanho #isso me certifica que em um caso ACCCCT eu não considerarei duas sequências
                            # pois a posição x será realocada para o fim ao término da análise
            else:
                k += 1
        else:
            k += 1

    return ocorrencias
"""


def verifica_proximos(genoma, tam, posicao, sequencia):
    verifica = True
    posicao += 1
    x = 1
    while x < tam and verifica and posicao < len(genoma):
        if genoma[posicao] == sequencia[x]:
            posicao += 1

        else:
            verifica = False

        x += 1

    return verifica 


def buscar_bidirecional(g:str, sequencia: str) -> int:
    
    ocorrencias = buscar(g, sequencia)
    return ocorrencias


def mostrar(g_ref):
    genoma = ''
    for x in range(len(g_ref)):
        genoma += g_ref[x]

    print(genoma)


main()