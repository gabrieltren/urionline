x = int(input())
y = int(input())
if x < y:
    maior = y
    menor = x
else:
    maior = x
    menor = y

somatorio = 0

for i in range(menor,(maior+1),1):
    if i % 13 != 0: 
        somatorio += i

print(somatorio)