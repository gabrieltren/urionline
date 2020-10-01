n = int(input())
ent = input().split(" ")

for i in range(0,n):
    ent[i] = int(ent[i])

menor = ent[0]
posi = 0

for i in range(1,n):
    if ent[i] < menor:
        menor = ent[i]
        posi = i

print("Menor valor:",menor)
print("Posicao:", posi)