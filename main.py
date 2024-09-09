from apoyo_desafio import Foto
from error import DimensionError

def main():
    # Caso 1: Creación de una foto válida
    try:
        foto_valida = Foto(1200, 800, 'ruta/foto.jpg')
        print(f"Foto creada correctamente con ancho {foto_valida.ancho} y alto {foto_valida.alto}")
    except DimensionError as e:
        print(f"Error al crear la foto válida: {e}")

    # Caso 2: Intentar asignar un valor de ancho mayor al permitido (mayor que MAX)
    try:
        foto_valida.ancho = 3000  # Esto debería lanzar una excepción
    except DimensionError as e:
        print(f"Error al modificar el ancho: {e}")

    # Caso 3: Intentar crear una foto con un valor de alto inválido (menor a 1)
    try:
        foto_invalida = Foto(500, 0, 'ruta/foto2.jpg')  # Esto debería lanzar una excepción
    except DimensionError as e:
        print(f"Error al crear la foto con alto inválido: {e}")

if __name__ == "__main__":
    main()
