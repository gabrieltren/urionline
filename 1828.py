
casos = int(input())

trap = "Raj trapaceou!"
denovo = "De novo!"
bazinga = "Bazinga!"

for c in range(1,casos+1):

    a, b = input().split(' ')

    if a == "pedra": 
        if b == "pedra":    
            print(f"Caso #{c}: {denovo}")
        elif b == "papel":
            print(f"Caso #{c}: {trap}")
        elif b == "tesoura":
            print(f"Caso #{c}: {bazinga}")
        elif b == "lagarto":
            print(f"Caso #{c}: {bazinga}")
        elif b == "Spock":
            print(f"Caso #{c}: {trap}")

    elif a == "papel":
        if b == "pedra":    
            print(f"Caso #{c}: {bazinga}")
        if b == "papel":
            print(f"Caso #{c}: {denovo}")
        elif b == "tesoura":
            print(f"Caso #{c}: {trap}")
        elif b == "lagarto":
            print(f"Caso #{c}: {trap}")
        elif b == "Spock":
            print(f"Caso #{c}: {bazinga}")
   
    elif a == "tesoura":
        if b == "pedra":    
            print(f"Caso #{c}: {trap}")
        elif b == "papel":
            print(f"Caso #{c}: {bazinga}")
        elif b == "tesoura":
            print(f"Caso #{c}: {denovo}")

        elif b == "lagarto":
            print(f"Caso #{c}: {bazinga}")
        elif b == "Spock":
            print(f"Caso #{c}: {trap}")
    
    elif a == "lagarto":
        if b == "pedra":    
            print(f"Caso #{c}: {trap}")
        elif b == "papel":
            print(f"Caso #{c}: {bazinga}")
        elif b == "tesoura":
            print(f"Caso #{c}: {trap}")
        elif b == "lagarto":
            print(f"Caso #{c}: {denovo}")
        elif b == "Spock":
            print(f"Caso #{c}: {bazinga}")
    
    elif a == "Spock":
        if b == "pedra":    
            print(f"Caso #{c}: {bazinga}")
        elif b == "papel":
            print(f"Caso #{c}: {trap}")
        elif b == "tesoura":
            print(f"Caso #{c}: {bazinga}")
        elif b == "lagarto":
            print(f"Caso #{c}: {trap}")
        elif b == "Spock":
            print(f"Caso #{c}: {denovo}")
