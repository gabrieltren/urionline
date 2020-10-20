def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factor(n-1)

while True:
    try:
        a, b = map(int, input().split(" "))
        fac = factor(a) + factor(b)
        print(fac)

    except EOFError:
        break
