hi,mi,hf,mf =input().split(" ") 
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
ht = int(0)
mt = int (0)

if hf > hi:
    if mf > mi:
        ht = hf - hi
        mt = mf - mi
    elif mf == mi:
        ht = hf - hi
    else:
        ht = hf - hi - 1
        mt = 60 + mf - mi
elif hi == hf:
    if mf > mi:
        mt = mf - mi
    elif mf == mi:
        ht = 24
    else:
        ht = 23
        mt = 60 + mf - mi
else:
    if mf > mi:
        ht = 24 + hf - hi
        mt = mf - mi
    elif mf == mi:
        ht = 24 + hf - hi
    else:
        ht = 24 + hf - hi -1
        mt = 60 + mf - mi
            
print("O JOGO DUROU",ht,"HORA(S) E",mt,"MINUTO(S)")
