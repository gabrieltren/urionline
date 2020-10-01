x = []
for i in range(0,20):
    a = int(input())
    x.append(a)
aux = x[0]
x[0] =x[19]
x[19] = aux

for i in range(1,10,1):
    aux = x[i]
    x[i] = x[19-i]
    x[19-i] = aux
    
for i in range(0,20):
    print("N[{}] = {}" .format(i,x[i]))