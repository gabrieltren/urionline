while True:
    try:
        text = input()
        s1 = text.split('=')
        resut = s1[1]
        s2 = s1[0].split('+')
        v1 = s2[0]
        v2 = s2[1]
        if resut == 'J':
            print(int(v1)+int(v2))
        elif v1 == 'R':
            print(int(resut) - int(v2))
        elif v2 == 'L':
            print(int(resut) - int(v1))
    
    except EOFError:
        break

