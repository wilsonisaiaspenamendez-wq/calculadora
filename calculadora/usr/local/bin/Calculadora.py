#!/usr/bin/env python3
from ladrillos import operador
from result import sumar, restar, multiplicar, dividir
from contrasena import contrasena
import sys
sys.path.append("/usr/share/archivos_calculadora")
contrasena()
while True:
	decision = input("va a sumar(S), restar(R), multiplicar(M), dividir(D):").upper()
	datos = operador()
	if decision == "S":
		sumar(datos)
	elif decision == "R":
		restar(datos)
	elif decision == "M":
		multiplicar(datos)
	elif decision == "D":
		dividir(datos)
	else:
		print("troleadoooooo, letra equivocada")
	intento = input("de nuevo? S o N:").upper()
	if intento == "N":
		print("ok")
		sys.exit()
