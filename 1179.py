impar = []
par = []
indimpar= 0
indpar = 0
for i in range(0,15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
        indpar += 1
    else:
        impar.append(x)
        indimpar += 1
    if indpar == 5 or indimpar == 5:
        if indpar == 5:
            for j in range(0,5):
                print("par[{}] = {}" .format(j, par[j]))
            indpar = 0
            par.clear()
        if indimpar == 5:
            for j in range(0,5):
                print("impar[{}] = {}" .format(j, impar[j]))
            indimpar = 0
            impar.clear()
for i in impar:
    print("impar[{}] = {}" .format(impar.index(i), i))
for i in par:
    print("par[{}] = {}" .format(par.index(i), i))
