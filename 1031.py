'''def tr(n,k):
    if salto(n, k)+2 != 13:
        return tr(n,(k+1))
    else:
        return k
'''
def salto(n,k):
    sat = 0

    for i in range(1,n):
        sat = ( sat + k ) % i
    
    return sat


def ret(n,k):
    if (salto(n, k)+2) == 13:
        return k
    else:
        k+=1
        return ret(n,k)

'''
def salto(n,k,i,sat):
    if i < n:
        return salto(n,k,(i+1),((sat+k)% i))
    else:
        return sat

'''

while True:
    try:
        n = int(input())
        k = 1
        
        re = ret(n,k)

        print(re)
    except EOFError:
        break
