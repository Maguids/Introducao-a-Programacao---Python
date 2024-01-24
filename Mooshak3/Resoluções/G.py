# Trilhos de números

#------------- funções auxiliares -------------
def create_visited(l, c):
    v = []
    for i in range(l):
        temp = []
        for j in range(c):
            temp.append(0)
        v.append(temp)
    return v

def possible_move(x, y,directions, d, c, l):    # vê se é possivel realizar o movimento, ou seja, se não sai do tabuleiro (d = direção)
    encX, encY = directions[d]      # vai buscar os encrementos necessários para realizar o movimento
    newX = x + encX
    newY = y + encY
    if (newX < 0 or newX >= c):
        return 0    # fora dos limites do x
    if(newY < 0 or newY >= l):
        return 0    # fora dos limites do y
    return 1    # movimento possivel
#------------- fim ------------------------------

l, c = map(int, input().split())    # l = linhas, c = colunas
tabuleiro = [list(map(int, input().split())) for i in range(l)]     # tabuleiro do jogo
n = tabuleiro[0][0]     # número inicial / número que temos de procurar sempre
visited = create_visited(l, c)     # marca os sitios que já foram visitados
sum = n    # soma de todos os números do trilho

x, y = 0,0      # posição onde nos encontramos
visited[0][0] = 1   # visitamos o primeiro local
control = 1     # enquanto houver mais movimentos control = 1
directions = {'C':(0,-1), 'B': (0,1), 'D':(1,0), 'E':(-1,0)}
moves = ['C', 'B', 'D', 'E']
path = ""
while (control == 1):
    possible = 0
    for d in moves:
        if (possible_move(x, y, directions, d, c, l) == 1):     # movimento é possivel (dentro dos limites)
            newX = x + directions[d][0]
            newY = y + directions[d][1]
            if (tabuleiro[newY][newX] == n and visited[newY][newX] == 0):
                possible = 1
                keeper = [newX, newY, d]

    if (possible == 1):
        x = keeper[0]
        y = keeper[1]
        path += keeper[2]
        sum += n
        visited[y][x] = 1
    else:
        control = 0

print(path)
print(sum)
    