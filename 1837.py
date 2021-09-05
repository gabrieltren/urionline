a,b = map(int, input().split(' '))

q = int(a/b)
r = a % b
if a >=0:
    q = int(a / b)
    if r>= 0:
        r = int(a % b)
    else:
        b = b*(-1)
        r = int(a % b)


else:
    c1 = 0
    c2 = 0
    c1 = b *(-1) if b < 0 else b

    r = 0
    while r<c1:
        c2 = a - r
        if c2 % b == 0:
            break
        r+=1

    
    q = int(c2 / b)



print(q,r)
