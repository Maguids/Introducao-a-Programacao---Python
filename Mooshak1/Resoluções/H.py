# Quem almoça de graça?

f = int(input())    # número fixado por todos
n = int(input())    # número de amigos
keeper = 1
control = 0

for i in range (n):
    e = int(input())
    if (e <= f and e >= keeper):
        keeper = e
        control = 1

if (control == 1):
    print(keeper)
else:
    print("No free lunch")