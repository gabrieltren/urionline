tentantivas = int(input())

ganhos = 0
for i in range(tentantivas):
    porta = int(input())
    if porta != 1:
        ganhos +=1

print(ganhos)