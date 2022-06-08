from ..io import save_keys, read_keys, get_password
from ..crypto import sha256sum, aes_encrypt, aes_decrypt
from ..crypto import generate_shares, regenerate_key

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
    user_pass = get_password()  # facil  # miriam
    K = sha256sum(user_pass) # facil   # beca
    shares = generate_shares(n, K, t) # difícil # beca

    # [(6,5), (7,10), (1,3)]
    save_keys(shares_path, shares) # medio   # miriam
    aes_encrypt(document_path, K) # medio   # raúl

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
    shares = read_keys(shares_path) # medio  # miriam
    K = regenerate_key(shares) # difícil    # miriam
    aes_decrypt(document_path, K) # medio   # raúl
