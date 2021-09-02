n = int(input())
tn = map(int, input().split(' '))
m2 =0
m3 =0
m4 =0
m5 =0
for i in tn:
    if i % 2 ==0:
        m2 +=1
    if i % 3 ==0:
        m3 +=1
    if i % 4 ==0:
        m4 +=1
    if i % 5 ==0:
        m5 +=1

print("{} Multiplo(s) de 2".format(m2))
print("{} Multiplo(s) de 3".format(m3))
print("{} Multiplo(s) de 4".format(m4))
print("{} Multiplo(s) de 5".format(m5))