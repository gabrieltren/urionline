c = int(input())
tc = map(int, input().split(' '))

cc = 0

for i in tc:
    if i == c:
        cc+=1

print(cc)