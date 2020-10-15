# Taller_Redes_PGSQL

Este repositorio tiene como finalidad instalar Dockerfile tanto para cliente como para su servidor, para fines practicos como tambien analisis de tráficos.
## Entrega 1:
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
Una vez ingresado, pedirá la clave en este caso es `12345` 


### Video explicativo y análisis de tráfico

[[Watch the video]](https://youtu.be/meM9peWLYMg)

## Entrega 2:

Esta segunda entrega tiene como finalidad poder interceptar y modificar packetes de datos en relacion a nuestro software postgresSQL, para ello es necesario ocupar `Polymorph` que nos permita facilmete modifacar estos paquetes a traves de funciones creadas por nosotros.

### Instalacion de Polymorph 

Para ello es necesarios basarnos en el repositorio de `Shamos` donde tenemos que seguir los siguentes pasos:

Es necesario saber que este framework está diseñado para instalarse y ejecutarse en entorno linux, antes de instalarlo son necesarios los siguientes requisitos:

```
apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git
```

Después de la instalación de las dependencias, el marco en sí se puede instalar con el administrador de paquetes Python pip de la siguiente manera:

```
pip3 install git+https://github.com/kti/python-netfilterqueue
pip3 install polymorph
```

Una vez instalado en el equipo, ademas del softwere de trabajo (PostgreSQL) es posible interceptar información, como modelos hay un `File` de nombre `funciones` que permiten realizar analisis a diferentes sentencias como tambien en la conexión con la base de datos.





