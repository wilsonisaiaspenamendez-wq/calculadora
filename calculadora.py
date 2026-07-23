#!/usr/bin/env python3
# esta parte es la encargada de invocar la calculadora
import sys
# sys.path.append() es el encargado de decirle a python en donde encontrar los modulos importados en este codigo(las clases y funciones)🤔🤔🤔
sys.path.append("/usr/local/bin")
from principal import Motor
from ladrillos import Datos
from result import Calculador
invocador = Motor()
invocador.decicion()
