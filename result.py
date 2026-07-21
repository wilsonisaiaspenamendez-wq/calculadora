import numpy as np
class Calculador():
    def suma(self, elemento):
        self.result = np.sum(elemento)
        print(self.result)
    def multiplicacion(self, elemento1):
        self.result1 = np.multiply.reduce(elemento1)
        print(self.result1)
    def resta(self, elemento2):
        self.result2 = np.subtract.reduce(elemento2)
        print(self.result2)
    def division(self, elemento3):
        self.di = np.divide.reduce(elemento3)
        print(self.di)
    def raiz_cuadrada(self, elemento4):
        self.result4 = np.sqrt(elemento4)
        print(self.result4)
