# Instalación

Primero es necesario instalar Python 3.7 y tener instalado pip para poder instalar los paquetes necesarios.
Buscad en internet como instalarlo.
<br>

#### Pasos

##### Paso 1 (opcional)

Ejecutamos el siguiente comando para crear un entorno virtual:

```
pip install virtualenv
```

Cuando se instale ejecutamos:

```
virtualenv venv
```

Ahora ya tenemos creado un entorno virtual, para ejecutarlo realizamos:

```
(LINUX):    source venv/bin/activate
(WINDOWS):  .\venv\Scripts\activate
```

##### Paso 2

Instalamos los paquetes necesarios

```
pip install -r requirements.txt
```

##### Paso 3

Ejecutamos el servidor

```
flusk run
```

##### Paso 4

Abrir el navegador con la ruta: http://localhost:5000

##### Paso 5 (OPCIONAL)

Para evitar tener que reiniciar el servidor manualmente cada vez que se realiza un cambio en recomendable activar el hot reload de la siguiente forma:

```
(LINUX):    export FLASK_DEBUG=1
(WINDOWS):  set FLASK_DEBUG=1
```

<br>

# Documentación para la API

### Obtener todas las líneas

```
GET /all-lines

```

devuelve

```
body: {
  status: int; // 200 -> OK
  allLines: [
    {
      name: string;
      color: string; // Color in hexadecimal format
      stations: [
        {
          name: string;
          id: int;
        }
      ];
    }
  ];
}

```

### Obtener ruta más corta entre dos estaciones

```
GET /get-route?origin=string&destination=string

```

devuelve

```
body: {
  status: int; // 200 -> OK
  route: [
    {
      name: string;

      // Contiene el color de la línea correspondiente.
      line: string;

      // En segundos. Contiene el tiempo que requiere ir de la estación anterior a la actual estación.
      // El primer elemento será 0.
      time: double;
    }
  ];
}

```

```

```
