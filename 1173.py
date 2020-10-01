c = int(input())
x = []
x.append(c)
print("N[0] = {}" .format(x[0]))
c*=2
for i in range(1,10):
    x.append(c)
    c*=2
    print("N[{}] = {}" .format(i,x[i]))
