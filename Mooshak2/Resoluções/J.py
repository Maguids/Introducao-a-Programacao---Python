# Cigarras Tontas

percurso = []
p = int(input())
n = 0   # número de 'paragens'
while (p != 0):
    percurso.append(p)
    p = int(input())
    n += 1

novo = []   # gurada o percurso final
novo.append(percurso[0])
end = 0
posN = 0    # posiçaõ na lista nova
posP = 0    # posição no percurso
while (end == 0):
    pos = posP
    x = novo[posN]
    for i in range(pos, n):
        if (x == percurso[i]):
            posP = i
    
    if (posP == n-1):
        end = 1
    elif (pos == posP):
        posP += 1
        novo.append(percurso[posP])
        posN += 1
    else:
        posP += 1
        novo.append(percurso[posP])
        posN += 1

for resp in novo:
    print(resp)

