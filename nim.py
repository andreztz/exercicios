global voce, computador

voce = 0
computador = 0

def multiplos(m):
    opcoes = []
    for i in range(1, (m + 1)):
        opcoes.append(i * (m + 1))
    return opcoes


def computador_escolhe_jogada(n, m):

    opcoes = multiplos(m)        
    jogada = int()
    if m >= n:
        jogada = n
    else:
        opcoes.reverse()    
        for i in opcoes:
            if i >= n:
                continue 
            else:
                if n - i > m:
                    jogada = m
                else:
                    jogada = n - i
    return jogada or 1
        

def usuario_escolhe_jogada(n, m):
    pergunta = True
    while pergunta:
        jogada = int(input("Quantas peças você vai tirar? "))
        print()
        if jogada >= 1 and jogada <= m:
            pergunta = False
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            print()
    return jogada


def campeonato():
    print("Voce escolheu um campeonato!")
    print()
    cont = 1
    while cont <= 3:
        print("**** Radada {} ****".format(cont))
        print()
        placar = partida()
        cont += 1
    print("Placar: Você {} x {} Computador".format(*placar))


def partida():
    global voce, computador
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    
    if n in multiplos(m):
        print(multiplos(m))
        print(n in multiplos(m))
        print("Voce começa!")
        print()
        jogador = True
    else:
        print("Computador começa!")
        print()
        jogador = False

    while True:

        if jogador:
            jogada = usuario_escolhe_jogada(n, m)
            
            n = n - jogada
            print("Voce tirou uma peca ", jogada)            
            print("Agora restam {} peças no tabuleiro".format(n))
            print()
            
            if n == 0:
                print('Fim de jogo! Você ganhou!')
                voce += 1 
                break
            jogador = False
        else:
            jogada = computador_escolhe_jogada(n, m)
            print(jogada)
            n = n - jogada
            print("O computador tirou uma peca ", jogada)
            print("Agora restam {} peças no tabuleiro".format(n))
            print()

            if n == 0:            
                print('Fim do jogo! O computador ganhou!')
                computador += 1
                break
            jogador = True
    return (voce, computador) or None


while True:
    print()
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    tipo = int(input("1 - para jogar uma partida isolada\n"
                 "2 - para jogar um campeonato: "))
    print()

    if tipo == 1:
        partida()
    
    if tipo == 2:
        campeonato()
