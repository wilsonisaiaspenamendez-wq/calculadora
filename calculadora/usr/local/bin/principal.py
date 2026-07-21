
from ladrillos import Datos
from result import Calculador
class Motor():
    def __init__(self):
        self.suma = Calculador()
        self.dato = Datos()
    def decicion(self):
        while True:
            self.obtener = input("va a: sumar(S), restar(R), multiplicar(M), dividir(D), raiz cuadrada(P)").upper()
            if self.obtener == "S":
                self.obtenido = self.dato.operador()
                self.suma.suma(self.obtenido)
            elif self.obtener == "R":
                self.obtenido = self.dato.operador()
                self.suma.resta(self.obtenido)
            elif self.obtener == "M":
                self.obtenido = self.dato.operador()
                self.suma.multiplicacion(self.obtenido)
            elif self.obtener == "D":
                self.obtenido = self.dato.operador()
                self.suma.division(self.obtenido)
            elif self.obtener == "P":
                self.obtenido = self.dato.operador()
                self.suma.raiz_cuadrada(self.obtenido)
            else:
                print("letra o opcion incorrectaaaaaaa")
                continue
            while True:
                self.decicion2 = input("de nuevo? S o N").upper()
                if self.decicion2 == "S":
                    break
                elif self.decicion2 == "N":
                    return
                else:
                    print("opcion no correcta!!!!!")
                    continue
                




    