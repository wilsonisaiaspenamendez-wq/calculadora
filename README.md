# Calculadora Básica

## Lo que tiene y lo que no tiene:
1. 🫡Es una calculadora sencilla capaz de: sumar, restar, dividir, multiplicar y encontrar la raiz cuadrada de 1 o varios numeros.
2. 🤕No tiene interfaz gráfica(es mi primer proyecto).
3. 🤕No tiene historial permanente.

---

## Nota importantisima:
1. Es mi primer proyecto por lo cual solo me enfoque en hacer compatible la calculadora para el OS que uso yo el cual es: Debian/GNU linux.
2. Si les da dificultad de ejecutar la calculadora pues construyan una imagen en base a uno de los dockerfile que estan en el repo.

---

# Pasos para su instalación:

1. Para los que usan docker desktop vallan al enlace oficial de docker desktop: https://www.docker.com/products/docker-desktop/
2. Para los que usan apt o otro gestor de paquetes vallan al enlace oficial de docker y sigan la guia correspondiente de ellos: https://docs.docker.com/desktop/setup/install/linux/

---

## construir imagen docker:

1. para el debian.dockerfile
```bash
docker build -f debian.dockerfile -t calculadora:debian .
```
2. para el dockerfile:
```bash
docker build -f dockerfile -t calculadora:python .
```
---

## para ejecutar las imagenes:

1. calculadora:debian:
```bash
docker run -it calculadora:debian
```
2. calculadora python:
```bash
docker run -it calculadora:python
```
3. Si como a mi ustedes les da pereza escribir sudo docker 24/7 pues ejecuten esto:
```bash
sudo usermod -aG docker $USER
```

---

# Nota para el yo del futuro:

1. Docker odia las comas.
2. No hay que olvidar las "" individuales en el CMD del dockerfile.
3. Piensa antes de poner codigooo por favooor! 🫤🫤🫤🫤
4. No uses self para todo 😵‍💫😵‍💫😵‍💫😵‍💫.

---

# Objetivo a añadir en las proximas versiones:
2. Se le añadirán más operaciones a la calculadora.
4. La calculadora tendrá la capacidad de soportar más de 2 digitos.
5. Sera mas compatible con mas plataformas(windows, linux).
6. Quitar el bucle for remplazando el codigo por numpy.

---

## Objetivos cumplidos en estas versiones:
1. V 0,1: Codigo subido a github.
2. V 0.2: Soporte para mas de 2 digitos con el bucle for.
3. V 0.3: Compatibilidad con Debian linux.
4. V 0.4: Remplazo del bucle for por numpy para optimizacion y soporte de mas digitos sin errores.
5. V 0.5: Ejecucion de la calculadora en terminal sin estar anclado al directorio del proyecto.
6. V 0.6: remplazo del endoesqueleto(codigo) por POO
7. V 0.7: Se purgo todos los self innecesarios que no son importantes, se dise;o mejor el control de errores por si se selecciona una opcion no correcta y se quito la contrasena para que la calculadora sea mas accesible y facil de acceder.

---

# Aclaracion importante!:

1. Docker es una herramienta externa y creada por otras personas. Aqui solo se proporcionan configuraciones para que el proyecto se ejecute sin ninguna dificultad en cualquier equipo.

---

