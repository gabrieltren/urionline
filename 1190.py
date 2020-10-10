t = input()
l = [0]*12
a = []
for i in range(12):
    l[i] = [0]*12


for i in range(12):
    for j in range(12):
        l[i][j] = float(input())
        

cfin = 11
for i in range(1,11):
    for j in range(cfin,12):
        a.append(l[i][j])
    if i < 5:
        cfin -= 1
    if i > 5:
        cfin += 1
       
if t == "S":
    print(("%.1f")%(sum(a)))
else:
    print(("%.1f")%(sum(a)/len(a)))
