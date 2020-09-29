n = int(input())


if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a = 0
    b = 1
    c = 1
    print(a,b, end=" ")

    for i in range(3,n+1,1):
        c = a + b
        a = b
        b = c
        if i == n:
            print(c)
            continue
        print(c, end=" ") 
        
        
    
