def operador():
    while True:
        try:
            Datos = list(map(float, input(":").split()))
            return Datos
        except ValueError:
            print("Pon numeros!")