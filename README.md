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




variables:

* `POSTGRES_USERNAME` to set a specific username
* `POSTGRES_PASSWORD` to set a specific password
