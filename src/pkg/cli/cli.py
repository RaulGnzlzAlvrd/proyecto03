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
        if len(argumentos)  == 5:
            path_archivo = argumentos[2]
            claves_totales = argumentos[2]
            claves_necesarias = argumentos[3]
            path_archivo_claves = argumentos[4]
            if claves_totales.isdigit() and claves_necesarias.isdigit() :
                encriptar(path_archivo, int(claves_totales), int(claves_necesarias), path_archivo_claves)
            else:
                print('argumentos invalidos')
        else:
            print('argumentos invalidos')
    elif 'd' == argumentos[1]:
        if len(argumentos) == 4:
            path_arch_encriptado = argumentos[2]
            path_t_claves = argumentos[3]
            desecriptar(path_arch_encriptado,path_t_claves)
        else:
            print('argurmntos invalidos')
    else:
        print('argumentos invalidos')

