import pytest
import hashlib
import tempfile
from unittest.mock import patch
from auxiliares import obtener_contraseña, escribir_fragmentos, leer_fragmentos, validar_argumentos

def test_obtener_contraseña():
    """
    Prueba que `obtener_contraseña` genere el hash correcto para una contraseña dada.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        La función genera un hash usando SHA-256 de la contraseña proporcionada a través de la función `getpass.getpass()`.
        El hash generado se compara con el hash esperado, basado en la contraseña de prueba.

    Precondiciones:
        La función `obtener_contraseña` debe estar implementada correctamente y debe generar un hash con SHA-256.

    Postcondiciones:
        Se verifica que el hash generado coincida con el valor esperado.
    """
    contraseña_prueba = "mi_contraseña_segura"
    hash_esperado = hashlib.sha256(contraseña_prueba.encode()).hexdigest()

    with patch("getpass.getpass", return_value=contraseña_prueba):
        hash_generado = obtener_contraseña()

    assert hash_generado == hash_esperado, "El hash generado no coincide con el esperado."

def test_escribir_y_leer_fragmentos():
    """
    Prueba que los fragmentos se escriban correctamente en un archivo y se puedan leer correctamente.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        Los fragmentos se escriben en un archivo temporal y luego se leen de ese archivo.
        Se compara el contenido leído con el contenido original.

    Precondiciones:
        Las funciones `escribir_fragmentos` y `leer_fragmentos` deben estar implementadas correctamente.
        La función `escribir_fragmentos` debe escribir los fragmentos en el archivo y `leer_fragmentos` debe devolver los fragmentos correctos.

    Postcondiciones:
        Se asegura que los fragmentos escritos y leídos coincidan.
    """
    fragmentos = [(1, 42), (2, 84), (3, 126)]

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        archivo_salida = temp_file.name
        escribir_fragmentos(archivo_salida, fragmentos)

        fragmentos_leidos = leer_fragmentos(archivo_salida)

    assert fragmentos == fragmentos_leidos, "Los fragmentos leídos no coinciden con los escritos."

def test_leer_fragmentos_archivo_invalido():
    """
    Prueba que `leer_fragmentos` lance un error al intentar leer un archivo con formato incorrecto.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        Se verifica que al leer un archivo con contenido mal formado, se lance una excepción `ValueError`.

    Precondiciones:
        La función `leer_fragmentos` debe estar implementada para detectar archivos con formato incorrecto y generar una excepción.

    Postcondiciones:
        Se asegura que la función lance una excepción `ValueError` cuando se intente leer un archivo con formato incorrecto.

    Excepciones:
        Lanza un `ValueError` si el contenido del archivo no cumple con el formato esperado.
    """
    contenido_invalido = "1,42\n2\n3,126" 

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(contenido_invalido)
        temp_file.seek(0)
        archivo_invalido = temp_file.name

    with pytest.raises(ValueError):
        leer_fragmentos(archivo_invalido)

def test_validar_argumentos_validos():
    """
    Prueba que `validar_argumentos` no lance una excepción para valores válidos.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        Verifica que la función `validar_argumentos` no lance una excepción cuando los valores proporcionados son válidos.

    Precondiciones:
        Los valores proporcionados (5 y 3) deben ser considerados válidos según la implementación de la función `validar_argumentos`.

    Postcondiciones:
        No se lanza ninguna excepción.
    """
    try:
        validar_argumentos(5, 3)
    except ValueError:
        pytest.fail("validar_argumentos lanzó una excepción con valores válidos.")

def test_validar_argumentos_invalidos():
    """
    Prueba que `validar_argumentos` lance un `ValueError` para valores inválidos.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        Se verifica que la función `validar_argumentos` lance una excepción `ValueError` cuando se proporcionan valores inválidos.

    Precondiciones:
        La función `validar_argumentos` debe estar implementada para identificar los valores inválidos.

    Postcondiciones:
        Se asegura que se lance una excepción `ValueError` cuando los argumentos no sean válidos.

    Excepciones:
        Lanza un `ValueError` si los valores no cumplen con los requisitos establecidos.
    """
    with pytest.raises(ValueError):
        validar_argumentos(3, 5)  

    with pytest.raises(ValueError):
        validar_argumentos(2, 2) 
