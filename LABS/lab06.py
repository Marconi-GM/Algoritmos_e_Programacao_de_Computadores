def main() -> None:
    vetor_inicial = converte_inteiros(input().split(','))

    operacao = 'iniciando'
    while operacao != 'fim':
        operacao = input()

        if operacao == 'soma_vetores':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = soma_vetores(vetor_inicial, vetor2, operacao)
            print(vetor_inicial)

        elif operacao == 'subtrai_vetores':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = subtrai_vetores(vetor_inicial, vetor2, operacao)
            print(vetor_inicial)

        elif operacao == 'multiplica_vetores':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = multiplica_vetores(vetor_inicial, vetor2, operacao)
            print(vetor_inicial)

        elif operacao == 'divide_vetores':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = divide_vetores(vetor_inicial, vetor2, operacao)
            print(vetor_inicial)

        elif operacao == 'multiplicacao_escalar':
            escalar = int(input())
            print(multiplicacao_escalar(vetor_inicial, escalar))

        elif operacao == 'n_duplicacao':
            n = int(input())
            print(n_duplicacao(vetor_inicial, n))

        elif operacao == 'soma_elementos':
            vetor_inicial = [soma_elementos(vetor_inicial)]
            print(vetor_inicial)

        elif operacao == 'produto_interno':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = [produto_interno(vetor_inicial, vetor2)]
            print(vetor_inicial)

        elif operacao == 'multiplica_todos':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = multiplica_todos(vetor_inicial, vetor2)
            print(vetor_inicial)

        elif operacao == 'correlacao_cruzada':
            vetor2 = converte_inteiros(input().split(','))
            vetor_inicial = correlacao_cruzada(vetor_inicial, vetor2, operacao)
            print(vetor_inicial)


def correlacao_cruzada(vetor1: list[int],
                       mascara: list[int],
                       funcao: str = '') -> list[int]:

    auxiliar = list()
    tamanho_mascara = len(mascara)

    for i in range(len(vetor1) - tamanho_mascara + 1):
        auxiliar.append(soma_elementos(
            multiplica_vetores(vetor1[i:tamanho_mascara+i], mascara, funcao)))

    vetor1 = auxiliar
    return vetor1


def soma_vetores(vetor1: list[int],
                 vetor2: list[int],
                 funcao: str = 'soma_vetores') -> list[int]:

    confere_tamanho(vetor1, vetor2, funcao)
    vetor_soma = list()
    for i in range(len(vetor1)):
        vetor_soma.append(vetor1[i] + vetor2[i])

    return vetor_soma


def subtrai_vetores(vetor1: list[int],
                    vetor2: list[int],
                    funcao: str = 'subtrai_vetores') -> list[int]:

    confere_tamanho(vetor1, vetor2, funcao)
    vetor_subtracao = list()
    for i in range(len(vetor1)):
        vetor_subtracao.append(vetor1[i] - vetor2[i])

    return vetor_subtracao


def multiplica_vetores(vetor1: list[int],
                       vetor2: list[int],
                       funcao: str = 'multiplica_vetores') -> list[int]:

    confere_tamanho(vetor1, vetor2, funcao)

    vetor_multiplicacao = list()
    for i in range(len(vetor1)):
        vetor_multiplicacao.append(vetor1[i] * vetor2[i])

    return vetor_multiplicacao


def divide_vetores(vetor1: list[int],
                   vetor2: list[int],
                   funcao: str = 'divide_vetores') -> list[int]:

    confere_tamanho(vetor1, vetor2, funcao)
    vetor_divisao = list()
    for i in range(len(vetor1)):
        vetor_divisao.append(vetor1[i] // vetor2[i])

    return vetor_divisao


def multiplicacao_escalar(vetor1: list[int], escalar: int) -> list[int]:

    for i in range(len(vetor1)):
        vetor1[i] = vetor1[i] * escalar

    return vetor1


def n_duplicacao(vetor1: list[int], n: int) -> list[int]:

    vetor1 *= n
    return vetor1


def soma_elementos(vetor1: list[int]) -> int:

    soma = 0
    for i in range(len(vetor1)):
        soma += vetor1[i]

    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    return soma_elementos(multiplica_vetores(
        vetor1, vetor2, 'multiplica_vetores'))


def converte_inteiros(vetor: list[str]) -> list[int]:
    auxiliar = list()

    for i in range(len(vetor)):
        auxiliar.append(int(vetor[i]))

    return auxiliar


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    auxiliar = list()
    aux = vetor2.copy()

    for i in range(len(vetor1)):
        auxiliar.append(soma_elementos(
            multiplicacao_escalar(vetor2, vetor1[i])))
        vetor2 = aux.copy()

    vetor1 = auxiliar
    return vetor1


def confere_tamanho(vetor1: list[int],
                    vetor2: list[int],
                    nome_funcao: str = '') -> None:
    """confere os tamanhos dos vetores e opera para que
      eles fiquem o mesmo numero de elementos

    a função recebe os vetores, verifica a quantidade de elementos
    e, em caso de desigualdade,
    acrescenta elementos até que a quantidade de elementos se tornem iguais
    dependendo da função os elementos a serem incluidos será zero ou um

    """

    if len(vetor1) == len(vetor2):
        pass

    else:
        if nome_funcao == 'soma_vetores' or nome_funcao == 'subtrai_vetores':
            if len(vetor1) > len(vetor2):

                diferenca = len(vetor1) - len(vetor2)
                for i in range(diferenca):
                    vetor2.append(0)

            else:
                diferenca = len(vetor2) - len(vetor1)
                for i in range(diferenca):
                    vetor1.append(0)

        elif nome_funcao == 'multiplica_vetores':
            if len(vetor1) > len(vetor2):

                diferenca = len(vetor1) - len(vetor2)
                for i in range(diferenca):
                    vetor2.append(1)

            else:
                diferenca = len(vetor2) - len(vetor1)
                for i in range(diferenca):
                    vetor1.append(1)

        elif nome_funcao == 'divide_vetores':
            if len(vetor1) > len(vetor2):

                diferenca = len(vetor1) - len(vetor2)
                for i in range(diferenca):
                    vetor2.append(1)

            else:
                diferenca = len(vetor2) - len(vetor1)
                for i in range(diferenca):
                    vetor1.append(0)


if __name__ == '__main__':
    main()