# foto.py
from error import DimensionError

class Foto:
    MAX = 1000  # Ejemplo de valor máximo, este puede cambiar según el contexto
    
    def __init__(self, ancho, alto):
        self._ancho = None
        self._alto = None
        self.ancho = ancho  # Utilizamos el setter
        self.alto = alto    # Utilizamos el setter

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        if value < 1 or value > Foto.MAX:
            raise DimensionError("Valor inválido para ancho", "ancho", Foto.MAX)
        self._ancho = value

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        if value < 1 or value > Foto.MAX:
            raise DimensionError("Valor inválido para alto", "alto", Foto.MAX)
        self._alto = value
