# Proyecto: Manejo de Excepciones en Aplicación de Galería de Fotos

Este proyecto tiene como objetivo implementar el manejo de excepciones personalizadas en una aplicación que gestiona una galería de fotos. Se controla que no se puedan asignar valores inválidos a los atributos de ancho y alto de las fotos, y se lanza una excepción personalizada (`DimensionError`) cuando los valores ingresados no son válidos.

## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

proyecto_galeria_fotos │ ├── 📄 error.py # Definición de la excepción personalizada DimensionError. ├── 📄 foto.py # Clase Foto con manejo de excepciones en los atributos ancho y alto. └── 📄 README.md # Descripción del proyecto y detalles de implementación.




## Descripción de Archivos

### `error.py`

Este archivo contiene la definición de la excepción personalizada `DimensionError`. Esta excepción es lanzada cuando los valores de ancho o alto de una foto no cumplen con las restricciones establecidas. 

- **Atributos**:
  - `mensaje`: Descripción del error.
  - `dimension`: (Opcional) Dimensión afectada (`ancho` o `alto`).
  - `maximo`: (Opcional) Valor máximo permitido para la dimensión.
  
- **Métodos**:
  - `__init__(mensaje, dimension=None, maximo=None)`: Constructor que inicializa los atributos de la excepción.
  - `__str__()`: Sobrecarga del método que devuelve un mensaje detallado si se proporcionan los atributos `dimension` y `maximo`.

### `foto.py`

Este archivo define la clase `Foto`, que representa una foto con atributos de `ancho` y `alto`. Se asegura que los valores de estos atributos sean válidos mediante el uso de la excepción `DimensionError`.

- **Atributos**:
  - `MAX`: Define el valor máximo permitido para las dimensiones de la foto.
  - `ancho` y `alto`: Representan las dimensiones de la foto y están protegidos mediante setters.

- **Métodos**:
  - `ancho.setter`: Valida el valor de `ancho` y lanza una excepción si no cumple con las restricciones.
  - `alto.setter`: Valida el valor de `alto` y lanza una excepción si no cumple con las restricciones.
 
  ## Ejecución del Proyecto

Para ejecutar el proyecto, puedes importar la clase `Foto` y la excepción `DimensionError` en un archivo de Python. Aquí tienes un ejemplo básico de uso:

```python
from foto import Foto
from error import DimensionError

try:
    foto1 = Foto(500, 600)  # Crear una foto con dimensiones válidas.
    foto1.ancho = 1200       # Intentar asignar un valor fuera de los límites.
except DimensionError as e:
    print(e)  # Manejo de la excepción.


### Requisitos

- Python 3.x
- No se requieren librerías externas adicionales.
  
