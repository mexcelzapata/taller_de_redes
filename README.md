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

https://youtu.be/meM9peWLYMg

## Entrega 2:

Esta segunda entrega tiene como finalidad poder interceptar y modificar packetes de datos en relacion a nuestro software postgresSQL, para ello es necesario ocupar `Polymorph` que nos permita facilmete modifacar estos paquetes a traves de funciones creadas por nosotros.

### Instalacion de Polymorph 

Para ello es necesarios basarnos en el repositorio de `Shramos` donde tenemos que seguir los siguentes pasos:

Es necesario saber que este framework está diseñado para instalarse y ejecutarse en entorno linux, antes de instalarlo son necesarios los siguientes requisitos:

```
apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git
```

Después de la instalación de las dependencias, el marco en sí se puede instalar con el administrador de paquetes Python pip de la siguiente manera:

```
pip3 install git+https://github.com/kti/python-netfilterqueue
pip3 install polymorph
```
Para mas información y soporte sobre `Polymorph` visita: https://github.com/shramos/polymorph .
Una vez instalado en el equipo, ademas del softwere de trabajo (PostgreSQL) es posible interceptar información, como modelos hay un `File` de nombre `funciones` que permiten realizar analisis a diferentes sentencias como tambien en la conexión con la base de datos.

### Video Explicativo 
Puedes revisar este video para saber como y cuando aplicar las funciones que estan en este repositorio.

https://www.youtube.com/watch?v=UEimNt_zGLY



## Entrega 3

En esta tercera entrega, se dio paso a trabajar con diferentes metricas dentro de la red, con la finalidad de ver como estas modificaciones afectan al software postgres.
Es por ello que en esta entrega es necesario trabajar con dos metodos que se describiran a continuacion:


### Metodo pasivo
Este metodo tiene como finalidad por ver en tiempo real el comportamiento del trafico generado entre el cliente y servidor. En primera instacia en necesario ocupar la herramienta `Netem` que nos permita controlar el trafico generado en la red, donde se aplicó un delay de 100ms:
```
 tc qdisc add dev eth0 root netem delay 100s 10ms distribution pareto
```
Una vez estabecido el delay a ocupar dentro del contenedor del cliente, es necesario utilizar `Polymorph` para poder interceptar los paquetes y poder desplegar el contenido en tiempo real del trafico generado entre el servidor y cliente.

la funcion empleada esta en `entrega_3/funcion_polymorph`, donde se trabaja la metrica de throughput dentro de la red.


### Metodo Activo
En este metodo fue necesario segmentar en 4 tipos de metricas, donde para cada una fue necesario realzar sus capturas correspondientes que nos permitió poder analizar las metricas dentro de ellas.

#### Delay
Para este caso, se ocupó una modificación de `Netem` de:
```
 tc qdisc add dev eth0 root netem delay 100s 10ms distribution pareto
 ```
Se puede apreciar en la carpeta de entrega_3/delay las diferentes capturas empleadas en esta métrica.

####  Packet corrupted

Para este caso, se ocupó una modificación de `Netem` de:
```
 tc qdisc add dev eth0 root netem corrupt 20%
 ```
Se puede apreciar en la carpeta de  entrega_3/packet_corrupted las diferentes capturas empleadas en esta métrica.

#### Packet Loss

Para este caso, se ocupó una modificación de `Netem` de:
```
  tc qdisc add dev eth0 root netem loss 40%
 ```
Se puede apreciar en la carpeta de  entrega_3/packet_loss las diferentes capturas empleadas en esta métrica.


#### Throughput

Para este caso, se ocupó una modificación de `Netem` de:
```
  tc qdisc add dev eth0 root netem delay 1000ms 30ms distribution pareto
 ```
Se puede apreciar en la carpeta de  entrega_3/throughput las diferentes capturas empleadas en esta métrica.

### Video Explicativo 
Puedes revisar este video para saber como y cuando aplicar las funciones que estan en este repositorio.
https://www.youtube.com/watch?v=-3PKxx-TLBo

## Entrega final

En este trabajo trataremos un concepto de herramienta que nos ayudara en este ámbito llamado IDS (Integrated Development Environment) en especifico trabajaremos con Snort el cual es uno de los IDS más conocidos.

### PCRE
```
alert tcp 172.17.0.2 any -> 172.17.0.3 5432( msg:"PostgreSQL constant deletions"; flow:established; pcre:"^((delete)|(DELETE)){1}";offset :0; sid:1000001; rev:20; )
```
### Activate/dynamic
```
activate tcp 172.17.0.2 any -> 172.17.0.3 5432 (flags: PA; msg:"Authentication request"; flow:established; activates: 1; content:"|52 00 00 00 0c|",depth 5; sid:1000006; rev:20;) 
dynamic tcp 172.17.0.2 any -> 172.17.0.3 5432 (activated_by: 1; count: 4;)
```
### Offset
```
alert tcp 172.17.0.2 any -> 172.17.0.3 5432 (msg:"consecutive insertions"; flow:established; content:"INSERT"; offset:0; content:"1"; offset:7; sid:1000003; rev:20; )
```
### dsize
```
alert tcp 172.17.0.2 any -> 172.17.0.3 5432 (msg:"Buffer overflow"; flow:established; dsize:>8192; sid:1000004; rev:1; )
```

### Flow
```
alert tcp 172.17.0.2 any -> 172.17.0.3 5432 (msg:"constant Authentication request"; flow:established; content:"|52 00 00 00 0c|",depth 5; sid:1000002; rev:20; )
```
### Video Explicativo 
Puedes revisar este video para saber que hacen las reglas que estan en este repositorio.
https://youtu.be/EG6499TvPmg








