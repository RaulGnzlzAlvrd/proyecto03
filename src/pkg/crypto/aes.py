from ..config.default import IV

from os import path
import re
import subprocess

def aes_encrypt(file_path, key):
    """Encripta el archivo ubicado en file_path usando el
    algoritmo AES junto con la llave.

    Parameters:
    -----------
    file_path: str
        La ubicación del archivo a encriptar
    key: str
        La llave usada en el algoritmo AES
    """
    command_template = f"""openssl enc -nosalt -aes-256-cbc \
        -in {file_path} -out {file_path}.aes \
        -base64 -K {key} -iv {IV}"""
    command = re.sub(" +", " ", command_template)
    result = subprocess.run(command.split(" "), stdout=subprocess.DEVNULL)
    if result.returncode != 0:
        raise Exception(f"Ocurrió un error al intentar encriptar:\n{command_template}")

def aes_decrypt(file_path, key):
    """Desencripta el archivo ubicado en file_path usando
    el algoritmo AES junto con la llave

    Parameters:
    -----------
    file_path: str
        La ubicación del archivo a desencriptar
    key: str
        La llave usada en el algoritmo AES
    """
    decrypted_file_path = _create_decrypted_path(file_path)
    command_template = f"""openssl enc -nosalt -aes-256-cbc -d \
            -in {file_path} -out {decrypted_file_path} \
            -base64 -K {key} -iv {IV}"""
    command = re.sub(" +", " ", command_template)
    result = subprocess.run(command.split(" "), stdout=subprocess.DEVNULL)
    if result.returncode != 0:
        raise Exception(f"Ocurrió un error al intentar desencriptar:\n{command_template}")

def _create_decrypted_path(file_path):
    """Crea el nombre del archivo desencriptado a partir del nombre
    del archivo encriptado.

    Parameters:
    -----------
    file_path: str
        El nombre del archivo encriptado

    Returns:
    --------
    str:
        El nombre del destino del archivo desencriptado
    """
    file_path = path.splitext(file_path)[0]
    dirname = path.dirname(file_path)
    file_name = f"DECRYPTED-{path.basename(file_path)}"
    return path.join(dirname, file_name)
