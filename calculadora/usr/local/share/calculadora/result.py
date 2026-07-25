import numpy as np
class Calculador():
    def suma(self, elemento):
        result = np.sum(elemento)
        return result
    def multiplicacion(self, elemento1):
        result1 = np.multiply.reduce(elemento1)
        return result1
    def resta(self, elemento2):
        result2 = np.subtract.reduce(elemento2)
        return result2
    def division(self, elemento3):
        di = np.divide.reduce(elemento3)
        return di
    def raiz_cuadrada(self, elemento4):
        result4 = np.sqrt(elemento4)
        return result4
    def division(self, numeros):
        di = np.divide.reduce(numeros)
        return di
    def raiz_cuadrada(self, numero):
        result4 = np.sqrt(numero)
        return result4
