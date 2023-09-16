def main() -> None:
    operacao = input()
    primeiro_marcador = input()
    segundo_marcador = input()
    numero_linhas = int(input())
    mensagem = list()
    mensagem_auxiliar = ''

    for i in range(numero_linhas):
        mensagem.append(input())

    mensagem_auxiliar = "".join(mensagem)

    chave_k = encontrar_k(mensagem_auxiliar, operacao, primeiro_marcador,
                          segundo_marcador)

    print(chave_k)
    for i in range(numero_linhas):
        nova_mensagem = decodifica(mensagem[i], chave_k)
        print(nova_mensagem)


def decodifica(msg: str, chave: int) -> str:
    nova_mensagem = ''
    for i in range(len(msg)):
        ascii = ord(msg[i])
        if chave + ascii > 126:
            overflow = ((ascii + chave) - 127) + 32
            while overflow >= 127:
                overflow = overflow - 95

            nova_mensagem += chr(overflow)

        elif chave + ascii < 32:
            underflow = 31 - chave
            nova_mensagem += chr(abs(ascii + underflow))

        else:
            nova_mensagem += chr(ascii + chave)

    return nova_mensagem


def busca_indices(msg: str, op: str, inicio: int):
    i = inicio
    nao_encontrado = True
    if op != 'vogal' and op != 'numero' and op != 'consoante':
        while i < len(msg) and nao_encontrado:
            if ord(msg[i]) == ord(op):
                inicio = i
                indice = i
                nao_encontrado = False
            i += 1

    elif op == 'vogal':
        while i < len(msg) and nao_encontrado:
            if vogal(ord(msg[i])):
                inicio = i
                indice = i
                nao_encontrado = False
            i += 1

    elif op == 'numero':
        while i < len(msg) and nao_encontrado:
            if numero(ord(msg[i])):
                inicio = i
                indice = i
                nao_encontrado = False
            i += 1

    elif op == 'consoante':
        while i < len(msg) and nao_encontrado:
            if consoante(ord(msg[i])):
                inicio = i
                indice = i
                nao_encontrado = False
            i += 1

    return indice, inicio


def encontrar_k(msg: str, operacao: str,
                operador1: str, operador2: str) -> int:

    inicio = 0
    indice1, inicio = busca_indices(msg, operador1, inicio)
    indice2, inicio = busca_indices(msg, operador2, inicio)
    if operacao == '*':
        k = indice1 * indice2

    elif operacao == '-':
        k = indice1 - indice2

    elif operacao == '+':
        k = indice1 + indice2

    return k


def vogal(ascii: int) -> bool:
    vogais = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    if ascii in vogais:
        return True

    else:
        return False


def consoante(ascii: int) -> bool:
    vogais = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    if 66 <= ascii <= 90 and ascii not in vogais:
        return True

    elif 98 <= ascii <= 122 and ascii not in vogais:
        return True

    else:
        return False


def numero(ascii: int) -> bool:
    numeros = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

    if ascii in numeros:
        return True

    else:
        return False


if __name__ == '__main__':
    main()