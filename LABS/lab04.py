D = int(input())
for p in range(1, D+1):
    
    M = int(input())
    brigam = []
    for i in range(M):
        brigam.append(input().split())

    #procedimento e quantidade --> p_q
    p_q = input().split()


    Z = int(input())
    #pets presentes
    #animal e procedimento --> a_p
    a_p = []
    for i in  range(Z):
        a_p.append(input().split())

    #verificando se há brigas

    """

    os dois primeiros laços são para verificar se há pets que brigam presentes no petshop
    uma vez que há um pet que briga presente verifica-se se o seu par na lista também está
    presente. 
    Para isso caso o pet presente esteja na posição brigam[k][0] buscamos verificar se o pet
    brigam[k][1] também está presente e vice-versa
    uma vez que o primeiro é identificado e o seu par também, ambos vão para a lista ja_brigaram
    para que não seja contada uma briga a mais


    """
    numero_brigas = 0
    ja_brigaram = []
    for i in range(M):
        for k in range(Z):
            if brigam[i][0] == a_p[k][0] and (brigam[i][0]+brigam[i][1]) not in ja_brigaram:
                for h in range(Z):
                    if brigam[i][1] == a_p[h][0]:
                        numero_brigas += 1
                        ja_brigaram.append(brigam[i][0]+brigam[i][1])
                        ja_brigaram.append(brigam[i][1]+brigam[i][0])

            if brigam[i][1] == a_p[k][0] and (brigam[i][1]+brigam[i][0]) not in ja_brigaram:
                for h in range(Z):
                    if brigam[i][0] == a_p[h][0]:
                        numero_brigas += 1
                        ja_brigaram.append(brigam[i][0]+brigam[i][1])
                        ja_brigaram.append(brigam[i][1]+brigam[i][0])



    #verificando se os animais foram atendidos

    atendidos = []
    nao_atendidos = []
    indisponivel = []

    for i in range(Z):
        #verificando se o procedimento está disponivel
        if a_p[i][1] not in p_q:
                indisponivel.append(a_p[i][0])

        #verificando se o há disponibilidade do procedimento
        for k in range(0, len(p_q), 2): 
            if a_p[i][1] == p_q[k] and int(p_q[k+1]) > 0:
                atendidos.append(a_p[i][0])
                p_q[k+1] = int(p_q[k+1]) - 1 #tirando a quantidade que foi usada do procedimento

            elif a_p[i][1] == p_q[k] and int(p_q[k+1]) <= 0:
                nao_atendidos.append(a_p[i][0]) 


    print(f'Dia: {p}')
    print(f'Brigas: {numero_brigas}')

    if len(atendidos) > 0:
        print('Animais atendidos: ', end='')
        for i in range(len(atendidos)):
            if i < len(atendidos) - 1:
                print(atendidos[i], end=', ')

            else:
                print(atendidos[i])
          
    if len(nao_atendidos) > 0:
        print('Animais não atendidos: ', end='')
        for i in range(len(nao_atendidos)):
            if i < len(nao_atendidos) - 1:
                print(nao_atendidos[i], end=', ')

            else:
                print(nao_atendidos[i])

    if len(indisponivel) > 0:
        for i in range(len(indisponivel)):
            print(f'Animal {indisponivel[i]} solicitou procedimento não disponível.')

    print()