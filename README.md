# Calculadora Básica

## Lo que tiene y lo que no tiene:
1. Es una calculadora sencilla capaz de: sumar, restar, dividir, multiplicar.
2. No tiene interfaz gráfica.
3. No tiene historial permanente.

---

## Pasos para su instalación:

1. La calculadora solo es compatible con Docker por el momento, por lo que hay que instalarlo. Para ir a su enlace oficial: https://www.docker.com/products/docker-desktop/

2. Una vez instalado Docker y descargado el `Dockerfile`, hay que construir la imagen:
```bash
sudo docker build -t calculadora:0.1 .
```
3. Despues de eso hay que ejecutar la imagen:
```bash
sudo docker run -it calculadora:0.1
```
# Nota para el yo del futuro:

1. Docker odia las comas.
2. No hay que olvidar las "" individuales en el CMD del dockerfile.
3. Piensa antes de poner codigooo por favooor!
4. Si te da pereza escribir sudo cada vez que quieras usar docker pues XD a;ade tu usuario al grupo docker:
```bash
sudo usermod -aG docker wilson(o el usuario que tengas)
   ```
Y no hace falta crear el grupo docker porque ya esta creado.

---

# Objetivo a añadir en las proximas versiones:
1. Se le añadirá interfaz gráfica.
2. Se le añadirán más operaciones a la calculadora.
3. La calculadora tendrá historial de operaciones.
4. La calculadora tendrá la capacidad de soportar más de 2 digitos.
5. Sera mas compatible con mas plataformas(windows, linux).
6. Quitar el bucle for remplazando el codigo por numpy.

---

## Objetivos cumplidos en estas versiones:
1. V 0,1: Codigo subido a github.
2. V 0.2: Soporte para mas de 2 digitos con el bucle for.
3. V 0.3: Compatibilidad con Debian linux.
4. V 0.4: Remplazo del bucle for por numpy para optimizacion y soporte de mas digitos sin errores. 


