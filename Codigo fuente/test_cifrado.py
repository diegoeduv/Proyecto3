import pytest
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from cifrado_AES import encriptar_archivo, desencriptar_archivo

@pytest.fixture
def archivo_temporal():
    """
    Crea un archivo temporal con contenido de prueba y lo elimina después de la prueba.
    """
    nombre_archivo = "prueba.txt"
    contenido = b"Este es un texto de prueba para cifrar y descifrar."

    with open(nombre_archivo, "wb") as f:
        f.write(contenido)

    yield nombre_archivo

    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)

    archivo_cifrado = os.path.splitext(nombre_archivo)[0] + ".aes"
    archivo_descifrado = os.path.splitext(nombre_archivo)[0] + ".txt"

    if os.path.exists(archivo_cifrado):
        os.remove(archivo_cifrado)
    if os.path.exists(archivo_descifrado):
        os.remove(archivo_descifrado)

@pytest.fixture
def clave_aes():
    """
    Genera una clave válida de 16 bytes para las pruebas.
    """
    return get_random_bytes(16)

def test_encriptar_archivo(archivo_temporal, clave_aes):
    """
    Verifica que `encriptar_archivo` cree un archivo cifrado y que tenga contenido.
    """
    archivo_cifrado = encriptar_archivo(archivo_temporal, clave_aes)

    # Verificar que el archivo cifrado se haya creado
    assert os.path.exists(archivo_cifrado), "El archivo cifrado no se generó."
    assert os.path.getsize(archivo_cifrado) > 16, "El archivo cifrado tiene un tamaño inesperado (demasiado pequeño)."