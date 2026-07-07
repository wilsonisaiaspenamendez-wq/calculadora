import numpy as np
def sumar(Suma):
    s = np.array(Suma)
    resultS = np.sum(s)
    print(resultS)      
def restar(resta):
    r = np.array(resta)
    resultR = np.subtract.reduce(r)
    print(resultR)
def multiplicar(multiplicacion):
    m = np.array(multiplicacion)
    resultM = np.multiply.reduce(m)
    print(resultM)
def dividir(D):
    d = np.array(D)
    Result = np.divide.reduce(d)
    print(Result)
  
