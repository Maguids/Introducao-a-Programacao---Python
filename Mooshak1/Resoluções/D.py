# Vai subir?

chamada, e1, e2 = list(map(int, input().split()))   #andar da chamada, elevador 1, elevador 2

if (e1 == 999 and e2 == 999):
    print(0)
elif (e1 == 999):
    print(2)
elif (e2 == 999):
    print(1)
else:
    d1 = chamada - e1   #diferença entre chamada e e1
    d2 = chamada - e2   #diferença entre chamada e e2
    if (d1 == d2):  #estão no mesmo piso
        print(1)
    elif (abs(d1) == abs(d2)):  #estão à mesma distância
        if (d1 < d2):
            print(1)
        else:
            print(2)
    elif (abs(d1) > abs(d2)):
        print(2)
    elif (abs(d1) < abs(d2)):
        print(1)