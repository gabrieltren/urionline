l = [0]*12
for i in range(0,12):
    l[i] = [0]*12

c = int(input())
t = input()

for i in range(0,12):
    for j in range(0,12):
        l[i][j] = float(input())

s = float(0)

for i in range(0,12):
    s += l[i][c]

if t == 'S':
    print("{:.1f}" .format(s))
else:
    print("{:.1f}" . format(s/12))