from error import DimensionError  # Importamos la excepción personalizada

class Foto:
    MAX = 2500  # Valor máximo permitido para ancho y alto

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Constructor de la clase Foto. Inicializa los atributos de ancho, alto y ruta.
        Se utilizan los setters para validar el ancho y el alto.
        
        Parámetros:
        -----------
        ancho : int
            Ancho inicial de la foto.
        alto : int
            Alto inicial de la foto.
        ruta : str
            Ruta del archivo de la foto.
        """
        self.ancho = ancho  # Usamos el setter para validar el valor
        self.alto = alto    # Usamos el setter para validar el valor
        self.ruta = ruta    # Se asigna la ruta, aunque no es validada

    @property
    def ancho(self) -> int:
        """
        Getter para el atributo ancho.
        
        Retorna:
        --------
        int:
            El valor actual del ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """
        Setter para el atributo ancho. Valida que el valor esté dentro de los límites permitidos.
        
        Parámetros:
        -----------
        ancho : int
            Nuevo valor para el ancho de la foto.
        
        Lanza:
        ------
        DimensionError:
            Si el valor de ancho es menor a 1 o mayor a MAX.
        """
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Valor inválido para ancho", "ancho", Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """
        Getter para el atributo alto.
        
        Retorna:
        --------
        int:
            El valor actual del alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """
        Setter para el atributo alto. Valida que el valor esté dentro de los límites permitidos.
        
        Parámetros:
        -----------
        alto : int
            Nuevo valor para el alto de la foto.
        
        Lanza:
        ------
        DimensionError:
            Si el valor de alto es menor a 1 o mayor a MAX.
        """
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Valor inválido para alto", "alto", Foto.MAX)
        self.__alto = alto
