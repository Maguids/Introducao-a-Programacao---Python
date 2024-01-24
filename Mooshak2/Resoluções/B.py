# Compras onçine com cupão

c, n = list(map(int,input().split()))   # c = valor do cupão, n = número de artigos
pagar = 0   # valor total pagar
novoC = c   # valor do novo cupão (vai se descontando as compras aceites)
ans = ""    # guarda os itens comprados

for i in range (n):
    preco = int(input())
    s = str(input())
    if (novoC-preco >= 0):
        novoC -= preco
        pagar += preco
        if (len(ans) != 0):
            ans += "\n" + s
        else:
            ans += s

if (len(ans) != 0):
    print(ans)
print("%d %d" %(pagar, novoC))