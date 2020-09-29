d = int(input())
alcool = 0
gasolina = 0
disel = 0
while d != 4:
    if d == 1:
        alcool +=1
    elif d == 2:
        gasolina +=1
    elif d == 3:
        disel +=1
    d = int(input())
    
print("MUITO OBRIGADO")
print("Alcool: {}" .format(alcool))
print("Gasolina: {}" .format(gasolina))
print("Diesel: {}" .format(disel))
        
    