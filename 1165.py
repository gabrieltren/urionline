n = int(input())

for i in range(0,n):
    x = int(input())
    a = 0
    for j in range(1,x):
        if x % j == 0:
            a +=1
        if a > 1:
            break
    if a == 1:
        print(x,"eh primo")
    else:
        print(x,"nao eh primo")