import base64
import hashlib 

def sha256sum(phrase):
    """Regresa el sha256sum de phrase.

    Parameters:
    -----------
    phrase: str
        La cadena a la que se le calcula en hash

    Returns:
    --------
    str:
        El hash calculado con el algoritmo sha256sum
    """
    m = hashlib.sha256()
    m.update(phrase.encode('utf-8'))
    hashed = m.hexdigest()
    return hashed