# Jogo dos feijões

n = int(input())    # número de montes de feijões
tabuleiro = list(map(int,input().split()))
Alex = 0    # pontuação
Bela =  0   # pontuação
jogada = 1  # se for 1 é Alex se for -1 é a Bela
control = 1 # se for 1 a bela tira o menor se for -1 a bela tira o maior

while (n != 0):
    if (jogada == 1):
        if (tabuleiro[0] >= tabuleiro[n-1]):
            Alex += tabuleiro[0]
            tabuleiro.remove(tabuleiro[0])
        else:
            Alex += tabuleiro[n-1]
            tabuleiro.pop()
    else:
        if (control == 1):
            if (tabuleiro[0] >= tabuleiro[n-1]):
                Bela += tabuleiro[n-1]
                tabuleiro.pop()
            else:
                Bela += tabuleiro[0]
                tabuleiro.remove(tabuleiro[0])
        else:
            if (tabuleiro[0] <= tabuleiro[n-1]):
                Bela += tabuleiro[n-1]
                tabuleiro.pop()
            else:
                Bela += tabuleiro[0]
                tabuleiro.remove(tabuleiro[0])
        control *= -1
    jogada *= -1
    n -= 1

if (Alex == Bela):
    print("Alex e Bela empatam a %d" %(Alex))
elif (Alex > Bela):
    print("Alex ganha com %d contra %d" %(Alex, Bela))
else:
    print("Bela ganha com %d contra %d" %(Bela, Alex))