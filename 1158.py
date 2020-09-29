n =int(input())

for i in range(1,n+1,1):
    a,b = input().split(" ")
    a= int(a)
    b= int(b)
    c = int(1)
    s= int(0)
    while c <= b:
        if a% 2 == 1:
            s+=a
            c+=1
        a+=1

    print(s)