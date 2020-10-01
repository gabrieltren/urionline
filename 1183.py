l = [0]*12
for i in range(0,12):
    l[i] = [0]*12

t = input()

for i in range(0,12):
    for j in range(0,12):
        l[i][j] = float(input())

s = float(0)

for i in range(0,11):
    for j in range(i+1,12):
        s+= l[j][i]

if t == 'S':
    print("{:.1f}" .format(s))
else:
    ac = s/66
    print("{:.1f}" . format(ac))