import sys
from ..logic import encriptar, desencriptar

def run():
    """Ejecuta la interfaz de línea de comandos (CLI).

    Valida los parámetros y manda llamar las funcionalidades base
    de la aplicación.
    """
    # Leer las opciones de la linea de comandos
    #if opcion == "c":
    #    encriptar(...)
    #if opcion == "d":
    #    desecriptar(...)
    argumentos = sys.argv
    if len(argumentos <= 1):
        print('argumentos inválidos')
    elif 'c' == argumentos[1]:
        path_archivo = argumentos[2]
        claves_totales = int(argumentos[2])
        claves_necesarias = int(argumentos[3])
        path_archivo_claves = argumentos[4]
        encriptar(path_archivo, claves_totales, claves_necesarias, path_archivo_claves)
    elif 'd' == argumentos[1]:
        path_arch_encriptado = argumentos[2]
        path_t_claves = argumentos[3]
        desecriptar(path_arch_encriptado,path_t_claves)
    else:
        print('argumentos invalidos')

