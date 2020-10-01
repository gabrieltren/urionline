t = int(input())

x = [] 
for i in range(0,1000):
    x.append(i % t)
    print("N[{}] = {}" .format(i,x[i]))