
def mort(qtsold,pulos):
    ret = 0
    for i in range(2,(qtsold+1)):
        ret= (ret + pulos) % i

    return ret


nc = int(input())
for i in range(1,nc+1):
    n,k = map(int, input().split(' '))
    x = mort( n, k) +1
    print("Case {}: {}".format(i, x) )