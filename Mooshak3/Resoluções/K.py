# Caçada aos Gambozinos

# -------------- NOTAS --------------   0 - vazio   1 - marcado c - centro
#   Tipo1   Tipo2   Tipo3   Tipo4   Tipo5
#   0 1 0   0 1 0   1 1 0   0 0 1   0 1 0
#   0 c 1   1 c 0   0 c 1   1 c 1   1 c 1
#   1 1 0   0 1 1   0 1 0   0 1 0   1 0 0
#

def type1(x, y, tabuleiro):
    return tabuleiro[y-1][x]==1 and tabuleiro[y][x+1]==1 and tabuleiro[y+1][x]==1 and tabuleiro[y+1][x-1]==1 

def type2(x, y, tabuleiro):
    return tabuleiro[y-1][x]==1 and tabuleiro[y][x-1]==1 and tabuleiro[y+1][x]==1 and tabuleiro[y+1][x+1]==1

def type3(x, y, tabuleiro):
    return tabuleiro[y-1][x-1]==1 and tabuleiro[y-1][x]==1 and tabuleiro[y][x+1]==1 and tabuleiro[y+1][x]==1

def type4(x, y, tabuleiro):
    return tabuleiro[y-1][x+1]==1 and tabuleiro[y][x-1]==1 and tabuleiro[y][x+1]==1 and tabuleiro[y+1][x]==1

def type5(x, y, tabuleiro):
    return tabuleiro[y-1][x]==1 and tabuleiro[y][x-1]==1 and tabuleiro[y][x+1]==1 and tabuleiro[y+1][x-1]==1

def update_type1(x, y, tabuleiro):
    tabuleiro[y][x], tabuleiro[y-1][x], tabuleiro[y][x+1], tabuleiro[y+1][x], tabuleiro[y+1][x-1] = 0
    return tabuleiro

def update_type2(x, y, tabuleiro):
    tabuleiro[y][x] = 0
    tabuleiro[y-1][x] = 0 
    tabuleiro[y][x-1] = 0
    tabuleiro[y+1][x] = 0
    tabuleiro[y+1][x+1] = 0
    return tabuleiro

def update_type3(x, y, tabuleiro):
    tabuleiro[y][x] = 0
    tabuleiro[y-1][x-1] = 0 
    tabuleiro[y-1][x] = 0 
    tabuleiro[y][x+1] = 0 
    tabuleiro[y+1][x] = 0
    return tabuleiro

def update_type4(x, y, tabuleiro):
    tabuleiro[y][x] = 0
    tabuleiro[y-1][x+1] = 0 
    tabuleiro[y][x-1] = 0 
    tabuleiro[y][x+1] = 0 
    tabuleiro[y+1][x] = 0
    return tabuleiro

def update_type5(x, y, tabuleiro):
    tabuleiro[y][x] = 0
    tabuleiro[y-1][x] = 0 
    tabuleiro[y][x-1] = 0 
    tabuleiro[y][x+1] = 0 
    tabuleiro[y+1][x-1] = 0
    return tabuleiro


m, n = map(int, input().split())    # m = linhas, n = colunas
tabuleiro = [list(map(int, input().split())) for i in range(m)]
counter = 0     # conta o  número de gambozinos

# como a partir daqelas funções apenas observo a partir do centro dos gambozinos e a borda do tabuleiro só tem 0's
# basta começar a minha pesquisa a partir da desunda linha e da segunda coluna

for y in range(2,m-1):
    for x in range(2, n-1):
        if (tabuleiro[y][x] == 1):
            if (type1(x,y,tabuleiro) == 1):
                tabuleiro = update_type1(x,y,tabuleiro)
                counter += 1
            elif (type2(x,y,tabuleiro) == 1):
                tabuleiro = update_type2(x,y,tabuleiro)
                counter += 1
            elif (type3(x, y, tabuleiro) == 1):
                tabuleiro = update_type3(x,y,tabuleiro)
                counter += 1
            elif (type4(x, y, tabuleiro) == 1):
                tabuleiro = update_type4(x,y,tabuleiro)
                counter += 1
            elif (type5(x, y, tabuleiro) == 1):
                tabuleiro = update_type5(x,y,tabuleiro)
                counter += 1

print(counter)
