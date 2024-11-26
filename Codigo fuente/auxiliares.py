import hashlib
import getpass
import os

def obtener_contraseña():
    """
    Solicita al usuario una contraseña, la cifra utilizando SHA-256 y devuelve su hash.

    **Parámetros:**  
      - Ninguno.

    **Resultados:**  
      - Devuelve un string que representa el hash hexadecimal de la contraseña ingresada.

    **Precondiciones:**  
      - La entrada del usuario debe ser una contraseña válida.

    **Postcondiciones:**  
      - La contraseña ingresada no se almacena en texto plano; solo su hash SHA-256 es devuelto.

    **Funcionamiento:**  
      - Utiliza `getpass` para obtener la entrada de manera segura sin mostrar caracteres en pantalla.
      - Codifica la contraseña ingresada y calcula su hash utilizando el algoritmo SHA-256.
    """
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    return hashlib.sha256(contraseña.encode()).hexdigest()

def escribir_fragmentos(archivo_salida, fragmentos, ruta_carpeta):
    """
    Escribe fragmentos de datos en un archivo de salida en formato CSV.

    **Parámetros:**  
      - `archivo_salida` (str): Nombre del archivo donde se guardarán los fragmentos.
      - `fragmentos` (list of tuples): Lista de tuplas con los fragmentos a escribir. Cada tupla debe contener dos valores enteros (x, y).
      - `ruta_carpeta` (str): Ruta de la carpeta donde se guardará el archivo.

    **Resultados:**  
      - No retorna nada. Los fragmentos se escriben en el archivo especificado.

    **Precondiciones:**  
      - `fragmentos` debe ser una lista no vacía de tuplas `(x, y)` con valores enteros.
      - `archivo_salida` debe ser una ruta válida donde se pueda escribir.

    **Postcondiciones:**  
      - Se genera un archivo de texto que contiene los fragmentos, con cada fragmento en una línea separada por comas.

    **Funcionamiento:**  
      - Itera sobre la lista de fragmentos y los escribe en el archivo en formato `x,y`.
    """
    ruta_fragmentos = os.path.join(ruta_carpeta, archivo_salida)
    with open(ruta_fragmentos, 'w') as f:
        for x, y in fragmentos:
            f.write(f"{x},{y}\n")

def leer_fragmentos(archivo_entrada, ruta_carpeta):
    """
    Lee fragmentos de datos desde un archivo en formato CSV y los retorna como una lista de tuplas.

    **Parámetros:**  
      - `archivo_entrada` (str): Nombre del archivo que contiene los fragmentos en formato `x,y`.
      - `ruta_carpeta` (str): Ruta de la carpeta donde se encuentra el archivo.

    **Resultados:**  
      - Devuelve una lista de tuplas `(x, y)` con los valores enteros de cada fragmento.

    **Precondiciones:**  
      - El archivo debe existir y contener líneas en formato `x,y` con valores enteros.

    **Postcondiciones:**  
      - Retorna una lista de tuplas de tamaño igual al número de líneas válidas en el archivo.

    **Funcionamiento:**  
      - Abre el archivo, lee cada línea, divide los valores por la coma y los convierte en enteros antes de almacenarlos como tuplas.
    """
    fragmentos = []
    ruta_fragmentos = os.path.join(ruta_carpeta, archivo_entrada)
    with open(ruta_fragmentos, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split(','))
            fragmentos.append((x, y))
    return fragmentos

def validar_argumentos(n, t):
    """
    Valida los argumentos `n` y `t` para asegurar que cumplen las restricciones necesarias.

    **Parámetros:**  
      - `n` (int): Número total de fragmentos.
      - `t` (int): Número mínimo de fragmentos necesarios para reconstruir el secreto.

    **Resultados:**  
      - No retorna nada si los valores son válidos.
      - Lanza un `ValueError` si los valores no cumplen con las restricciones.

    **Precondiciones:**  
      - `n` y `t` deben ser enteros positivos.

    **Postcondiciones:**  
      - Lanza una excepción si `t > n` o `n <= 2`.

    **Funcionamiento:**  
      - Comprueba las condiciones `1 < t <= n` y `n > 2`. Si no se cumplen, lanza un error.
    """
    if t > n or n <= 2:
        raise ValueError("Debe cumplir: 1 < t <= n y n > 2.")
