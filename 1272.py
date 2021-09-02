testes = int(input())

for i in range(testes):
    texto = input()
    palavras = texto.split(' ')
    retorno = ''
    for p in palavras:
        if p != '':
            retorno += p[0]
    print(retorno)
