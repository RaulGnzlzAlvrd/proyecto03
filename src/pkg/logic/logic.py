def encriptar(shares_path, n, t, document_path):
    """Encripta el archivo ubicado en document_path, genera el
    archivo shares_path con los n puntos requeridos.
    El valor de t debe ser menor igual a n.

    Parameters:
    -----------
    shares_path: str
        El path del archivo donde se van a guardar los puntos
    n: int
        El número total de puntos a generar
    t: int
        El número mínimo de puntos para desencriptar
    document_path: str
        El path del archivo que se va a encriptar
    """
    pass

def desencriptar(shares_path, document_path):
    """Desencripta el archivo ubicado en document_path, usando
    las llaves almacenadas en shares_path.

    Parameters:
    -----------
    shares_path: str
        El path del archivo donde están los puntos
    document_path: str
        El path del archivo a desencriptar
    """
    pass
