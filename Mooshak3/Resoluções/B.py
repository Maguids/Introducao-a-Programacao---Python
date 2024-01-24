# Preservação Digital

n, m = map(int, input().split())    # n = linhas    m = colunas
files = []
for i in range(n):
    temp = list(str(input()))
    files.append(temp)

ans = ""    # vai guardar a repsosta

def escolha(v):     # escolhe o que acrescentar a 'ans', tendo em conta o número de 1's e 0's
    if (v[0] >= v[1]):
        return '0'
    return '1'

for j in range(m):
    valores = [0,0]
    for k in range(n):
        if (files[k][j] == '0'):
            valores[0] += 1
        else:
            valores[1] += 1
    ans += escolha(valores)

print(ans)