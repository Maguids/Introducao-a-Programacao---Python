# Bacalhaus Congelados

nos, trocos = map(int, input().split())
dict = {}
for i in range(trocos):
    x1, x2, t, c = map(int,input().split())
    dict[(x1,x2)] = t

percursos = []
p = list(map(int, input().split()))
while (p[0] != 0):
    percursos.append(p)
    p = list(map(int, input().split()))

def find_max(v1, v2):
    if (v1 >= v2):
        return v1
    return v2

def find_min(v1, v2):
    if (v1 <= v2):
        return v1
    return v2

for p in percursos:
    index = p[0]
    for i in range(1,index):
        x1 = p[i]
        x2 = p[i+1]
        if ((x1,x2) in dict):
            if(i == 1):
                min = dict[(x1,x2)]
                max = dict[(x1,x2)]
            else:   
                min = find_min(min, dict[(x1,x2)])
                max = find_max(max, dict[(x1,x2)])
        elif ((x2,x1) in dict):
            if(i == 1):
                min = dict[(x2,x1)]
                max = dict[(x2,x1)]
            else:   
                min = find_min(min, dict[(x2,x1)])
                max = find_max(max, dict[(x2,x1)])
    print(min,max)