# Miradouros 

# dicionário que guarda a localização de cada sitio
cidades = {'ARCO DA VILA': 'Faro', 'GRACA': 'Lisboa', 'IGREJA DOS GRILOS': 'Porto',
            'JARDINS DO PALACIO DE CRISTAL': 'Porto', 'MONTE AGUDO': 'Lisboa', 'MONTE DE FARO': 'Faro',
            'PENHA DE FRANCA': 'Lisboa', 'SANTA CATARINA': 'Lisboa', 'SANTA LUZIA': 'Lisboa', 'SAO JORGE': 'Lisboa', 
            'SAO PEDRO DE ALCANTARA': 'Lisboa', 'SE CATEDRAL': 'Porto', 'SENHORA DO MONTE': 'Lisboa',
            'SERRA DO PILAR': 'Porto', 'TORRE DOS CLERIGOS': 'Porto', 'VITORIA': 'Porto'}

visitas = {}    # vai guardar o nome do sítio e a quantidade de visitas

n_visitas = 0   # guarda o número total de visitas
temp = str(input())
while (temp != 'FIM'):
    n_visitas += 1
    if (temp in visitas):
        visitas[temp] += 1
    else:
        visitas[temp] = 1
    temp = str(input())

# procurar o/os local/locais mais visitado(s)
def encontrar_maior(d):
    maior = 0
    for local in d:
        if (d[local] > maior):
            maior = d[local]
            keeper = []
            keeper.append(local)
        elif (d[local] == maior):
            keeper.append(local)
    return maior, keeper

m, k = encontrar_maior(visitas)
print(n_visitas, m)
k = sorted(k)
for place in k:
    print(place, cidades[place])