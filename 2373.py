n = int(input())
copq = 0
for i in range(n):
    l, c = map(int, input().split(' '))
    copq += c if c < l else 0

print(copq)