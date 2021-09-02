a = int(input())
n = int(input())

e = 0
for i in range(n):
    f = int(input())
    if f*a >= 40000000:
        e +=1

print(e)