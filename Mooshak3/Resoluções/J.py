# Casamentos Perfeitos


def resolver(s):
    abertos = []    # lista que vai guardar tuplos com o tipo de parenteses e a sua posição
    start = 0
    fechados = []   # guarda a sublistas com os parenteses e as suas posições
    pares = {'(': ')', '[': ']', '{': '}'}
    for i in range(len(s)):
        if (s[i] in "({["):   # se encontrar um parenteses aberto mete na lista aberto
            abertos.append((s[i], i))
            start = 1
        elif (s[i] in ")}]") :
            if (len(abertos) == 0):
                return 0, fechados
            elif (s[i] != pares[abertos[-1][0]]):
                return 0, fechados
            else:
                key = abertos[-1][0]+s[i]
                place = str(abertos[-1][1]) + " " + str(i)
                fechados.append((key,place))
                abertos = abertos[:-1]

    if (start == 0):
        return 2, fechados
    elif (len(abertos) == 0):
        return 1, fechados
    else:
        return 0, fechados


s = str(input())    # lê o input
ans, f = resolver(s)

if (ans == 0):
    print("Pares mal formados")
elif (ans == 1):
    for valores in f:
        key, place = valores
        print(key, place)
else:
    print("Sem noivos para casar")