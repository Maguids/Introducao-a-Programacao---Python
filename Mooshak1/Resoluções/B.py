# Febre!!!

i1,d1,i2,d2 = list(map(int, input().split()))   # valores do input
t1 = i1 + d1/10     #temperatura 1
t2 = i2 + d2/10     #temperatura 2
febre = 37.0  # valor que indica febre

if (t2 < febre):
    print("NORMAL")
else:
    if (t1 == t2):
        print("FEBRE MANTEVE")
    elif (t1 > t2):
        print("FEBRE BAIXOU")
    else:
        print("FEBRE SUBIU")