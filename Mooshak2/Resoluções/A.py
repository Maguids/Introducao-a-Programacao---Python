# Reunião

n = int(input())    # número de intervalos

control = 1     # se ficar zero é porque há algum intervalo que não faz interseções com os outros

for i in range (n):
    if (i == 0):    # apanhar o primeiro caso
        inicio, fim = list(map(int,input().split()))
    else:       # todos os outros
        i, f = list(map(int,input().split()))
        if (i > fim or f < i):
            control = 0     # não há interseção entre os conjuntos
        else:
            # redefinir um novo conjunto
            if (i > inicio):
                inicio = i
            if (f < fim):
                fim = f

if (control == 0):
    print("impossivel")
else:
    if ((inicio+fim)%2 == 0):
        print("%d" %((inicio+fim)/2))
    else:
        print("%d e meia" %((inicio+fim)//2))
        

