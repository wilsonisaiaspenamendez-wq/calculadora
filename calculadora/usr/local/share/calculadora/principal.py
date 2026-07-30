from ladrillos import Datos
from result import Calculador
class Motor():
    def __init__(self):
        self.calculadores = Calculador()
        self.portero = Datos()
    def decicion(self):
            while True:
                obtener = input("va a: sumar(S), restar(R), multiplicar(M), dividir(D), raiz cuadrada(P)").upper()
                opciones = {
                    "S": self.calculadores.suma,
                    "R": self.calculadores.resta,
                    "M": self.calculadores.multiplicacion,
                    "D": self.calculadores.division,
                    "P": self.calculadores.raiz_cuadrada
                }
                if obtener in opciones:
                    obtenido = self.portero.operador()
                    resultado = opciones[obtener](obtenido)
                    print(resultado)
                else:
                    print("letra o opcion incorrectaaaaaaa")
                    continue
                while True:
                    decision2 = input("de nuevo? S o N").upper()
                    if decision2 == "S":
                        break
                    elif decision2 == "N":
                        return
                    else:
                        print("opcion no correcta!!!!!")
                        continue
