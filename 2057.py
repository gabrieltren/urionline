h,v,f = map(int, input().split())

t = h+v+f
if t >= 24 :
    t -= 24
    print(t)
elif t < 0:
    t += 24
    print(t)
else:
    print(t)