n = int(input())
tper= 0
for i in range(n):
    t,v = map(int, input().split(' '))
    tper += t*v

print(tper)