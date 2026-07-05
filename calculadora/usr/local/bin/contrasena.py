import sys
def contrasena():
    for i in range(3):
        datos = input("ponga contrasena:")
        if datos == "2711":
            print("correcto")
            return
        print("contrasena incorrecta. Quedan menos intentos")
    sys.exit()
