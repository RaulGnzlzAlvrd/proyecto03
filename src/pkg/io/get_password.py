import getpass

def get_password():
    """Obtiene una contraseña desde la línea de comandos
    ingresada por el usuario. La contraseña no se 
    muestra en consola mientras se teclea.

    Returns:
    --------
    str:
        La contraseña ingresada por el usuario
    """
    try:
        p = getpass.getpass(prompt= 'Ingresa tu contraseña: ', stream=None)

    except Exception as err:
        print('ERROR:', err)
    else:
        return p
