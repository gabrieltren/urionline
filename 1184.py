t = input()
l = []

for i in range(12):
    for j in range(12):
        ab = float(input())
        if i > j:
            l.append(ab)

if t == "S":
    print(("%.1f")%(sum(l)))
else:
    print(("%.1f")%(sum(l)/len(l)))
