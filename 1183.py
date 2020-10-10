'''
l = [0]*12
for i in range(0,12):
    l[i] = [0]*12
ab = float(0.0)
t = input()
total = float(0.0)
for i in range(0,12):
    for j in range(0,12):
        ab = float(input())
        if i < j:
            total += ab

if t =="M":
    print("%1f" %(total/66))
elif t =="S":
    print("%1f"%total)
    '''
     
t = input()
l = []

for i in range(12):
    for j in range(12):
        ab = float(input())
        if i < j:
            l.append(ab)

if t == "S":
    print(("%.1f")%(sum(l)))
else:
    print(("%.1f")%(sum(l)/len(l)))



'''
t = input()
l = []
for i in range(0,12):
    for j in range(0,12):
        ab = float(input())
        if i < j:
            l.append(ab)

if t =="M":
    print("%1f" %(sum(l)/66))
elif t =='S':
    print("%1f"%(sum(l)))



soma_ou_media = input()
matriz = []

for i in range(12):
    for j in range(12):
        valor = float(input())
        if i < j:
            matriz.append(valor)

if soma_ou_media == "S":
    print(("%.1f")%(sum(matriz)))
else:
    print(("%.1f")%(sum(matriz)/len(matriz)))
    

s = float(0)

for i in range(0,11):
    for j in range(0,12):
        if j<i:
            s+= l[j][i]

if t == 'S':
    print("{:.1f}" .format(s))
else:
    ac = s/66.0
    print("{:.1f}" . format(ac))
'''