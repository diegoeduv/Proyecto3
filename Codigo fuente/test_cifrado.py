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

    assert os.path.exists(archivo_cifrado), "El archivo cifrado no se generó."
    assert os.path.getsize(archivo_cifrado) > 16, "El archivo cifrado tiene un tamaño inesperado (demasiado pequeño)."

def test_desencriptar_archivo(archivo_temporal, clave_aes):
    """
    Verifica que `desencriptar_archivo` recupere el contenido original correctamente.
    """
    archivo_cifrado = encriptar_archivo(archivo_temporal, clave_aes)
    archivo_descifrado = desencriptar_archivo(archivo_cifrado, clave_aes)

    # Verificar que el archivo descifrado tenga el mismo contenido que el original
    with open(archivo_temporal, "rb") as original, open(archivo_descifrado, "rb") as descifrado:
        assert original.read() == descifrado.read(), "El contenido descifrado no coincide con el original."

def test_desencriptar_archivo_con_clave_incorrecta(archivo_temporal, clave_aes):
    """
    Verifica que `desencriptar_archivo` falle si se usa una clave incorrecta.
    """
    archivo_cifrado = encriptar_archivo(archivo_temporal, clave_aes)
    clave_incorrecta = get_random_bytes(16)

    with pytest.raises(ValueError, match="Padding is incorrect."):
        desencriptar_archivo(archivo_cifrado, clave_incorrecta)

def test_encriptar_archivo_con_clave_invalida(archivo_temporal):
    """
    Verifica que `encriptar_archivo` falle si la clave no es de un tamaño válido.
    """
    clave_invalida = b"clave_corta"  # Clave menor a 16 bytes

    with pytest.raises(ValueError):
        encriptar_archivo(archivo_temporal, clave_invalida)

def test_desencriptar_archivo_con_formato_invalido(archivo_temporal, clave_aes):
    """
    Verifica que `desencriptar_archivo` falle si el archivo cifrado no tiene el formato esperado.
    """
    archivo_cifrado = "archivo_invalido.aes"

    with open(archivo_cifrado, "wb") as f:
        f.write(b"contenido_invalido")

    with pytest.raises(ValueError):
        desencriptar_archivo(archivo_cifrado, clave_aes)

    os.remove(archivo_cifrado)