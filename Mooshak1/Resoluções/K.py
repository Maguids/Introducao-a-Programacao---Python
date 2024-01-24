# Ali Baba e a Biometria

x, y = list(map(int,input().split()))
keeper = 0
counter = 0

while(x != -1 and y != -1):
    if (x == 1 and y == 1):
        counter += 1
    elif (x == 1 and y == 0):
        if (counter > keeper):
            keeper = counter
        counter = 0
            
        a = int(input())    # só tem um valor

        while (a == 0):
            a = int(input())


    x, y = list(map(int,input().split()))

if (counter > keeper):
    keeper = counter
print(keeper)