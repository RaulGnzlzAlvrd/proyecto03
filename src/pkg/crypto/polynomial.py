def horner_rule(x, coefs):
    """Se evalúa un polinomio en el punto dado usando
    el método de Horner.

    Parameters:
    -----------
    x: number
        El punto a evaluar
    coefs: list(number)
        Los coeficientes del polinomio. El índice de
        cada elemento corresponde con la potencia.
        En coefs[0] está el término independiente.

    Returns:
    --------
    number
        El resultado de evaluar el punto x en el polinomio
    """
    result = 0
    n = len(coefs)
    for i in range(n-1, -1, -1):
        result = (result * x) + coefs[i]
    return result

def lagrange_polynomial(points, x):
    """Evalúa el polinomio que pasa por los puntos dado, en el punto x.
    
    Se usan los polinomios de lagrange para evaluar el punto sin necesidad
    de calcular el polinomio. El polinomio obtenido es el de menor grado
    que pasa por todos los puntos pasados como parámetro.

    Parameters:
    -----------
    points: list(tuples(number))
        Los puntos por los que pasa el polinomio
    x: number
        El punto donde se quiere evaluar el polinomio

    Returns:
    --------
    number
        El valor obtenido al evaluar el punto x en el polinomio
    """
    result = 0
    r = len(points)
    for i in range(r):
        xi, yi = points[i]
        Pi = 1
        for j in range(r):
            if j == i:
                continue
            xj, _ = points[j]
            Pi = Pi * ((x - xj) / (xi - xj))
        result = result + yi * Pi
    return result
