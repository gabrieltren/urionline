a = int(0)
n = int(0)
t = int(0)
l = input()

lista = l.split(" ")
for i in range(0,len(lista),1):
    lista[i] = int(lista[i])
    if a == 0 or n == 0:
        if a== 0:
            a = lista[i]
            continue
        if a != 0 and n == 0 and lista[i]>0:
            n = lista[i]

for i in range(1, n+1, 1):
    t += a + i-1
    
print(t)