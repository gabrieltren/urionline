t = float(input())

x = [] 
for i in range(0,100):
    x.append(float(t))
    t/=2
    print("N[{}] = {:.4f}" .format(i,x[i]))