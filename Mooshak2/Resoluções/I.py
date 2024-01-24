# Não lhes dês troco

def up_quantidade(m, q, x):
    i = 0
    for j in m:
        if (j == x):
            q[i] += 1
        i += 1

def troco_euros(m, q, e):
    end = 0
    i = 0
    while(end == 0 and i != 2):
        if (q[i] != 0):
            e -= m[i]
            q[i] -= 1
        else:
            i += 1


moedas = [200, 100, 50, 20 , 10, 5]
quantidades = list(map(int, input().split()))

e, c = map(int, input().split())
dado = 6*[0]
x = int(input())
while (x != 0):
    up_quantidade(moedas, quantidades, x)
    x = int(input())
