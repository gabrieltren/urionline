n = int(input())

for i in range(1,n+1,1):
    for j in range(1,4,1):
        if j < 3: 
            print(i**j, end=" ")
        else:
            print(i**j)
    for k in range(1,4,1):
        if k == 1:
            print(i**k, end=" ")
        elif k < 3: 
            print((i**k + 1), end=" ")
        else:
            print(i**k +1)