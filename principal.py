# hecho en un p*** mes por un randon(yo)
# pesos gastados en IA: 0
# IA utilizada como copia y pega: 0%
# IA local como asistente para lo aburrido y repetitivo: 60% 
# qwen 2.5 coder:1.5b es la claveeeee!!!!!!!!!!!!!!!!!🤖🤖🤖
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
            opciones = {
                "S": self.suma.suma,
                "R": self.suma.resta,
                "M": self.suma.multiplicacion,
                "D": self.suma.division,
                "P": self.suma.raiz_cuadrada
            }
            if obtener in opciones:
                obtenido = self.dato.operador()
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