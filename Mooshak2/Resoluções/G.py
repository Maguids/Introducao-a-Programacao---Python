# Medições Adocicadas

def count_negative(i, seq, n):      # conta o número de -1 seguidos que há e a primeira posição em que deixa de haver
    counter = 0
    while (i <= n-1 and seq[i] == -1):
        counter += 1
        i += 1
    return i, counter

def create_keeper(p, c, k, s, n):       # cria uma sequencias que guarda os valores escrito e uma soma dos 'apagados'
    if (c == 0):
        k.append(s[p])
    else:
        k.append(-c)
        if (p < n):
            k.append(s[p])
    
    if (p+1 >= n):
        return keeper
    else:
        p1, c1 = count_negative(p+1, s, n)
        print("p = ", p1, " c = ", c1)
        return create_keeper(p1, c1, k, s, n)

def consecutivos(seq, n):
    variancias = []
    for i in range (n-1):
        if (seq[i] >= 0 and seq[i+1] >= 0):
            var = seq[i+1] - seq[i]
            variancias.append(var)
    return variancias


n = int(input())    # número de dados
seq = list(map(int, input().split()))   # lista que guarda os dados
pos, counter = count_negative(0, seq, n)     # primeira posição != de -1, caso a primeira posição não seja != de zero sabemos quantos -1 há antes
keeper = []


if (pos >= n):
    print("Possivel")
else:
    keeper = create_keeper(pos,counter,keeper, seq, n)


