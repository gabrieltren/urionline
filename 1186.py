t = input()
l = [0]*12
a = []
for i in range(12):
    l[i] = [0]*12
d = int(1)
c = int(13)
for i in range(12):
    for j in range(12):
        l[i][j] = float(input())

for i in range(12):
    c -=1
    for j in range(c,12,1):
        a.append(l[j][i])
        
if t == "S":
    print(("%.1f")%(sum(a)))
else:
    print(("%.1f")%(sum(a)/len(a)))
