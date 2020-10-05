# Taller_Redes_PGSQL

Este repositorio tiene como finalidad instalar Dockerfile tanto para cliente como para su servidor, para fines practicos como tambien analisis de tráficos.

### Instalacion del Repositorio
Se debe clonar este repositorio en la terminal con el comando:

```
$ git clone https://github.com/mexcelzapata/taller_de_redes.git
```
### Instalacion de imagenes 
Para la instalación de la imagen `Cliente` de Postgres se debe ingresar el comando:
```
$ docker build -t cliente taller_de_redes/client/
```
Para la instalación de la imagen `Servidor` de Postgres se debe ingresar en la carpeta `servidor`, el comando:
```
$docker build -t servidor taller_de_redes/servidor

```
### Arranque del servidor
Para ejecutar la imagen del `servidor`  es necesario:

```
$ docker run -it servidor
```

### Arranque del cliente
Para realizar la imagen del `cliente` de postgres, ingresar el comando:

```
docker run -it cliente

```
Para establecer la conexión es necesario saber la ip del `servidor`:
```
$ psql -h ip_servidor -p 5432 -U postgres

```
Una vez ingresado, pedirá la clave en este caso es `12345`.
### Video explicativo y análisis de tráfico

[![Watch the video]](https://youtu.be/meM9peWLYMg)
