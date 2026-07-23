# hecho en un p*** mes por un randon(yo)
# pesos gastados en IA: 0
# IA utilizada como copia y pega: 0%
# IA local como asistente para lo aburrido y repetitivo: 60% 
# usando docker: 100%
from ladrillos import Datos
from result import Calculador
# clase Motor: es la encargada de ocultar la logica de invocacion hacia las funciones.
class Motor():
    def __init__(self):
        self.suma = Calculador()
        self.dato = Datos()
    def decicion(self):
        while True:
            obtener = input("va a: sumar(S), restar(R), multiplicar(M), dividir(D), raiz cuadrada(P)").upper()
            if obtener == "S":
                obtenido = self.dato.operador()
                resultado = self.suma.suma(obtenido)
                print(resultado)
            elif obtener == "R":
                obtenido = self.dato.operador()
                resultado1 = self.suma.resta(obtenido)
                print(resultado1)
            elif obtener == "M":
                obtenido = self.dato.operador()
                resultado2 = self.suma.multiplicacion(obtenido)
                print(resultado2)
            elif obtener == "D":
                obtenido = self.dato.operador()
                resultado3 = self.suma.division(obtenido)
                print(resultado3)
            elif obtener == "P":
                obtenido = self.dato.operador()
                resultado4 = self.suma.raiz_cuadrada(obtenido)
                print(resultado4)
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




    
