# Sopinha de letras

m, n = map(int, input().split())    # m = linhas, n = colunas
tabuleiro = [list(str(input())) for i in range(m)]      # guarda os valores do tabuleiro
k = int(input())    # número de palavras
palavras = [str(input()) for i in range(k)]     # guarda as palavras a procurar
found = [0 for i in palavras]       # marca com 0 as palavras que ainda não foram encontradas
resp = {}   # dicionário que vai guardar as respostas


# ------------------ funções auxiliares ---------------
def check_horizontal(s, x, c):
    comp = len(s)
    return (x+comp-1)<c

def find_horizontal(s, x, y, tabuleiro):
    palavra = ''.join(tabuleiro[y][x:x+len(s)])
    if (s == palavra):
        return 1        # plavra encontrada e está na ordem correta
    if (s == palavra[::-1]):
        return 2        # palavra encontrada e está invertida
    return 0    # não foi encontrada

def check_vertical(s, y, l):
    comp = len(s)
    return (y+comp-1) < l

def find_vertical(s, x, y, tabuleiro):
    palavra = ''.join(tabuleiro[i][x] for i in range(y, y+len(s)))
    if (s == palavra):
        return 1        # plavra encontrada e está na ordem correta
    if (s == palavra[::-1]):
        return 2        # palavra encontrada e está invertida
    return 0    # não foi encontrada

def check_diagonal_1(s, x, y, l, c):    # diagonal que vai para a direita
    comp = len(s)
    return (x+comp-1 < c and y+comp-1 < l)

def find_diagonal_1(s, x, y, tabuleiro):
    palavra = ''.join(tabuleiro[y+i][x+i] for i in range(0, len(s)))
    if (s == palavra):
        return 1        # plavra encontrada e está na ordem correta
    if (s == palavra[::-1]):
        return 2        # palavra encontrada e está invertida
    return 0    # não foi encontrada

def check_diagonal_2(s, x, y, l):    # diagonal que vai para a esquerda
    comp = len(s)
    return (x+comp-1 > 0 and y+comp-1 < l)

def find_diagonal_2(s, x, y, tabuleiro):
    palavra = ''.join(tabuleiro[y+i][x-i] for i in range(0, len(s)))
    if (s == palavra):
        return 1        # plavra encontrada e está na ordem correta
    if (s == palavra[::-1]):
        return 2        # palavra encontrada e está invertida
    return 0    # não foi encontrada

# -----------------------------------------------------

for y in range(m):
    for x in range(n):
        for f in range (len(found)):
            if (found[f] == 0):     # ainda temos de encontrar
                if (check_horizontal(palavras[f], x, n) == 1):
                    z = find_horizontal(palavras[f], x, y, tabuleiro)
                    if (z == 1):
                        resp[f] = [(y+1,x+1),(y+1, x+len(palavras[f]))]
                        found[f] = 1
                    elif (z == 2):
                        resp[f] = [(y+1, x+len(palavras[f])), (y+1,x+1)]
                        found[f] = 1
                if (check_vertical(palavras[f], y, m) == 1):
                    z = find_vertical(palavras[f], x, y, tabuleiro)
                    if (z == 1):
                        resp[f] = [(y+1,x+1), (y+len(palavras[f]), x+1)]
                        found[f] = 1
                    elif (z == 2):
                        resp[f] = [(y+len(palavras[f]), x+1), (y+1,x+1)]
                        found[f] = 1
                if (check_diagonal_1(palavras[f], x, y, m, n) == 1):
                    z = find_diagonal_1(palavras[f], x, y, tabuleiro)
                    if (z == 1):
                        resp[f] = [(y+1,x+1), (y+len(palavras[f]), x+len(palavras[f]))]
                        found[f] = 1
                    elif (z == 2):
                        resp[f] = [(y+len(palavras[f]), x+len(palavras[f])), (y+1,x+1)]
                        found[f] = 1
                if (check_diagonal_2(palavras[f], x, y, m) == 1):
                    z = find_diagonal_2(palavras[f], x, y, tabuleiro)
                    if (z == 1):
                        resp[f] = [(y+1,x+1), (y+len(palavras[f]), x+2-len(palavras[f]))]
                        found[f] = 1
                    elif (z == 2):
                        resp[f] = [(y+len(palavras[f]), x+2-len(palavras[f])), (y+1, x+1)]
                        found[f] = 1


for j in range(len(palavras)):
    s = ""
    i = 0
    for tuplo in resp[j]:
        for coordinates in tuplo:
            if (i == 0):
                s += str(coordinates)
            else:
                s += " " + str(coordinates)
            i+=1
    print(s)