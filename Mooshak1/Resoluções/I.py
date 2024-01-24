# Temperaturas

moderado, n = list(map(int, input().split()))
keeper = 0  # guarda a maior sequencia se temperaturas moderadas
counter = 0     # conta a sequencia atual de dias consecutivos 

for i in range(n):
    x = int(input())
    if (x >= moderado-2 and x <= moderado+2):
        counter += 1
    else:
        if (counter > keeper):
            keeper = counter
        counter = 0

if (counter > keeper):
    keeper = counter

if (keeper == 0):
    print("Sem registo de temperaturas moderadas")
elif (keeper == 1):
    print("Temperaturas moderadas apenas em dias isolados")
else:
    print("Durante %d dias consecutivos, temperaturas moderadas" %(keeper))