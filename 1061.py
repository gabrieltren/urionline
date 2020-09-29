d, di = input().split(" ") 
hi,mi,si = input().split(" : ")
d2, df = input().split(" ")
hf,mf,sf = input().split(" : ")

di = int(di)
df = int(df)

hi = int(hi)
mi = int(mi)
si = int(si)

hf = int(hf)
mf = int(mf)
sf = int(sf)

dt = int(0)
ht = int(0)
mt = int(0)
st = int(0)

if df > di:
    dt = df - di
    if hf == hi:
        ht = 0
        if mf == mi:
            mt = 0
            if sf == si:
                st = 0
            elif sf > si:
                st = sf - si
            else:
                dt -= 1
                ht = 23
                mt = 59
                st = 60 + sf - si
        elif mf > mi:
            mt = mf - mi
            if sf == si:
                sf = 0
            elif sf > si:
                st = sf - si
            else:
                mt -= 1
                st = 60 + mf - mi
        else:
            if sf == si:
                dt -= 1
                ht = 23
                mt = 60 + mf - mi 
                st =0
            elif sf > si:
                dt -= 1
                ht = 23
                mt = 60 + mf - mi 
                st = sf - si
            else:
                dt -= 1
                ht = 23
                mt = 60 + mf - mi - 1
                st =60 + sf -si
    elif hf > hi:
        ht = hf - hi
        if mf == mi:
            mt = 0
            if sf == si:
                st = 0
            elif sf > si: 
                st = sf - si
            else:
                ht -= 1
                mt = 59
                st = 60  + sf - si
        elif mf > mi:
            mt = mf - mi
            if sf == si:
                st = 0
            elif sf > si:
                st = sf - si
            else:
                mt -= 1
                sf = 60 + mf -mi
        else:
            ht -= 1
            mt = 60 + mf - mi
            if sf == si:
                sf = 0 
            elif sf > si:
                st = sf - si
            else:
                mt -= 1
                st = 60 +sf -si
    else:
        dt -= 1
        ht = 24 + hf - hi
        if mf == mi:
            mt = 0
            if sf == si:
                st = 0
            elif sf > si:
                st = sf - si
            else:
                ht -= 1
                mt = 59
                st = 60  + sf - si
        elif mf > mi:
            mt = mf - mi
            if sf == si:
                st = 0
            elif sf > si:
                st = sf - si
            else:
                mt -= 1
                sf = 60 +mf -mi
        else:
            ht -= 1
            mt = 60 + mf - mi
            if sf == si:
                sf = 0 
            elif sf > si:
                st = sf - si
            else:
                mt -= 1
                st = 60 +sf -si
    
else:
    dt = 0
    if hf == hi:
        if mf == mi:
            if sf == si:
                ht = 0
                mt = 0
                st = 0
            elif sf > si:
                ht = 0
                mt = 0
                st = sf - si
            else:
                ht = 0
                mt =0
                st = 0
        elif mf > mi:
            if sf == si:
                ht = 0
                mt = mf - mi
                sf = 0
            elif sf > si:
                ht = 0 
                mt = mf - mi
                st = sf - si
            else:
                ht = 0
                mt = mf - mi - 1
                st = 60 + mf - mi
        else:
            if sf == si:
                ht = 0
                mt = 0
                st =0
            elif sf > si:
                ht= 0
                mt =0
                st =0
            else:
                ht = 0
                mt = 0
                st = 0
    elif hf >hi:
        if mf == mi:
            if sf == si:
                ht = hf - hi
                mt = 0
                st = 0
            elif sf > si:
                ht = hf - hi
                mt = 0 
                st = sf - si
            else:
                ht = hf - hi - 1
                mt = 59
                st = 60  + sf - si
        elif mf > mi:
            if sf == si:
                ht = hf - hi
                mt = mf - mi
                st = 0
            elif sf > si:
                ht = hf - hi
                mt = mf - mi
                st = sf - si
            else:
                ht = hf - hi
                mt = mf -mi -1
                sf = 60 +mf -mi
        else:
            if sf == si:
                ht = hf - hi - 1
                mt = 60 + mf - mi
                sf = 0 
            elif sf > si:
                ht = hf - hi - 1
                mt = 60 + mf - mi
                st = sf - si
            else:
                ht = hf - hi - 1
                mt = 60 + mf -mi -1
                st = 60 +sf -si
    else:
        ht = 0
        mt = 0
        st = 0


print("{} dia(s)" .format(dt))
print("{} hora(s)" .format(ht))
print("{} minuto(s)" .format(mt))
print("{} segundo(s)" .format(st))