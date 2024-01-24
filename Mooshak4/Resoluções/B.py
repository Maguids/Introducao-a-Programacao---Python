# Mapa sem sentidos únicos

n_trajetos, n_nos = map(int, input().split())
paragens = {}   # guarda todas as paragens de todos os trajetos

s = ""
for i in range(n_trajetos):
    temp = list(map(int, input().split()))
    soma = 0
    for j in range (1,temp[0]*2-2,2):   # se a posição for divisivel por 2 é paragens senão é distancia
        paragens[(temp[j], temp[j+2])] = 1
        paragens[(temp[j+2], temp[j])] = 1
        soma += temp[j+1]
    if (i != n_trajetos-1):
        s += "Trajeto " + str(i+1) + ": " + str(soma) + "\n"
    else:
        s += "Trajeto " + str(i+1) + ": " + str(soma)

print(s)
for x in range(1, n_nos+1):
    counter = 0
    for y in range(1, n_nos+1):
        if ((x,y) in paragens or (y,x) in paragens):
            counter += 1
    print("No %d: %d" %(x, counter))
