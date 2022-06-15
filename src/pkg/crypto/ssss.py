from zp_number import ZpNumber
from polynomial import horner_rule

from ..config.default import MODP 
def generate_shares(n, K, t):
    """Genera n puntos (shares), usando el esquema SSSS.

    Parameters:
    -----------
    n: int
        El número de puntos evaluados en el polinomio
    K: str
        El término independiente en el polinomio generado.
    t: int
        El grado del polinomio generado (t-1)

    Returns:
    --------
    list of(tuples of int)
        Los puntos generados
    """
    k_int = int(K,16)
    key = ZpNumber(k_int, MODP)
    coefs = [ZpNumber.randomNumber(MODP) for _ in range(t)]
    coefs[0] = key
    X = [ZpNumber.randomNumber(MODP) for _ in range(n)]
    shares = list()
    for x in X:
        y = horner_rule(x, coefs)
        shares.append((x,y))
    return shares

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
    key = lagrange_polynomial(shares, 0)
    hex_key = hex(key)[2:].upper()
    return hex_key
