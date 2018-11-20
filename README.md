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

