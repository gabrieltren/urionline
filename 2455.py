p1,c1,p2,c2 = map(int,input().split())

e = p1*c1
d = p2*c2

if e == d:
    print(0)
else:
    if e > d:
        print(-1)
    else:
        print(1)