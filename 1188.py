t = input()
l = [0]*12
a = []
for i in range(12):
    l[i] = [0]*12


for i in range(12):
    for j in range(12):
        l[i][j] = float(input())
        
sup = 11
inf = 1 
for i in range(5):
    for j in range(inf,sup):
        a.append(l[i][j])
    sup -=1
    inf+=1
       
if t == "S":
    print(("%.1f")%(sum(a)))
else:
    print(("%.1f")%(sum(a)/len(a)))
