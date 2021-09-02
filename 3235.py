n,l = map(int, input().split(' '))

malas = input().split(' ')
v1 = float(0)
v2 = float(0)
vs = float(0)
if len(malas) == 1:
    print("0.1")
else:
    for i in range(1,len(malas),1):
        if i == 1:
            v1 = float(malas[i-1])
            v2 = float(malas[i])
            vs = v2-v1
        else:
            v1 = v2
            v2 = float(malas[i])
            vc = v2-v1
            if vc < vs:
                vs = vc

    print(vs)
