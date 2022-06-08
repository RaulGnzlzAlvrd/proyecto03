def encriptar(path_archivo, n, t, path_claves):
    user_pass = get_password()  # facil  # miriam
    K = generate_hash(user_pass) # facil   # beca
    llaves = generate_keys(n, K, t) # difícil # beca
    # [(6,5), (7,10), (1,3)]
    save_keys(path_claves, llaves) # medio   # miriam
    encript_aes(path_archivo, K) # medio   # raúl



def desecriptar(path_archivo, path_claves):
    llaves = read_keys(path_claves) # medio  # miriam
    K = regenerate_key(llaves) # difícil    # miriam
    decrypt_aes(K, path_archivo) # medio   # raúl

# media
def main():  # beca
    # Leen las opciones de la linea de comandos
    if opcion == "c":
        encriptar(...)
    if opcion == "d":
        desecriptar(...)
