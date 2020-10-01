x = []
for i in range(0,100):
    a = float(input())
    x.append(a)

for i in range(0,100):
    if x[i] <= 10:
        print("A[{}] = {}" .format(i,x[i]))