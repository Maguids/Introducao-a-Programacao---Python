# Psittacus Erithacus

patas2 = ["piupiu", "cocorocoo", "cacaraca", "quaqua", "jaco"]
patas4 = ["muuu", "miao","auau", "meemee"]

total = 0
minimo = 0      # todos os sons com 'Jaco', todos aqueles em que o som não corresponde ao número de patas
maximo = 0      # todos os sons de animais com duas patas e cujo som de um animal de 4 não está correto

s = str(input())
while (s != "0"):
    patas = s[0]
    sons = s[2:]

    control = 0     # se control = 0 foi o Jacó
    if (sons == "jaco"):
        control = 0
        maximo += 1
    elif (patas == '2'):
        maximo += 1
        for som in patas2:
            if(som == sons):
                control = 1
    elif (patas == '4'):
        for som in patas4:
            if (som == sons):
                control = 1
        if (control == 0):
            maximo += 1

    if (control == 0):
        minimo += 1
    total += 1
    s = str(input())

print(total, minimo, maximo)