# Modelado y Programación 2022-2, Proyecto 3 - Esquema de Secreto Compartido de Shamir

## Integrantes del equipo:
- Camargo Fortiz Miriam: 313056459
- González Alvarado Raúl: 313245312
- Novella Jiménez Maria Rebeca: 313143926

## Descripción

## Instrucciones de uso
- Instalar dependencias `pip install -r requirements.txt`
- Para ejecutar depende de la acción a realizar:
	- Encriptar: `python -B src/main.py -c shares_path num_shares min_shares document_path` donde `shares_path` es el nombre del archivo donde se van a guardar los puntos (_shares_), `num_shares` el número total de puntos, `min_shares` el número mínimo de puntos necesarios para desencriptar el archivo y `document_path` el path del archivo a encriptar.
	- Desencriptar: `python -B src/main.py -d shares_path document_path`, donde `shares_path` es el nombre del archivo que contiene al menos la cantidad de puntos necesarios para descifrar y `document_path` el nombre del documento cifrado.

> **Nota 1:** Si se ocupan path relativos, deben ser relativos al directorio base del proyecto.

> **Nota 2:** La opción `-B` es para que no se generen archivos cache.

### Ejemplo
**TODO:** Incluir un ejemplo de ejecución

## Instrucciones de testeo
Para ejecutar los tests, desde el directorio raíz (este mismo directorio) ejecutar:
```
python -Bm unittest discover -v
```
