i = int (input())
idades = int(0)
c= int(0)
while i >=0:
    idades +=i
    c+=1
    i = int(input())

if(c == 0):
    print(0)
else:
    print("{:.2f}".format((idades/c)))
    
