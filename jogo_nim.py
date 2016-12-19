def multiplos(n, m):
    opcoes = []
    for i in range(1, n):
        opcoes.append(i * (m + 1))
    return opcoes


def iniciar(n, m):
    if n in multiplos(n, m): 
        return True
    return False


def computador_escolhe_jogada(n, m):
    jogadas = [x for x in multiplos(n, m) if x < n]
    
    jogada = m

    if len(jogadas):
        pos = jogadas[-1]
        if n - m > pos:
            jogada = m
        else:
            for i in range(1, 3):
                if n - i == pos:
                    jogada = i
    else:
        if n < m:
            jogada = n

    return jogada



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
    return int(jogada)


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()

    if iniciar(n, m):
        print("Você começa!")
        print()
        jogador = True
    else:
        print("O computador começa!")
        print()
        jogador = False

    while n:
        if jogador:
            jogada = int(usuario_escolhe_jogada(n, m))
            n = n - jogada
            print("Você tirou uma peça ", jogada)
            print("Agora restam {} peças no tabuleiro".format(n))
            print()
            jogador = False
            if not n:
                print("Fim do jogo! Você ganhou!")
                return False
        else:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print("O computador tirou uma peça ", jogada)
            print("Agora restam {} peças no tabuleiro".format(n))
            print()
            jogador = True
            if not n:
                print("Fim do jogo! O computador ganhou!")
                return True

def campeonato():
    voce = 0
    computador = 0
    print("Voce escolheu um campeonato!")
    print()
    cont = 1
    while cont <= 3:
        print("**** Radada {} ****".format(cont))
        print()
        placar = partida()
        if placar:
            computador += 1
        else:
            voce += 1
        cont += 1
    
    print("Placar: Você {} x {} Computador".format(voce, computador))


if __name__ == '__main__':
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
