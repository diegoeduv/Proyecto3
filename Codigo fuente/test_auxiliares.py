import pytest
import hashlib
import tempfile
from unittest.mock import patch
from auxiliares import obtener_contraseña, escribir_fragmentos, leer_fragmentos, validar_argumentos

def test_obtener_contraseña():
    """
    Prueba que `obtener_contraseña` genere el hash correcto para una contraseña dada.
    """
    contraseña_prueba = "mi_contraseña_segura"
    hash_esperado = hashlib.sha256(contraseña_prueba.encode()).hexdigest()

    with patch("getpass.getpass", return_value=contraseña_prueba):
        hash_generado = obtener_contraseña()

    assert hash_generado == hash_esperado, "El hash generado no coincide con el esperado."

def test_escribir_y_leer_fragmentos():
    """
    Prueba que los fragmentos se escriban correctamente en un archivo y se puedan leer correctamente.
    """
    fragmentos = [(1, 42), (2, 84), (3, 126)]

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        archivo_salida = temp_file.name
        escribir_fragmentos(archivo_salida, fragmentos)

        fragmentos_leidos = leer_fragmentos(archivo_salida)

    assert fragmentos == fragmentos_leidos, "Los fragmentos leídos no coinciden con los escritos."

def test_leer_fragmentos_archivo_invalido():
    """
    Prueba que leer_fragmentos lance un error al intentar leer un archivo con formato incorrecto.
    """
    contenido_invalido = "1,42\n2\n3,126"  # Línea 2 tiene formato incorrecto

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(contenido_invalido)
        temp_file.seek(0)
        archivo_invalido = temp_file.name

    with pytest.raises(ValueError):
        leer_fragmentos(archivo_invalido)
