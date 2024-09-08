# error.py
class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        return f"{self.mensaje}. Dimension: {self.dimension}, Maximo permitido: {self.maximo}"
