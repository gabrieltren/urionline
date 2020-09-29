x = int(input())

while x != 0:
    c = int(1)
    s = int(0)
    while c <=5:
        if x % 2 == 0:
            s+= x
            c+=1
        x+=1
    
    print(s)
    x = int(input())