n = int(input())
'''
for i in range(0,n):
    if i< n-1:
        print("HO ", end="")
    else:
        print("HO!")
'''
an = (n-1)*"Ho " + "Ho!"

print(an)