n = int(input())
for i in range(n,4,-1):
    if i % 2 != 0:
        p= 0
        for b in range(3,i):
            if i % b == 0:
                p +=1
                break
        if p == 0:
            a = i - 2
            p2 = 0
            for c in range(2,a):
                if a % c == 0:
                    p2 +=1
                    break
            if p2 == 0:
                print("{} {}".format(a, i))
                break