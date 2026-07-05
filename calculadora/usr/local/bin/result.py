def sumar(Suma):
    suma1 = 0
    for numero in Suma:
        suma1 += float(numero)
    print(suma1)      
def restar(resta):
    resta1 = float(resta[0])
    for numero in resta[1:]:
        resta1 -= float(numero)
    print(resta1)
def multiplicar(multiplicacion):
    multiplicar1 = 1
    for numero in multiplicacion:
        multiplicar1 *= float(numero)
    print(multiplicar1)
def dividir(D):
    d = float(D[0])
    for numero in D[1:]:
        d /= float(numero)
    print(d)