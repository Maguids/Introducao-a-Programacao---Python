# Somando

n = int(input())    # n números da sequencia

soma = 0     # soma os numeros que satisfazem as condições
counter = 0     # conta os valores lidos

x1 = int(input())
x2 = int(input())

for i in range (n-2):
    x = int(input())
    if (x == 0):
        continue
    elif (x != x1 and x != x2 and (x % x2 == 0 or x > x1)):
        soma += x
        counter += 1

if (counter == 0):
    print("Resposta G - nenhum valor satisfaz")
else:
    print("Resposta G - soma: %d" %(soma))