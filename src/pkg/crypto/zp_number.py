import random
from utils import inverse_zn

class ZpNumber:
    """Representa un número dentro de un campo Zp.

    Implementa operaciones aritméticas básicas con notación infija.
    Puede operar entre objetos del mismo tipo o con números usuales
    de python. El resultado de cualquier operación aritmética con este
    objeto es otro objeto de esta misma clase usando el mísmo módulo.

    El módulo p puede ser primo o no, pero se recomienda usar primo
    para tener bien definida la división.
    """

    def __init__(self, value, p):
        """Crea un número dentro de el campo Zp
        
        Parameters:
        -----------
        value: number
            El valor que tendrá dentro del campo
        p: number
            El módulo del campo

        Returns:
        --------
        ZpNumber:
            La instancia creada
        """
        self.value = value % p
        self.p = p

    def randomNumber(p):
        """Método de clase. Genera un número aleatorio dentro del campo
        módulo p.

        Parameters:
        -----------
        p: number
            El módulo del campo

        Returns:
        --------
        ZpNumber:
            En número aleatorio
        """
        number = random.randint(0, p-1)
        return ZpNumber(number, p)

    def __add__(self, other):
        """Aplica la operación aritmética suma de la forma self + other

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a sumar

        Returns:
        --------
        ZpNumber:
            El resultado de la suma
        """
        if not isinstance(other, ZpNumber):
            other = ZpNumber(other, self.p)
        result_value = (self.value + other.value) % self.p
        return ZpNumber(result_value, self.p)

    def __sub__(self, other):
        """Aplica la operación aritmética resta de la forma self - other

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a restar

        Returns:
        --------
        ZpNumber:
            El resultado de la resta
        """
        if not isinstance(other, ZpNumber):
            other = ZpNumber(other, self.p)
        inverse_other = other.get_additive_inverse()
        return self.__add__(inverse_other)

    def __mul__(self, other):
        """Aplica la operación aritmética multiplicación de la forma
        self * other

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a multiplicar

        Returns:
        --------
        ZpNumber:
            El resultado de la multiplicación
        """
        if not isinstance(other, ZpNumber):
            other = ZpNumber(other, self.p)
        result_value = (self.value * other.value) % self.p
        return ZpNumber(result_value, self.p)

    def __div__(self, other):
        """Aplica la operación aritmética división de la forma
        self / other

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a dividir

        Returns:
        --------
        ZpNumber:
            El resultado de la división
        """
        if not isinstance(other, ZpNumber):
            other = ZpNumber(other, self.p)
        inverse_other = other.get_multiplicative_inverse()
        return self.__mul__(inverse_other)
    
    def __truediv__(self, other):
        """Aplica la operación aritmética división de la forma
        self / other

        Tienen que estar implementados __div__ y __truediv__ para
        que funcione la división usual.

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a dividir

        Returns:
        --------
        ZpNumber:
            El resultado de la división
        """
        if not isinstance(other, ZpNumber):
            other = ZpNumber(other, self.p)
        inverse_other = other.get_multiplicative_inverse()
        return self.__mul__(inverse_other)

    def __radd__(self, other):
        """Aplica la operación aritmética suma por la derecha de la forma
        other + self

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a suma

        Returns:
        --------
        ZpNumber:
            El resultado de la suma
        """
        return self.__add__(other)

    def __rsub__(self, other):
        """Aplica la operación aritmética resta por la derecha de la forma
        other - self

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a restar

        Returns:
        --------
        ZpNumber:
            El resultado de la resta
        """
        inverse = self.get_additive_inverse()
        return inverse.__add__(other)

    def __rmul__(self, other):
        """Aplica la operación aritmética multiplicación por la derecha
        de la forma other * self

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a multiplicar

        Returns:
        --------
        ZpNumber:
            El resultado de la multiplicación
        """
        return self.__mul__(other)

    def __rdiv__(self, other):
        """Aplica la operación aritmética división por la derecha
        de la forma other / self

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a dividir

        Returns:
        --------
        ZpNumber:
            El resultado de la división
        """
        inverse = self.get_multiplicative_inverse()
        return inverse.__mul__(other)

    def __rtruediv__(self, other):
        """Aplica la operación aritmética división por la derecha
        de la forma other / self

        Tienen que estar implementados __div__ y __truediv__ para
        que funcione la división usual.

        Parameters:
        -----------
        other: number | ZpNumber
            El número con el que se va a dividir

        Returns:
        --------
        ZpNumber:
            El resultado de la división
        """
        inverse = self.get_multiplicative_inverse()
        return inverse.__mul__(other)

    def get_multiplicative_inverse(self):
        """Regresa el inverso multiplicativo de self dentro
        del campo Zp.

        Returns:
        --------
        ZpNumber:
            El inverso multiplicativo
        """
        inverse = inverse_zn(self.value, self.p)
        return ZpNumber(inverse, self.p)

    def get_additive_inverse(self):
        """Regresa el inverso aditivo de self dentro
        del campo Zp.

        Returns:
        --------
        ZpNumber:
            El inverso aditivo
        """
        return ZpNumber(-self.value, self.p)

    def __str__(self):
        """Regresa la representación en cadena del individuo,
        que solo es su valor entero.

        Returns:
        --------
        str:
            La representación de su valor entero
        """
        return str(self.value)

    def __repr__(self):
        """Regresa la representación que se usa en el intérprete
        interactivo de python. Es una representación más completa
        que dice su valor y el campo en el que está.

        Returns:
        --------
        str:
            La representación más detallada
        """
        return f"value: {self.value}\nmodulus: {self.p}"

    def __eq__(self, other):
        """Dice si self es equivalente a other, usando self == other

        Parameters:
        -----------
        other: any
            El objeto con el que se va a comparar

        Returns:
        --------
        boolean:
            True si son equivalentes, False en otro caso
        """
        if isinstance(other, ZpNumber):
            same_value = self.value == other.value
            same_p = self.p == other.p
            return same_value and same_p
        return False
