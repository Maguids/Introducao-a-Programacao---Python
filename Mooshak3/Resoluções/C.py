# ET em estado de choque!

# NOTA: apesar de no enunciado dizer que a leitura do input é dada numa única linha separada por espaços e que termina com "#"
#       a prof faz os testes de modo a que o programa reconheça os caracteres um am cada linha e temonha quando aparece "#"
#       s = list(map(str, input().split()))     # leitura do ADN do ET (tudo na mesma linha separado por espaços)
s = []
char = str(input())
while (char != '#'):
    s.append(char)
    char = str(input())

ans = s[0]  # manter a primeira letra
len = len(s)

for i in range(len-1):
    if (s[i] == s[i+1]):
        ans += s[i]
    elif ((s[i] == 'a' and s[i+1] == 'c') or (s[i] == 'c' and s[i+1] == 'a')):
        ans += 't'
    elif ((s[i] == 'a' and s[i+1] == 't') or (s[i] == 't' and s[i+1] == 'a')):
        ans += 'c'
    elif ((s[i] == 't' and s[i+1] == 'c') or (s[i] == 'c' and s[i+1] == 't')):
        ans += 'a'


for x in ans:
    print(x)
