
### Encriptar 
#### Entrada 
- archivo 
- n (cantidad de claves)
- t (cantidad claves necesarias)
- archivo_claves 

#### Salida
- archivo encriptado
- archivo_claves

#### En ejecucion:
- Pedir contraseña sin hacer eco
- Crear el hash con base en la contraseña 
- Construir las n llaves con base en hash 
- Guardar las n llaves en el archivo de llaves 
- Encriptar el archivo 

### Desencriptar
#### Entrada 
- archivo encirptado 
- archivo con al menos t claves 

#### Salida
- archivo desencriptado

#### En ejecución:
- Leer el archivo de las t llaves 
- Reconstruir el hash con base en las t llaves 
- Desencriptar el archivo con el hash 


### En terminal 
- escoger la opción encriptar o desencriptar 
- verificar parametros de la opcion escogida 
