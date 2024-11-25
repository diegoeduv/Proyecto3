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