# Anagramas

s1 = str(input())
s2 = str(input())

def tratamento(s):      # deixa apenas char que sejam letras e transforma-as em minúsculas (elemina espaços e caracteres não letras)
    s = s.lower()   # transforma a string em lower case
    ans = ""
    for ch in s:
        if (ch.isalpha()):  # vê se o char faz parte do alfabeto
            ans += ch
    return ans

s1 = tratamento(s1)
s2 = tratamento(s2)

if (len(s1) != len(s2)):
    print("no")
else:
    # vamos eliminando as letras que encontramos iguas a s1 em s2
    control = 1     # supomos que é anagrama se não for control = 0
    for ch in s1:
        if (s2.find(ch) != -1):
            s2 = s2.replace(ch, '0', 1)      # trocamos apenas a primeira ocorrencia
        else:
            control = 0

    if (control == 0):
        print("no")
    else:
        print("yes")
