# Salta Lajes

c, l = map(int,input().split())     # c = comprimento máximo, l = número de lajes
lajes = []  # guarda os valores das lajes
for i in range (l):  
    lajes.append(int(input()))

pe = 1  # se p == 1 salto com o pé direito se p == -1 salto com o pé esquerdo
p = -1  # posição (inicialmete -1 fora das lajes)
pontuacao = 0

def min(x1, p1, x2, p2):
    if (x1 <= x2):
        return x1, p1
    else:
        return x2, p2

def max(x1, p1, x2, p2):
    if (x1 <= x2):
        return x2, p2
    else:
        return x1, p1
        

while (p < l):
    if (pe == -1):
        for i in range (1, c+1):     
            if (p+i >= l):      # o jogo acaba
                p = l+1
            elif (i == 1):
                valor_min = lajes[p+i]
                pos = p+i
            else:
                valor_min, pos = min(valor_min, pos, lajes[p+i], p+i)
        if (p != l+1):
            p = pos
            pontuacao -= valor_min
    else:
        if (p+1 >= l):  # não tem para onde saltar
            p = l + 1
        else:
            for i in range (1, c+1):
                if (p+i >= l):
                    continue
                elif (i == 1):
                    valor_max = lajes[p+1]
                    pos = p+1
                else:
                    valor_max, pos = max(valor_max, pos, lajes[p+i], p+i)
            p = pos
            pontuacao += valor_max
    pe *= -1

print(pontuacao)

                


                