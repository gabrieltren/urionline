while True:
    try:
        n = int(input())
        for i in range(n):
            a = ''
            for k in range(n):
                if k == i:
                    if k != (n-1-i):
                        a += '1'
                    else:
                        a += '2'
                elif k == (n-1-i):
                    a += '2'
                else:
                    a +='3'
            print(a)

    except EOFError:
        break