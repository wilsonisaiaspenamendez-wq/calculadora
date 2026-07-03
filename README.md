#Calculadora Basica
##Lo que tiene y lo que no tiene:
1-Es una calculadora sencilla capaz de: sumar, restar, dividir, multiplicar.
2-No tiene interfaz grafica.
3-No tiene historial permanente.

##Pasos para su instalacion:
1-La calculadora solo es compatible con docker por el momento por lo que hay que instalar docker
Para instalar docker hay que ir a su enlace oficialL: https://www.docker.com/products/docker-desktop/
2-Una vez instalado docker y descargado el dockerfile hay que construir la imagen:
Sudo docker build -t calculadora:0.1 .
3-Despues ejecutamos la imagen creada:
sudo docker run -it calculadora:0.1
###Dato importante para el yo de futuro.
1-Docker odia las comas
2-Hay que acordarse siempre de poner comillas individuales XD.
#Proximo a a;adir:
1-Se le a;adira interfaz grafica
2-se le a;adiran mas operaciones a la calculadora
3-La calculadora tendra historial de operaciones
4-La calculadora tendra la capacidad de soportar mas de 2 elementos.
Estos cambios se implementaran poco a poco para que no se encuentren errores.
