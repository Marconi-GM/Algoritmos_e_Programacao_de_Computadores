from typing import Optional
from typing import Any
notas_finais: dict[str, int] = dict()


def main() -> None:
    F = int(input())
    filmes = list()
    for i in range(F):
        filmes.append(input().lower())

    categorias = ['filme que causou mais bocejos',
                  'filme que foi mais pausado',
                  'filme que mais revirou olhos',
                  'filme que não gerou discussão nas redes sociais',
                  'enredo mais sem noção',
                  'prêmio pior filme do ano',
                  'prêmio não merecia estar aqui']

    Q = int(input())
    avaliacoes: dict[str, str] = dict()

    for i in range(Q):
        auxiliar = input().split(', ')
        if auxiliar[0] not in avaliacoes.keys():
            avaliacoes[auxiliar[0]] = [auxiliar[1:]]

        else:
            avaliacoes[auxiliar[0]].append(auxiliar[1:])

    bocejos = calcula_vencedor(categorias[0], avaliacoes, filmes)
    pausado = calcula_vencedor(categorias[1], avaliacoes, filmes)
    olhos = calcula_vencedor(categorias[2], avaliacoes, filmes)
    sem_discussao = calcula_vencedor(categorias[3], avaliacoes, filmes)
    sem_nocao = calcula_vencedor(categorias[4], avaliacoes, filmes)

    vencedores = [bocejos, pausado, olhos, sem_discussao, sem_nocao]
    premiados = dict()
    for i in range(len(vencedores)):
        premiados[categorias[i]] = vencedores[i]

    pior_filme = calcula_pior_filme(premiados, avaliacoes)
    premiados[categorias[5]] = pior_filme

    nao_merecia = calcula_nao_merecia(avaliacoes, filmes)
    if nao_merecia == 0:
        premiados[categorias[6]] = "sem ganhadores"

    else:
        premiados[categorias[6]] = nao_merecia

    anuncia_vencedores(premiados)


def votos_por_filme(categoria: str, avaliacoes: dict):
    votos = dict()
    for dados in avaliacoes.values():
        i = 0
        while i < len(dados):
            if dados[i][0] == categoria:
                if dados[i][1] not in votos:
                    votos[dados[i][1]] = 1

                else:
                    votos[dados[i][1]] += 1

            i += 1

    return votos


def nota_dos_filmes(categoria: str, avaliacoes: dict):
    filmes_notas = dict()
    for lista in avaliacoes.values():
        i = 0
        while i < len(lista):
            if lista[i][0] == categoria:
                if lista[i][1] not in filmes_notas:
                    filmes_notas[lista[i][1]] = float(lista[i][2])

                else:
                    filmes_notas[lista[i][1]] += float(lista[i][2])

            i += 1

    return filmes_notas


def calcula_vencedor(categoria: str, avaliacoes: dict,
                     filmes: list[str]):
    global notas_finais
    notas_finais = dict()
    notas = nota_dos_filmes(categoria, avaliacoes)
    numero_votos = votos_por_filme(categoria, avaliacoes)

    for nome_notas, nota in notas.items():
        for nome_votos, votos in numero_votos.items():
            if nome_notas == nome_votos:
                if votos == 0:
                    print('DIVISAO POR ZERO')

                else:
                    notas_finais[nome_notas] = nota/votos

    nota_vencedor = 0
    vencedor = filmes[0]
    for nome_filme, nota_final in notas_finais.items():
        if nota_final > nota_vencedor:
            vencedor = nome_filme
            nota_vencedor = nota_final

    return vencedor


def calcula_pior_filme(premiados: dict, avaliacoes: dict):
    contagem = dict()
    for filme in premiados.values():
        if filme not in contagem:
            contagem[filme] = 1

        else:
            contagem[filme] += 1

    maior = 0
    pior_filme = None

    for filme, qtde in contagem.items():
        if qtde > maior:
            maior = qtde
            pior_filme = filme

        elif qtde == maior:
            pior_filme = desempata(filme, pior_filme, avaliacoes)
            maior = qtde

    return pior_filme


def desempata(empatador: str, empatado: Optional[str], avaliacoes: dict):

    categorias = ['filme que causou mais bocejos',
                  'filme que foi mais pausado',
                  'filme que mais revirou olhos',
                  'filme que não gerou discussão nas redes sociais',
                  'enredo mais sem noção',
                  'prêmio pior filme do ano',
                  'prêmio não merecia estar aqui']

    media_empatador = 0
    media_empatado = 0
    for i in range(len(categorias)):
        if i < 5:
            notas_filmes = nota_dos_filmes(categorias[i], avaliacoes)
            votos = votos_por_filme(categorias[i], avaliacoes)
            for nome_filme in notas_filmes.keys():
                if nome_filme == empatador:
                    media = (notas_filmes[empatador]) / votos[empatador]
                    media_empatador += media

                elif nome_filme == empatado:
                    media = (notas_filmes[empatado]) / votos[empatado]
                    media_empatado += media

    if media_empatador > media_empatado:
        return empatador

    elif media_empatador < media_empatado:
        return empatado


def calcula_nao_merecia(avaliacoes: dict, filmes: list[str]) -> Any:
    n_merecedores = list()
    merecedores = list()
    for lista in avaliacoes.values():
        i = 0
        while i < len(lista):
            for filme in filmes:
                if filme == lista[i][1]:
                    if lista[i][1] not in merecedores:
                        merecedores.append(lista[i][1])

            i += 1

    for filme in filmes:
        if filme not in merecedores:
            n_merecedores.append(filme)

    if len(n_merecedores) == 0:
        return 0

    else:
        return n_merecedores


def anuncia_vencedores(vencedores: dict) -> None:
    categ_especial1 = 'prêmio não merecia estar aqui'
    categ_especial2 = 'prêmio pior filme do ano'

    print("#### abacaxi de ouro ####")
    print()
    print("categorias simples")
    for categ, filme in vencedores.items():
        if categ == categ_especial1 or categ == categ_especial2:
            pass

        else:
            print(f'categoria: {categ}\n- {filme}')

    print()
    print('categorias especiais')
    for categ, filme in vencedores.items():
        if categ == categ_especial2:
            print(f'{categ}\n- {filme}')

    if vencedores[categ_especial1] == 'sem ganhadores':
        print(f'{categ_especial1}\n- {"sem ganhadores"}')

    else:
        print(categ_especial1)
        tamanho = len(vencedores[categ_especial1])
        i = 0
        print('- ', end='')
        while i < tamanho:
            if i < tamanho - 1:
                print(f'{vencedores[categ_especial1][i]},', end=' ')

            else:
                print(f'{vencedores[categ_especial1][i]}')

            i += 1


if __name__ == '__main__':
    main()