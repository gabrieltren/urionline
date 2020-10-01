x = []
for i in range(0,10):
    a = int(input())
    x.append(a)

for i in range(0,10):
    if x[i] > 0:
        print("X[{}] = {}" .format(i,x[i]))
    else:
        print("X[{}] = 1" .format(i))