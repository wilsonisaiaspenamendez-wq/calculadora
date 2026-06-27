from ladrillos import operador
from result import sumar, restar, multiplicar, dividir
from contrasena import contrasena
import sys
contrasena()
while True:
	decision = input("va a sumar(S), restar(R), multiplicar(M), dividir(D):").upper()
	n1, n2 = operador()
	if decision == "S":
		sumar(n1, n2)
	elif decision == "R":
		restar(n1, n2)
	elif decision == "M":
		multiplicar(n1, n2)
	elif decision == "D":
		dividir(n1, n2)
	else:
		print("troleadoooooo, letra equivocada")
	intento = input("de nuevo? S o N").upper()
	if intento == "N":
		print("ok")
		sys.exit()

