# Calculadora Básica

## Lo que tiene y lo que no tiene:
1. Es una calculadora sencilla capaz de: sumar, restar, dividir, multiplicar.
2. No tiene interfaz gráfica.
3. No tiene historial permanente.

---

# Pasos para su instalación:

## Para los que usan docker desktop en windows:
1. Para instalarlo hay que ir al enlace oficial y descargar la version del sistema operativo correspondiente: https://www.docker.com/products/docker-desktop/

2. Una vez instalado Docker y descargado el `Dockerfile`, hay que construir la imagen:
```bash
sudo docker build -t calculadora:0.1 .
```
3. Despues de eso hay que ejecutar la imagen:
```bash
sudo docker run -it calculadora:0.1
```

---

## Para los que usan docker desktop en Debian:

1. Si quieren descargar la version desktop pues van a este enlace: https://docs.docker.com/desktop/setup/install/linux/debian/
2. Descargan el .deb y ejecutan:
```bash
sudo apt install ./(el .deb que descargaron)
```
* En debian hay otra forma de instalarlo y es a travez del repositorio apt(que no consume recursos.)
```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```
* Estos comandos los encontraran en el enlace oficial de docker.

---


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
5. V 0.5: Ejecucion de la calculadora en terminal sin estar anclado al directorio del proyecto.
6. V 0.6: remplazo del endoesqueleto(codigo) a la POO
