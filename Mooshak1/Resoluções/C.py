# Problemas de Agenda

d = int(input())    # duração
i1,f1 = list(map(int, input().split())) # inicio e fim da pessoa 1
inicio = i1
fim = f1
i2,f2 = list(map(int, input().split())) # inicio e fim da pessoa 2

if (f1 <= i2 or f2 <= i1):      #os conjuntos não se intersetam
    print("Impossivel")
else:
    if(inicio < i2): inicio = i2    # determinar inicio da interseção do intervalo
    if(fim > f2): fim = f2      # determinar fim da interseção do intervalo
    
    ultimo_horário = fim - d    # útlima hora possivel de começar a rewunião
    if (ultimo_horário < inicio):
        print("Impossivel")
    elif (ultimo_horário == inicio):
        print(inicio)
    else:
        print(inicio, ultimo_horário)

    
