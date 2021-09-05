"""
pisca varias vezes:
 piscada em  binario
 - = 0
 * = 1


grita 3 vezes:
3º para o programa
"""

def valor(p,v,i):
    if i == 0:
        if p == '*':
            return 2**v[i]
        else:
            return 0
    else:
        if p[i] == '*':
            return 2**v[i] + valor(p[:i],v,(i-1))
        else:
            return valor(p[:i],v,(i-1))

k = [2,1,0]

gritos= 0
total = 0
while gritos <3:
    pis = input()
    if pis == 'caw caw':
        print(total)
        gritos+=1
        total = 0
    else:
        total+= valor(pis,k,((len(pis)-1)))