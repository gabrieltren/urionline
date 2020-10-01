l = int (input())
c = input()

x = []
s = float(0)

for i in range(0,144):
    a = float(input())
    x.append(a)
for i in range(0,12):
    inde = int(l*12+i)
    s+= x[inde]

if c == 'S':
    print(s)
else:
    print(s/12)