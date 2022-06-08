def generate_shares(n, K, t):
    """Genera n puntos (shares), usando el esquema SSSS.

    Parameters:
    -----------
    n: int
        El número de puntos evaluados en el polinomio
    K: int
        El término independiente en el polinomio generado.
    t: int
        El grado del polinomio generado (t-1)

    Returns:
    --------
    list of(tuples of int)
        Los puntos generados
    """
    pass

def regenerate_key(shares):
    """Regenera la llave K a partir de los puntos.

    Parameters:
    -----------
    shares: list of(tuples of int)
        Los puntos

    Returns:
    --------
    int
        La llave recuperada
    """
    pass
