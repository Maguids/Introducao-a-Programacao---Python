# Manual de Sobrevivência

s = str(input())    # lê a linha em forma de string
s = s.lower()   # torna-mos a string toda em minúsculas

def count_x(s, x):      # conta o número de ocorrencias de um char x
    counter = 0
    for ch in s:
        if (ch == x):
            counter += 1
    return counter

print(count_x(s, 'p'))