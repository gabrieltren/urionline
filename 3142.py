def sp1(a):
    if(a=='A'):
        return 1
    if(a=='B'):
        return 2
    if(a=='C'):
        return 3
    if(a=='D'):
        return 4
    if(a=='E'):
        return 5
    if(a=='F'):
        return 6
    if(a=='G'):
        return 7
    if(a=='H'):
        return 8
    if(a=='I'):
        return 9
    if(a=='J'):
        return 10
    if(a=='K'):
        return 11
    if(a=='L'):
        return 12
    if(a=='M'):
        return 13
    if(a=='N'):
        return 14
    if(a=='O'):
        return 15
    if(a=='P'):
        return 16
    if(a=='Q'):
        return 17
    if(a=='R'):
        return 18
    if(a=='S'):
        return 19
    if(a=='T'):
        return 20
    if(a=='U'):
        return 21
    if(a=='V'):
        return 22
    if(a=='W'):
        return 23
    if(a=='X'):
        return 24
    if(a=='Y'):
        return 25
    if(a=='Z'):
        return 26  

def sp2(a):
    return (sp1(a[0]) * 26) + sp1(a[1])

def sp3(a):
    return (sp1(a[0])* 676) + (sp1(a[1]) * 26) + sp1(a[2])


c = int(0)
while True:
    try:
        a = str(input())
        if(len(a) == 1):
            c = sp1(a)
        elif(len(a) == 2):
            c = sp2(a)
        elif(len(a)== 3):
            c = sp3(a)
        else:
            c = 17000

        if(c <= 16384):
            print(c)
        else:
            print("Essa coluna nao existe Tobias!")
    except EOFError:
        break