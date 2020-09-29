x = int(input())
z = int(input())

while z <= x:
    z = int(input())

i = int(0)
t = int(0)
while t < z:
    t += x
    x += 1
    i += 1

print(i)