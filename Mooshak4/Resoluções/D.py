# Reservas

n, r = map(int, input().split())    # n = número de nós, r = numero de ligações
ligacoes = {}   # dicionário que guarda as ligações possiveis, os lugares disponiveis e o preço
for i in range(r):
    i, f, d, b = map(int, input().split())  #i = inicio, f = fim, d = lugares disponiveis, b = preço bilhete
    ligacoes[(i,f)] = [d, b]

def pedido_possivel(l, n_p, p, bilhetes):
    for i in range(n_p-1):
        if((p[i],p[i+1]) not in l): # não é possivel porque um determinado trajeto não existe
            s = "(" + str(p[i]) + "," + str(p[i+1]) +") inexistente"
            return s
        else:
            if (l[(p[i],p[i+1])][0] - bilhetes < 0):
                s = "Sem lugares suficientes em (" + str(p[i]) + "," + str(p[i+1]) + ")"
                return s
    return "POSSIVEL"


t = int(input())    # número de reservas a processar
for i in range(t):
    info = list(map(int, input().split()))
    n_bilhetes = info[0]    # número de bilhetes pedidos
    p = info[1] # número de nós do percurso
    percurso = info[2:]
    ans = pedido_possivel(ligacoes, p, percurso, n_bilhetes)
    if (ans != "POSSIVEL"):
        print(ans)
    else:
        pagar = 0
        for j in range(p-1):
            ligacoes[(percurso[j],percurso[j+1])][0] -= n_bilhetes
            pagar += n_bilhetes * ligacoes[(percurso[j],percurso[j+1])][1]
        print("Total a pagar: %d" %(pagar))
