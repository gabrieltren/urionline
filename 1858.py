n = int(input())

b = list(map(int, input().split(' ')))


menor = 0
m_n = 0
for i in range(len(b)):
    if i == 0:
        menor = 1
        m_n = b[i]
    else:
        if m_n > b[i]:
            menor = i+1
            m_n = b[i]

print(menor)
            
            