def posicaoN(letra):
    if letra == 'A':
        return 0
    elif letra == 'B':
        return 1
    elif letra == 'C':
        return 2
    elif letra == 'D':
        return 3
    elif letra == 'E':
        return 4
    elif letra == 'F':
        return 5
    elif letra == 'G':
        return 6
    elif letra == 'H':
        return 7
    elif letra == 'I':
        return 8
    elif letra == 'J':
        return 9
    elif letra == 'K':
        return 10
    elif letra == 'L':
        return 11
    elif letra == 'M':
        return 12
    elif letra == 'N':
        return 13
    elif letra == 'O':
        return 14
    elif letra == 'P':
        return 15
    elif letra == 'Q':
        return 16
    elif letra == 'R':
        return 17
    elif letra == 'S':
        return 18
    elif letra == 'T':
        return 19
    elif letra == 'U':
        return 20
    elif letra == 'V':
        return 21
    elif letra == 'W':
        return 22
    elif letra == 'X':
        return 23
    elif letra == 'Y':
        return 24
    elif letra == 'Z':
        return 25

    return 0
       
def valorTotal(hash, elem):
    valor = 0
    for i in range(len(hash)):
        valor += posicaoN(hash[i]) + elem + i
    
    return valor

def vrec(hash, elem, e):
    if hash == []:
        return 0
    else:
        return posicaoN(hash.pop(0)) + elem + e + vrec(hash,elem,(e+1))

n = int(input())

total = 0

for i in range(n):
    a = int(input())
    for k in range(a):
        hash = input()
        total += vrec(list(hash), k, 0)
    print(total)
    total = 0
