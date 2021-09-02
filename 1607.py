
def valor_letra(letra):
    if letra =='a':
        return 1
    elif letra == 'b':
        return 2
    elif letra == 'c':
        return 3
    elif letra == 'd':
        return 4
    elif letra == 'e':
        return 5
    elif letra == 'f':
        return 6
    elif letra == 'g':
        return 7
    elif letra == 'h':
        return 8
    elif letra == 'i':
        return 9
    elif letra == 'j':
        return 10
    elif letra == 'k':
        return 11
    elif letra == 'l':
        return 12
    elif letra == 'm':
        return 13
    elif letra == 'n':
        return 14
    elif letra == 'o':
        return 15
    elif letra == 'p':
        return 16
    elif letra == 'q':
        return 17
    elif letra == 'r':
        return 18
    elif letra == 's':
        return 19
    elif letra == 't':
        return 20
    elif letra == 'u':
        return 21
    elif letra == 'v':
        return 22
    elif letra == 'w':
        return 23
    elif letra == 'x':
        return 24
    elif letra == 'y':
        return 25
    elif letra == 'z':
        return 26
    else:
        return 0

testes = int(input())

for i in range(testes):
    texto = input().split(' ')
    t1 = texto[0]
    t2 = texto[1]
    operacoes = 0
    for l in range(len(t1)):
        if t1[l] != t2[l]:
            v1 = valor_letra(t1[l])
            v2 = valor_letra(t2[l])
            if v1 < v2:
                operacoes += (v2-v1)
            else:
                operacoes += (26 + v2 - v1)
    print(operacoes)
