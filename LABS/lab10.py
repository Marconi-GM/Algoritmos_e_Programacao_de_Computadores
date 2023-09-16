class Alloy:
    def __init__(self, vida: int, flechas: dict[str]) -> None:
        self.vida = vida
        self.flechas = flechas


    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, vida: int) -> None:
        global vida_maxima
        
        if vida >= vida_maxima:
            self._vida = int(vida_maxima)

        elif vida < 0:
            self._vida = 0

        else:
            self._vida = int(vida)


    @property
    def flechas(self):
        return self._flechas

    @flechas.setter
    def flechas(self, flechas: dict[str]) -> None:
        for nome_flecha, qtde in flechas.items():
            if qtde <= 0:
                flechas[nome_flecha] = 0

        self._flechas = flechas

        #verificar se o numero de flechas é negativo
        #se for joga ele pra zero


    def recolhe_flechas(self, flechas_usadas: dict[str], 
                        flechas: dict[str]) -> None:
        """Resgata, ao fim do combate, as flechas, além de exibir quantas
        flechas foram usadas.

        Parâmetros:
        flechas --> dicionário no qual as chaves são os nomes (tipos) das
        flechas e o valor sua quantidade.
        flechas_usadas --> dicionário no qual as chaves são os nomes (tipos) 
        das flechas e o seu valor é a quantidade desse tipo que foi usada no 
        combate.
        """
        if len(flechas_usadas) > 0:
            print('Flechas utilizadas:')

        # O laço externo é uma gambiarra para garantir que as flechas usadas
        # saiam ordenadas conforme a entrada. O laço se faz necessário pela
        # maneira com que armazenei as informações
        for flecha in flechas.keys():
            if flecha in flechas_usadas:
                self.flechas[flecha] += flechas_usadas[flecha]
                total_de_flechas = self.flechas[flecha]
                print(f"- {flecha}: {flechas_usadas[flecha]}/{total_de_flechas}")


    def dispara_as_flechas(self, maquinas: dict[str], maquinas_vivas: set, 
                           criticos: dict[str], 
                           flechas_usadas: dict[str]) -> None:
        """Aplica o dano das flechas, verifica se a flecha atirada foi um 
        acerto crítico, informa a quantidade de flechas (de cada tipo) usadas,
        caso uma flecha mate uma máquina printa a máquina morta.

        A função começa armazenando os dados da flecha atirada. Após, verifica
        se a máquina ataca está viva. Feito isso verifica se a flecha usada no
        disparo corresponde com o tipo de fraqueza da parte atacada.
        Se sim, o dano é calculado e aplicado. Se não, o dano é calculado e
        metade do seu valor é aplicado.

        Depois, com as informações da flecha usada a função verifica se o
        disparo foi um acerto crítico.

        Então armazena a informação do uso da flecha.

        Atualiza a quantidade de flechas disponíveis.

        E verifica se a máquina foi morta com a flecha.

        Parâmetros:
        maquinas --> dicionário, no qual a chave é a máquina e o valor 
        outro dicionário com as informações da máquina.
        maquinas_vivas --> conjunto com os índices das máquinas vivas para o 
        controle de expressões lógicas.
        criticos --> dicionário, no qual a chave é a máquina que recebeu o
        crítico e o valor outro dicionário, esse por sua vez tem chave como
        as coordenadas da parte que recebeu o crítico e valor a quantidade de
        vezes que a parte recebeu o crítico.
        flechas_usadas --> dicionário, no qual a chave é o tipo da flecha e o
        valor é a quantidade de vezes que tal tipo foi usado no combate.
        """
        i = 0


        while i < 3 and len(maquinas_vivas) > 0:
            maquina_esta_morta = False
            dados_do_disparo = input().split(', ')
            alvo_atacado = int(dados_do_disparo[0]) # indice do alvo
            parte_atacada = dados_do_disparo[1] # parte do corpo a ser atacada
            flecha_usada = dados_do_disparo[2] # tipo de flecha usado
            coord_flecha_usada = (int(dados_do_disparo[3]), int(dados_do_disparo[4]))

            # APLICA O DANO DA FLECHA
            if alvo_atacado in maquinas_vivas:
                if flecha_usada == maquinas[alvo_atacado]._componentes[parte_atacada]['fraqueza']:
                    dano = dano_causado(maquinas, alvo_atacado, parte_atacada, coord_flecha_usada)
                    maquinas[alvo_atacado]._pontos_vida -= dano

                elif maquinas[alvo_atacado]._componentes[parte_atacada]['fraqueza'] == 'todas':
                    dano = dano_causado(maquinas, alvo_atacado, parte_atacada, coord_flecha_usada)
                    maquinas[alvo_atacado]._pontos_vida -= dano                  

                else:
                    dano = (dano_causado(maquinas, alvo_atacado, parte_atacada, coord_flecha_usada)) // 2
                    maquinas[alvo_atacado]._pontos_vida -= dano

            # VERIFICA SE O DISPARO ACERTOU O PONTO CRÍTICO
            verifica_critico(coord_flecha_usada, maquinas, parte_atacada, alvo_atacado, criticos)
            
            # GUARDA AS INFORMAÇÕES SOBRE A FLECHA USADA
            infos_flechas_usadas(flecha_usada, flechas_usadas)

            self.flechas[flecha_usada] -= 1

            maquina_esta_morta, indice = alguma_maquina_morreu(maquinas, alvo_atacado)
            if maquina_esta_morta:
                maquinas_vivas.discard(indice)
                print(f'Máquina {indice} derrotada')
            
            i += 1


class Maquina:
    def __init__(self, info_maquina):
        self._pontos_vida = int(info_maquina[0])
        self._pontos_ataque = int(info_maquina[1])
        self._componentes = dict() # nome do componente, sua fraqueza, dano maximo, coordenadas

        # Aqui se guarda as informações dos componentes da máquina.
        # Cada componente é chave de um dicionário cujo valor é outro
        # dicionário
        # nesse último as chaves são as informações e os valores seus valores.
        for i in range(int(info_maquina[2])):
            parte = dict()

            info_das_partes = input().split(', ')
            
            # info_das_partes[0] é o nome da parte
            parte['fraqueza'] = info_das_partes[1]
            parte['dano_max'] = int(info_das_partes[2])
            parte['coordenadas'] = (int(info_das_partes[3]),
                                               int(info_das_partes[4]))
            
            self._componentes[info_das_partes[0]] = parte
            


    @property
    def pontos_vida(self):
        return self._pontos_vida
    
    @pontos_vida.setter
    def pontos_vida(self, info_maquina):
        self._pontos_vida = int(info_maquina[0])


    @property
    def pontos_ataque(self):
        return self._pontos_ataque
    
    @pontos_ataque.setter
    def pontos_ataque(self, info_maquina):
        self._pontos_ataque = int(info_maquina[1])


def main():
    vida = int(input())
    global vida_maxima

    vida_maxima = vida
    flechas = tipo_e_qtde_flechas()
    alloy = Alloy(vida, flechas)
    N_monstros = int(input()) # total de máquinas a serem enfrentadas
    proximo_combate = True
    # k é apenas uma variável para que eu não precise iterar o próprio U
    k = 0
    indice = 0
    while proximo_combate and k < N_monstros:
        U = int(input()) # numero de máquinas que Aloy enfrentará no combate AO MESMO TEMPO
        maquinas = dict()
        for i in range(U):
            info_maquina = input().split(' ')
            maquinas[i] = Maquina(info_maquina)

        proximo_combate = combate(U, maquinas, alloy, vida_maxima, indice)
        indice += 1
        k += U

    if proximo_combate:
        print("Aloy provou seu valor e voltou para sua tribo.")    


def combate(oponentes: int, maquinas: dict[str], 
            alloy: Alloy, vida_maxima: int, 
            indice: int) -> bool:

    # COMEÇA O COMBATE 
    criticos = dict()
    flechas_usadas = dict()
    inicio_ao_combate(alloy, maquinas, oponentes, indice, criticos, flechas_usadas)


    # FINAL DO COMBATE 
    if alloy.vida <= 0:
        print(f'Vida após o combate = {alloy.vida}')
        print("Aloy foi derrotada em combate e não retornará a tribo.")
        proximo_combate = False
      
    elif flechas_acabaram(alloy):
        print(f'Vida após o combate = {alloy.vida}')
        print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
        proximo_combate = False

    else:
        print(f'Vida após o combate = {alloy.vida}')
        alloy.vida += (vida_maxima) * 0.5
        alloy.recolhe_flechas(flechas_usadas, alloy.flechas)
        mostra_criticos(criticos, maquinas)
        proximo_combate = True
    
    return proximo_combate

def mostra_criticos(criticos: dict[str], maquinas: dict[str]) -> None:
    """Printa os acertos críticos.

    A função começa verificando se houve algum acerto crítico no combate.
    Caso sim, então verifica-se os críticos e os printa

    Paramêtros:
    criticos --> Dicionário, no qual a chave é o índice da máquina e o valor
    outro dicionário. Neste último a chave são as coordenadas do críticos
    e os valores a quantidade de vezes que elas foram acertadas
    maquians --> dicionário, no qual a chave é o índice da máquina e o valor
    outro dicionário. Neste último guarda-se as informações sobre a máquina.
    """
    if len(criticos) != 0:
        print('Críticos acertados:')
        # Esse proxímo laço se faz necessário para imprimir os críticos em
        # ordem ou seja, a máquina zero terá seus críticos mostrados antes da 
        # máquina um que terá seus críticos mostrados antes da máquina 2 e...
        for i in range(len(criticos) + 1):
            if i in criticos:
                print(f'Máquina {i}:')
                # Esse próximo laço também é uma gambiarra para imprimir os 
                # críticos de acorodo com a entrada das partes, na ordem certa
                for parte in maquinas[i]._componentes.keys():
                    for coord, qtde in criticos[i].items():
                        if maquinas[i]._componentes[parte]['coordenadas'] == coord:
                            print(f'- {coord}: {qtde}x')


def maquinas_atacam(alloy: Alloy, maquinas: dict[str], 
                    maquinas_vivas: set) -> None:
    """Funçao soma o dano de todas as máquinas vivas e aplica na vida de Aloy
    
    """
    if len(maquinas_vivas) > 0:
        dano_total = soma_dano_maquinas(maquinas, maquinas_vivas)
        alloy.vida = alloy.vida - dano_total


# OPONENTES AQUI SÃO AS MÁQUINAS VIVAS
def soma_dano_maquinas(maquinas: dict[str], oponentes: set) -> float:
    """Função faz a soma dos danos das máquinas que estão vivas e o retorna
    """
    dano_total = 0
    for i in oponentes:
        dano_total += maquinas[i]._pontos_ataque

    return dano_total
        

def flechas_acabaram(alloy: Alloy) -> bool:
    """Verifica se as flechas de alloy acabaram e retorna um bool com a resp
    """
    acabou = True
    total_flechas = 0
    for qtde_da_flecha in alloy.flechas.values():
        total_flechas += qtde_da_flecha

    if total_flechas > 0:
        acabou = False

    return acabou


def alguma_maquina_morreu(maquinas: dict[str], indice: int) -> tuple:
    """Verifica se a máquina cujo índice fornecido está morta

    A função retorna um booleano, com a reposta se a máquina morreu ou não e,
    caso sim, retorna também o índice da máquina morta.

    Paramêtros:
    maquinas --> dicionário, no qual a chave é o índice da máquina e o valor
    as informações sobre a máquina.
    indice --> indice da máquina que se deseja verificar se morreu ou não.
    """
    indice_maquina_morta = None
    morreu = False
    
    if maquinas[indice]._pontos_vida <= 0:
        morreu = True
        indice_maquina_morta = indice

    return (morreu, indice_maquina_morta)


def dano_causado(maquinas: dict[str], alvo_atacado: int, 
                 parte_atacada: str, coord_flecha_usada: tuple) -> float:
    """Calcula o dano e o retorna

    """
    M = maquinas[alvo_atacado]._componentes[parte_atacada]['dano_max']

    Cx = maquinas[alvo_atacado]._componentes[parte_atacada]['coordenadas'][0]
    Cy = maquinas[alvo_atacado]._componentes[parte_atacada]['coordenadas'][1]

    Fx = coord_flecha_usada[0]
    Fy = coord_flecha_usada[1]

    D = M - ((modulo(Cx - Fx)) + modulo(Cy - Fy))
    
    if D >= 0:
        return D
    
    else:
        return 0


def modulo(N: float) -> float:
    """Função necessária já que não se pode usar import math
    """
    if N >= 0:
        return N
    
    else:
        return -(N)


def inicio_ao_combate(alloy: Alloy, maquinas: dict[str], 
                      oponentes: int, indice: int, criticos: dict[str], 
                      flechas_usadas: dict[str]) -> None:
    """A função inicia e da continuidade até o fim do combate.

    A função começa armazenando as máquinas vivas em um conjunto para 
    manipulação das sentenças lógicas. Cria também um set vazio das máquinas
    mortas.
    Depois entra em um laço que terminará ou com alloy morta ou com as máquinas
    mortas ou caso as flechas da alloy acabem.
    Então se realiza os 3 disparos da alloy.
    Verifica-se se alguma máquina morreu.
    Então as máquinas realizam seu ataque.
    Isso até o fim do laço
    """
    print(f'Combate {indice}, vida = {alloy.vida}')

    maquinas_vivas = {i for i in range(oponentes)} # aqui ficarão os índices
    maquinas_mortas = set()                        # das maquinas vivas

    while (alloy.vida > 0 and not flechas_acabaram(alloy)) and len(maquinas_vivas) != 0:

        alloy.dispara_as_flechas(maquinas, maquinas_vivas, criticos, flechas_usadas)
        for i in range(oponentes):
            morreu_uma_maquina, maquina_morta = alguma_maquina_morreu(maquinas, i)

            if morreu_uma_maquina and maquina_morta not in maquinas_mortas:
                maquinas_vivas.discard(maquina_morta)
                maquinas_mortas.add(maquina_morta)
                

        maquinas_atacam(alloy, maquinas, maquinas_vivas)


def verifica_critico(coord_f_usada: tuple, maquinas: dict[str], 
                     parte_atacada: str, alvo_atacado: int, 
                     criticos: dict[str]) -> None:
    #criticos e um dict que como chave tem a maquina e como valor tem outro dict
    # esse outro dict tem como chave a tupla da posicao do critio e como valor
    # um int ou uma string avisando quantas vezes ele foi atacado 
    coord = dict()

    if coord_f_usada == maquinas[alvo_atacado]._componentes[parte_atacada]['coordenadas']:
        if alvo_atacado not in criticos and coord_f_usada not in coord:
            coord[coord_f_usada] = 1
            criticos[alvo_atacado] = coord
            #criticos[alvo_atacado][coord_f_usada] = 1
        elif alvo_atacado in criticos and coord_f_usada not in criticos[alvo_atacado]:
            criticos[alvo_atacado][coord_f_usada] = 1

        else:
            criticos[alvo_atacado][coord_f_usada] += 1


def infos_flechas_usadas(f_usada: str, flechas_usadas: dict[str]) -> None:
    """A função armazena a quantidade usada de cada tipo de flecha no dict
    """
    if f_usada not in flechas_usadas:
        flechas_usadas[f_usada] = 1

    else:
        flechas_usadas[f_usada] += 1
    

def tipo_e_qtde_flechas():
    """Cria um diconario do tipo nome_da_flecha --> quantidade
    
    A função armazena a entrada em uma lista, onde em posições pares
    se armazena os tipos da flecha e nas ímpares amazena-se a quantidade
    delas. 
    Depois cria um dicionário para facilitar a manipulação dos dados
    """
    flechas_e_qtde = input().split(' ')
    flechas = dict()
    for i in range(0, len(flechas_e_qtde), 2):
        flechas[flechas_e_qtde[i]] = int(flechas_e_qtde[i + 1])
        # optei por não fazer um list comprehension porque acho que ficaria
        # mais confuso além de enorme

    return flechas


if __name__ == '__main__':
    main()