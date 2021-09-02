a,b,c = map(int, input().split(' '))

if a > b:
    if b <=c:
        print(':)')
    elif b > c and (b-c) < (a-b):
        print(':)')
    elif b > c and (b-c) >= (a-b):
        print(':(')
elif a < b:
    if b>= c:
        print(':(')
    elif b < c and (c-b) <(b-a):
        print(':(')
    elif b< c and (c -b) >= (b-a):
        print(':)')
    
elif a == b:
    if b < c :
        print(':)')
    else:
        print(':(')
