def tdec(a):
    b = int(0)
    k = 31
    for i in range(0,32,1):
        if(a[k-i] == '1'):
            b = b + 2**(31-(k-i))
    return b
def tbit(a):
    r = ""
    c= int(32)
    while c>0:
        if(a>0):
            if(a % 2 == 0):
                q = "0"
            else:
                q = "1"
            a = a // 2
            r = q + r
        else:
            r = "0" + r
        c-=1
    return r

def xord(a, b):
    k = 31
    resp = ""
    for i in range(0,32,1):
        if((a[k - i] == '0' and b[k-i] == '1') or (a[k - i] == '1' and b[k-i] == '0')):
            resp = "1" + resp
            
        else:
            resp = "0" + resp               
    return resp

while True:
    try:
        ac , bc = map(int, input().split(" "))
        abt = tbit(ac)
        bbt = tbit(bc)
        resp = xord(abt,bbt)
        resp2 = tdec(resp)
        print(resp2)

    except EOFError:
        break