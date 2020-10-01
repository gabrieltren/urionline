t = int(input())
for i in range(0,t):
    x= int(input())
    
    if x == 0:
        print("Fib(0) = 0")
    elif x == 1:
        print ("Fib(1) = 1")
    else:
        a = 0
        b = 1
        for j in range(2,x+1):
            c = a + b
            a = b
            b = c
        print("Fib({}) = {}" .format(x , c))
        