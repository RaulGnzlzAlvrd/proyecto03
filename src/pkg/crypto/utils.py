def gcd(a,b):
    """
    Computa el máximo común divisor d entre dos
    enteros positivos a, b con a>= b

    params:
    int: a
    int: b

    return: 
    int: d El máximo común divisor
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_ext(a,b):
    """
    Algoritmo extendido de Euclides que regresa
    el máximo común divisor d para a,b y además
    regresa x,y tal que d = ax + by

    params:
    int: a
    int: b

    return:
    (int, int, int): (d,x,y)
    """
    if b == 0:
        return (a,1,0)
    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0
    while b > 0:
        q = a // b
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return (a, x2, y2)

def inverse_zn(a, n):
    """
    Calcula el inverso multiplicativo de a en Zn si es
    que existe

    params:
    int: a
    int: b

    return:
    int: a^{-1}
    """
    d, _, y = gcd_ext(n,a)
    if d == 1:
        return y % n
    else:
        raise Exception("No existe el inverso multiplicativo de {} en Z{}".format(a,n))
