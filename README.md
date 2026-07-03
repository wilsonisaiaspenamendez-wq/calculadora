# Calculadora Básica

##Lo que tiene y lo que no tiene:
1. Es una calculadora sencilla capaz de: sumar, restar, dividir, multiplicar.
2. No tiene interfaz gráfica.
3. No tiene historial permanente.

---

## Pasos para su instalación:

1. La calculadora solo es compatible con Docker por el momento, por lo que hay que instalarlo. Para ir a su enlace oficial: https://www.docker.com/products/docker-desktop/

2. Una vez instalado Docker y descargado el `Dockerfile`, hay que construir la imagen:
```bash
sudo docker build -t calculadora:0.1 .
