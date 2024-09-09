# Proyecto: Manejo de Excepciones en una Galería de Fotos

Este proyecto tiene como objetivo la implementación de excepciones personalizadas en una aplicación que gestiona fotos. La aplicación controla los valores de ancho y alto de las fotos, lanzando una excepción propia (`DimensionError`) si dichos valores no cumplen con los límites establecidos. 

El proyecto está basado en los requerimientos de un desafío de manejo de excepciones, en el cual se especifica que los valores de las dimensiones de las fotos deben estar entre 1 y un valor máximo (`MAX`).

## Estructura del Proyecto

El proyecto se organiza en los siguientes archivos:

📁 proyecto_galeria_fotos │ ├── 📄 error.py # Definición de la excepción personalizada DimensionError. ├── 📄 apoyo_desafio.py# Clase Foto con validación de dimensiones. └── 📄 main.py # Archivo para ejecutar pruebas.

## Descripción de los Archivos

### `error.py`

Este archivo contiene la definición de la excepción personalizada `DimensionError`. La excepción es utilizada para manejar errores relacionados con las dimensiones (ancho y alto) de las fotos, lanzándose cuando los valores ingresados no cumplen con los requisitos.

- **Atributos**:
  - `mensaje`: Describe el error.
  - `dimension`: (Opcional) La dimensión que causó el error (ancho o alto).
  - `maximo`: (Opcional) Valor máximo permitido para la dimensión.

- **Métodos**:
  - `__str__()`: Retorna un mensaje detallado del error. Si solo se proporciona un mensaje, usa el método de la clase base `Exception`.

### `apoyo_desafio.py`

Este archivo define la clase `Foto`, que representa una foto con atributos de ancho, alto y ruta. El control de los valores de ancho y alto está implementado en los setters, donde se lanzan excepciones si los valores están fuera de los límites permitidos.

- **Atributos**:
  - `MAX`: Valor máximo permitido para el ancho y el alto (2500).
  - `ancho` y `alto`: Atributos que representan las dimensiones de la foto.

- **Métodos**:
  - `ancho.setter`: Valida el valor de ancho, lanzando una excepción `DimensionError` si el valor es menor a 1 o mayor a `MAX`.
  - `alto.setter`: Valida el valor de alto, lanzando una excepción `DimensionError` si el valor es menor a 1 o mayor a `MAX`.

## Ejecución del Proyecto

Para ejecutar el proyecto, puedes utilizar el archivo `main.py` para realizar pruebas de los distintos escenarios donde se pueden lanzar excepciones. A continuación, se presentan ejemplos básicos de uso.

### Ejemplo 1: Crear una foto válida

```python
from apoyo_desafio import Foto
from error import DimensionError

try:
    foto_valida = Foto(1200, 800, 'ruta/foto.jpg')
    print(f"Foto creada correctamente con ancho {foto_valida.ancho} y alto {foto_valida.alto}")
except DimensionError as e:
    print(f"Error al crear la foto válida: {e}")



### Requisitos

- Python 3.x
- No se requieren librerías externas adicionales.
  
