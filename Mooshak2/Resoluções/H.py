# Sentar ou não sentar

def chair(tipo, tipos, numeros):    # vê se a cadeira está disponivel, se está devolve 1 e remove 1 cadeira, se não está devolve 0
    i = 0
    for x in tipos:
        if (x == tipo):
            if (numeros[i] > 0):
                numeros[i] = numeros[i] - 1
                return 1
        i += 1
    return 0


n_tipos = int(input())  # tipos de cadeira
t = []   # tipo cadeira
v = []     # número de cadeiras do tipo
for i in range(n_tipos):
    t.append(int(input()))
    v.append(int(input()))

n_habitantes = int(input())     # número de habitantes de cada reino
counter = 0     # número de habitantes de pé
for j in range (n_habitantes):
    n_pref = int(input())
    if (n_pref == 0):
        counter += 1
    else:
        control = 0
        for k in range(n_pref):
            x = int(input())
            if (control == 0):
                if (chair(x, t, v) == 1):
                    control = 1
        
        if (control == 0):
            counter += 1

sobras = 0
for x in v:
    sobras += x
print("%d" %(counter))
print("%d" %(sobras))               
