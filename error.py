# error.py
class DimensionError(Exception):
    """
    Excepción personalizada para manejar errores de dimensiones inválidas en la clase Foto.

    Atributos:
    ----------
    mensaje : str
        Mensaje que describe el error.
    dimension : str, opcional
        Nombre de la dimensión que causó el error (ancho o alto).
    maximo : int, opcional
        Valor máximo permitido para la dimensión.
    
    Métodos:
    --------
    __str__():
        Retorna una descripción del error. Si solo se ingresa el mensaje, 
        se utiliza el comportamiento por defecto de la clase Exception.
        Si se ingresan dimension o maximo, retorna un mensaje más detallado.
    """
    def __init__(self, mensaje, dimension=None, maximo=None):
        """
        Constructor de la excepción DimensionError.

        Parámetros:
        -----------
        mensaje : str
            Mensaje que describe el error.
        dimension : str, opcional
            Nombre de la dimensión que causó el error (por defecto None).
        maximo : int, opcional
            Valor máximo permitido para la dimensión (por defecto None).
        """
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self):
        """
        Sobrecarga del método __str__ para retornar un mensaje detallado.

        Retorna:
        --------
        str:
            Si se proporcionan dimension y maximo, retorna un mensaje detallado.
            En caso contrario, retorna el mensaje original utilizando el método
            __str__ de la clase padre (Exception).
        """
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        return f"{self.mensaje}. Dimension: {self.dimension}, Maximo permitido: {self.maximo}"
