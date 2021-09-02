def rec(b1, b2 ,maior, menor, i):
    if maior == menor:
        if i < maior-1:
            if b1[i] == b2[i]:
                return rec(b1, b2 ,maior, menor, (i+1)) + '0'
            else:
                return rec(b1, b2 ,maior, menor, (i+1)) + '1'
        else:
            if b1[i] == b2[i]:
                return '0'
            else:
                return '1'
    else:
        if i < menor:
            if b1[i] == b2[i]:
                return rec(b1, b2 ,maior, menor, (i+1)) + '0'
            else:
                return rec(b1, b2 ,maior, menor, (i+1)) + '1'
        else:
            if i < maior -1:
                return rec(b1, b2 ,maior, menor, (i+1)) + b1[i]
            else:
                return b1[i]

while True:
    try:
        n1, n2 = map(int, input().split(' '))
        b1 = str(format(n1, "b"))
        b2 = str(format(n2, "b"))
        b_i1 = b1[::-1]
        b_i2 = b2[::-1]
        v_b = ''
        if len(b_i1) >= len(b_i2):
            maior = len(b_i1)
            menor = len(b_i2)
            m_b = b_i1
            v_b = rec(b_i1, b_i2 ,maior, menor, 0)
        else:
            maior = len(b_i2)
            menor = len(b_i1)
            m_b = b_i2
            v_b = rec(b_i2, b_i1 ,maior, menor, 0)

        print(int(v_b, 2))

    except EOFError:
        break        
