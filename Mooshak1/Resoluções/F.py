# Preciosismos

h1, m1 = list(map(int,input().split()))
h2, m2 = list(map(int,input().split()))

t1 = h1 * 60 + m1   # total minutos encontro 1
t2 = h2 * 60 + m2   # total minutos encontro 2
d = t2 - t1     # diferença em minutos dos dois encontro

if (d//60 == 0):
    if (d == 1):
        print("Passou apenas 1 minuto!")
    else:
        print("Passaram apenas %d minutos!" %(d))
    print("De facto!")
else:
    print("Passaram apenas %d minutos!" %(d))
    s = "Queres dizer,"
    h = d // 60 # horas
    m = d % 60  # minutos
    if (h == 1):
        s += " 1 hora"
    else:
        s += " " + str(h) + " horas"
    if (m == 1):
        s += " e 1 minuto"
    elif (m > 1):
        s += " e " + str(m) + " minutos"
    s += "?!"
    print(s) 



