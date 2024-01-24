# CaixaNegra

n = int(input())    # n números

x1 = int(input())
x2 = int(input())
x3 = int(input())
if (x2 > x1*2 and x2 > x3*2):
    counter = 1
else:
    counter = 0

for i in range(3,n):
    x1 = x2
    x2 = x3
    x3 = int(input())
    if (x2 > x1*2 and x2 > x3*2):
        counter += 1

print(counter)