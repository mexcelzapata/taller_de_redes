# Taller_Redes_PGSQL

### Instalacion del Repositorio
Se debe clonar este repositorio en la terminal con el comando:



```
$ git clone https://github.com/mexcelzapata/taller_de_redes.git
```

Para la instalación del `Cliente` Postgres se debe ingresar el comando:
```
$ docker build -t cliente taller_de_redes/client/
```
Para la instalación del `Seridor` Postgres se debe ingresar el comando:
```
$ docker build -t servidor taller_de_redes/servidor/
```

### Arranque del servidor
para ejecutar la imagen y seleccionar el puerto 5432, junto a una base de datos establecida es necesario:
```
$ docker run -d \
    --name postgresql \
    -p 5432:5432 \
    -e POSTGRES_USERNAME=myuser \
    -e POSTGRES_PASSWORD=mypassword \
    -e POSTGRES_DBNAME=mydb \
    -e POSTGRES_EXTENSIONS=citext \
    taller_de_redes/servidor/
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
