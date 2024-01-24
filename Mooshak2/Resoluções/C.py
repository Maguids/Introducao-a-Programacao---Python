# Campeonato de Telepatia

n = int(input())
leigo = list(map(int,input().split()))
telepata = list(map(int,input().split()))

certas = 0  # conta o número de acertos
pontuacao = 0 # guarda a pontuação
seq = 0  

l1 = leigo[1]
t1 = telepata[1]

if (leigo[0] == telepata[0] and l1 == t1):
    pontuacao += 3
    certas += 1
    seq += 1 
elif (leigo[0] == telepata[0]):
    pontuacao += 1
    certas += 1
    seq = 0

for i in range (2, n):
    l2 = leigo[i]
    t2 = telepata[i]

    if (l1 == t1 and l2 == t2):
        pontuacao += 3
        certas += 1
        seq += 1
    else:
        if (seq != 0):
            if (l1 == t1):
                pontuacao += 3
                certas += 1
            seq = 0
        else:
            if (l1 == t1):
                pontuacao += 1
                certas += 1
                seq = 1
    l1 = l2
    t1 = t2


if (l1 == t1 and seq != 0):
    pontuacao += 3
    certas += 1
    seq = 0
elif (l1 == t1):
    pontuacao += 1
    certas += 1

print(certas)
print(pontuacao)


       

