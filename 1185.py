t = input()
l = [0]*12
a = []
for i in range(12):
    l[i] = [0]*12

c = int(12)
for i in range(12):
    for j in range(12):
        l[i][j] = float(input())
for i in range(12):
    c -=1
    for j in range(c):
        a.append(l[j][i])
        
if t == "S":
    print(("%.1f")%(sum(a)))
else:
    print(("%.1f")%(sum(a)/len(a)))
