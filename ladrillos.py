# clase encargada de diregir los datos para que la clase Calculadora trabaje con ellos facilmente.
class Datos():
    def operador(self):
        while True:
            try:
                self.datos = list(map(float, input(":").split()))
                return self.datos
            except ValueError:
                print("Pon numeros!")
                continue