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
$ cd /taller_de_redes/servidor/
$ docker build -t frodenas/postgresql .
```

### Arranque del servidor
para ejecutar la imagen y seleccionar el puerto 5432, es necesario:
```
$ docker run -d --name postgresql -p 5432:5432 frodenas/postgresql

```
La primera vez que ejecute su contenedor, `pgadmin` creará un nuevo usuario con todos los privilegios con una contraseña aleatoria. Para obtener la contraseña, verifique los registros del contenedor ejecutando:

```
$ docker logs <CONTAINER_ID>
```
Verá una salida como la siguiente:
```
========================================================================
PostgreSQL User: "pgadmin"
PostgreSQL Password: "WH7fwqY7bJCEMYKC"
========================================================================
```

Si desea crear una base de datos en el momento del arranque del contenedor, puede ocupar:

```
$ docker run -d \
    --name postgresql \
    -p 5432:5432 \
    -e POSTGRES_USERNAME=myuser \
    -e POSTGRES_PASSWORD=mypassword \
    -e POSTGRES_DBNAME=mydb \
    -e POSTGRES_EXTENSIONS=citext \
    frodenas/postgresql
```
### Arranque del cliente
Para realizar la imagen del `cliente` de postgres, ingresar el comando:

```
docker run -it cliente
$ psql -p 5432 -U pgadmin -P zxM9Ye0sB2eZthEe

```
## Video capturando trafico generado entre el servidor y cliente

[![Watch the video](https://t.jpg)](https://youtu.be/)
