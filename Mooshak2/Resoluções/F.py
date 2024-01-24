# Convites para amigos

#------------ funções a serem utilizadas -----------
def min(lista, n):         # função que encontra o mínimo
    k = 0
    while(k <= n-1 and lista[k] == 0):
        k += 1
    if (k == n):
        return 0
    else:
        min = lista[k]
        for x in lista:
            if (x < min and x != 0):
                min = x
        return min
    
def count_pessoas(lista):
    counter = 0
    for x in lista:
        if(x != 0):
            counter += 1
    return counter
    
def update(lista, n, keeper, valor):    # dá update aos dados todos
    for i in range(n):
        if (lista[i] >= valor):
            keeper[i] += valor
            lista[i] -= valor
    return lista, keeper

def diminuir_min(lista, n):
    for i in range(n):
        if (lista[i] != 0):
            lista[i] -= 1
    return lista

def compare_lists(p, o, k, n):  
    for i in range (n):
        if (p[i] == 0 and o[i] != k[i]):
            return 0    # errado
    return 1

#----------- Enunciado ---------
b = int(input())    # número de bilhetes disponiveis
n = int(input())    # número de amigos
oferecido = n*[0]
total = 0           # total de bilhetes pedidos
pedido = []     # lista que guarda quantos bilhetes pediu cada amigo
for i in range(n):
    x = int(input())
    total += x
    pedido.append(x)
keeper = pedido[:]     # guarda os pedidos mas esta lista não vai sofrer alterações

if (total <= b):    # todos tem o que pediram
    oferecido = pedido
elif (n > b):
    oferecido = n * [0]
else:
    control = 1     # enquanto control == 1 ainda dá para dar mais bilhetes
    while (control == 1):
        pessoas = count_pessoas(pedido)     # pessoas que sofrem alterações (ainda se lhes podem ser dados bilhetes)
        m = min(pedido, n)     # valor mínimo pedido
        if (m == 0):
            control = 0
        elif (m * n <= b):
            pedido, oferecido = update(pedido, n, oferecido, m)
            b -= m * pessoas
        elif (m * pessoas <= b):
            if (compare_lists(pedido, oferecido, keeper, n) == 0):
                control = 0
            else:
                pedido, oferecido = update(pedido, n, oferecido, m)
                b -= m * pessoas
        elif (m * pessoas > b):
            pedido = diminuir_min(pedido, n)

for x in oferecido:
    print(x)