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
    if len(argumentos) <= 1:
        print('argumentos inválidos')
    elif 'c' == argumentos[1]:
        if len(argumentos)  == 6:
            path_archivo_claves = argumentos[2]
            claves_totales = argumentos[3]
            claves_necesarias = argumentos[4]
            path_archivo = argumentos[5]
            if claves_totales.isdigit() and claves_necesarias.isdigit() :
                encriptar(path_archivo_claves, int(claves_totales), int(claves_necesarias), path_archivo)
            else:
                print('argumentos invalidos')
        else:
            print('argumentos invalidos')
    elif 'd' == argumentos[1]:
        if len(argumentos) == 4:
            path_t_claves = argumentos[2]
            path_arch_encriptado = argumentos[3]
            desencriptar(path_t_claves,path_arch_encriptado)
        else:
            print('argurmntos invalidos')
    else:
        print('argumentos invalidos')

