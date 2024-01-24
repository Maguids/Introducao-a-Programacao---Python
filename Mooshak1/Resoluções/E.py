# Minuto Verde

azul = 0
verde = 0
amarelo = 0

x = int(input())
while (x != -1):
    if (x <= 10 and x >= 1):
        azul += 1
    elif (x <= 23 and x >= 11):
        verde += 1
    elif (x <= 40 and x >= 24):
        amarelo += 1
    x = int(input())
print("azul: %d\namarelo: %d\nverde: %d" %(azul, amarelo, verde))