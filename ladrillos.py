def operador():
    try:
        numeros = list(map(float, input(":").split()))
        return numeros
    except TypeError:
        print("porfavoooor, ingresa un numero")
    except ValueError:
        print("ponga un numeroooo!")

            
            
