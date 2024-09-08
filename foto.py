# foto.py
from error import DimensionError

class Foto:
    """
    Clase que representa una foto con ancho y alto.

    Atributos:
    ----------
    MAX : int
        Valor máximo permitido para el ancho y alto de la foto.
    _ancho : int
        Ancho de la foto (valor privado, modificado solo por el setter).
    _alto : int
        Alto de la foto (valor privado, modificado solo por el setter).

    Métodos:
    --------
    ancho():
        Getter para el ancho de la foto.
    ancho(value):
        Setter para el ancho de la foto. Lanza una excepción DimensionError
        si el valor ingresado es menor a 1 o mayor a MAX.
    alto():
        Getter para el alto de la foto.
    alto(value):
        Setter para el alto de la foto. Lanza una excepción DimensionError
        si el valor ingresado es menor a 1 o mayor a MAX.
    """

    MAX = 1000  # Valor máximo permitido para las dimensiones de la foto.

    def __init__(self, ancho, alto):
        """
        Constructor para crear una nueva instancia de Foto.

        Parámetros:
        -----------
        ancho : int
            Valor inicial del ancho de la foto.
        alto : int
            Valor inicial del alto de la foto.
        """
        self._ancho = None
        self._alto = None
        self.ancho = ancho  # Utilizamos el setter para validar el valor.
        self.alto = alto    # Utilizamos el setter para validar el valor.

    @property
    def ancho(self):
        """
        Getter para el ancho de la foto.

        Retorna:
        --------
        int:
            Valor del ancho de la foto.
        """
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        """
        Setter para el ancho de la foto. Valida que el valor ingresado sea mayor
        o igual a 1 y menor o igual al valor máximo permitido (MAX).
        Si no se cumple la condición, lanza una excepción DimensionError.

        Parámetros:
        -----------
        value : int
            Nuevo valor para el ancho de la foto.
        
        Excepciones:
        ------------
        DimensionError:
            Si el valor es menor que 1 o mayor que MAX.
        """
        if value < 1 or value > Foto.MAX:
            raise DimensionError("Valor inválido para ancho", "ancho", Foto.MAX)
        self._ancho = value

    @property
    def alto(self):
        """
        Getter para el alto de la foto.

        Retorna:
        --------
        int:
            Valor del alto de la foto.
        """
        return self._alto

    @alto.setter
    def alto(self, value):
        """
        Setter para el alto de la foto. Valida que el valor ingresado sea mayor
        o igual a 1 y menor o igual al valor máximo permitido (MAX).
        Si no se cumple la condición, lanza una excepción DimensionError.

        Parámetros:
        -----------
        value : int
            Nuevo valor para el alto de la foto.
        
        Excepciones:
        ------------
        DimensionError:
            Si el valor es menor que 1 o mayor que MAX.
        """
        if value < 1 or value > Foto.MAX:
            raise DimensionError("Valor inválido para alto", "alto", Foto.MAX)
        self._alto = value
