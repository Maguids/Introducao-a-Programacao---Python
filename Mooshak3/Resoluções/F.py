# Segredos mal guadados

g = int(input())    # número de gavetas
estado = [str(input()) for i in range(g)]   # ler os inputs a partir de uma lista em compressão
estado = estado[::-1]   # inverter a ordem da lista para que na posição 0 fique a gaveta mais em baixo

counter = 0   # conta o número de gavetas que estão inacessiveis
for i in range(g-1):    # vemos a última gaveta apenas fora do ciclo
    if (estado[i] == "#" and estado[i+1] == "#"):      # então a gaveta está fechada e a de cima também, logo não se consegue abrir
        counter += 1

if (estado[g-1] == "#"):    # não conseguimos abrir a ultima gaveta
    counter += 1

print(counter)