def save_keys(file_path, keys):
    """Guarda las llaves en el archivo ubicado en file_path

    Las llaves deben ser una lista de tuplas. Cada tupla
    representa un punto. Ej: [(1,3), (8,9), (14, 123), (28, 2)]

    Parameters:
    -----------
    file_path: str
        El path del archivo donde se van a guardar los puntos
    keys: list of (tuples of int)
        Los puntos a guardar
    """
    document=open(file_path, 'w')
    n = len(keys)
    for i in range(n):
        point = keys[i]
        x = point[0]
        y = point[1]
        line = str(x) "," str(y)
        document.write(line)
    document.close()

  

def read_keys(file_path):
    """Obtiene los puntos almacenados en el archivo ubicado
    en file_path.

    Las llaves obtenidas deben ser una lista de tuplas. Cada tupla
    representa un punto. Ej: [(1,3), (8,9), (14, 123), (28, 2)]

    Parameters:
    -----------
    file_path: str
        El path del archivo donde se encuentras los puntos

    Returns:
    --------
    list of (tuples of int)
        Las llaves leidas
    """
    file = open(file_path, 'r')
    shares = list()
    for line in file:
        line = line.strip()
        points_str = line.split(",")
        point = (int(points_str[0]), int(points_str[1]))
        shares.append(point)
    return points



