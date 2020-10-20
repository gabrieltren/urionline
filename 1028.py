''' 
seguindo a seguinte regra: 
cada um contava quantas figurinhas tinha.
Em seguida, eles tinham que dividir as figurinhas de cada um em pilhas do mesmo tamanho, 
no maior tamanho que fosse possível para ambos.
Então, cada um escolhia uma das pilhas de figurinhas do amigo para receber. 

Por exemplo, 
se Ricardo e Vicente fossem trocar as figurinhas e tivessem respectivamente 8 e 12 figuras, 
ambos dividiam todas as suas figuras em pilhas de 4 figuras (Ricardo teria 2 pilhas e Vicente teria 3 pilhas) 
e ambos escolhiam uma pilha do amigo para receber.

'''
def mdc(a,b):
    if a % b == 0: 
        return b
    else:
        return mdc(b, a%b)

n = int(input())
ac = int(0)
while n > 0:
    k1, k2 = input().split(" ")
    k1 = int(k1)
    k2 = int(k2)
    ac = mdc(k1, k2)
    print(ac)
    n-=1