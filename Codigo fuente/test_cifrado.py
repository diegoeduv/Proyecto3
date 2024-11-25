import pytest
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from cifrado_AES import encriptar_archivo, desencriptar_archivo

@pytest.fixture
def archivo_temporal():
    """
    Crea un archivo temporal con contenido de prueba y lo elimina después de la prueba.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        Crea un archivo llamado `prueba.txt` con contenido predefinido que simula datos a cifrar.

    Precondiciones:
        El archivo `prueba.txt` debe poder crearse en el sistema de archivos y contener texto binario adecuado.

    Postcondiciones:
        El archivo `prueba.txt` se elimina después de la ejecución de la prueba, junto con sus versiones cifradas o descifradas.
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

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        Genera una clave aleatoria de 16 bytes utilizando `get_random_bytes`, que es válida para el cifrado y descifrado AES.

    Precondiciones:
        El generador de números aleatorios de Cryptodome debe estar disponible.

    Postcondiciones:
        Devuelve una clave válida de 16 bytes que se utilizará en las pruebas de cifrado y descifrado.
    """
    return get_random_bytes(16)

def test_encriptar_archivo(archivo_temporal, clave_aes):
    """
    Verifica que `encriptar_archivo` cree un archivo cifrado y que tenga contenido.

    Parámetros:
        archivo_temporal: El archivo de prueba a cifrar.
        clave_aes: La clave de 16 bytes que se utilizará para cifrar el archivo.

    Resultados:
        La función `encriptar_archivo` debe crear un archivo con el contenido cifrado.
        El tamaño del archivo cifrado debe ser mayor a 16 bytes.

    Precondiciones:
        El archivo debe existir y la clave debe ser válida.

    Postcondiciones:
        Se asegura que el archivo cifrado se crea y tiene un tamaño adecuado.

    Excepciones:
        Ninguna.
    """
    archivo_cifrado = encriptar_archivo(archivo_temporal, clave_aes)

    assert os.path.exists(archivo_cifrado), "El archivo cifrado no se generó."
    assert os.path.getsize(archivo_cifrado) > 16, "El archivo cifrado tiene un tamaño inesperado (demasiado pequeño)."

def test_desencriptar_archivo(archivo_temporal, clave_aes):
    """
    Verifica que `desencriptar_archivo` recupere el contenido original correctamente.

    Parámetros:
        archivo_temporal: El archivo de prueba original.
        clave_aes: La clave de 16 bytes que se utilizará para cifrar y descifrar el archivo.

    Resultados:
        La función `desencriptar_archivo` debe recuperar el contenido original del archivo cifrado.

    Precondiciones:
        El archivo debe estar cifrado previamente y la clave debe ser válida.

    Postcondiciones:
        Se asegura que el contenido descifrado coincida con el original.
    """
    archivo_cifrado = encriptar_archivo(archivo_temporal, clave_aes)
    archivo_descifrado = desencriptar_archivo(archivo_cifrado, clave_aes)

    with open(archivo_temporal, "rb") as original, open(archivo_descifrado, "rb") as descifrado:
        assert original.read() == descifrado.read(), "El contenido descifrado no coincide con el original."

def test_desencriptar_archivo_con_clave_incorrecta(archivo_temporal, clave_aes):
    """
    Verifica que `desencriptar_archivo` falle si se usa una clave incorrecta.

    Parámetros:
        archivo_temporal: El archivo de prueba original.
        clave_aes: La clave de 16 bytes utilizada para cifrar.

    Resultados:
        La función `desencriptar_archivo` debe lanzar una excepción `ValueError` si se intenta usar una clave incorrecta.

    Precondiciones:
        El archivo debe estar cifrado previamente.

    Postcondiciones:
        Se lanza una excepción `ValueError` al intentar descifrar el archivo con una clave incorrecta.

    Excepciones:
        Lanza una excepción `ValueError` con el mensaje "Padding is incorrect." cuando la clave es incorrecta.
    """
    archivo_cifrado = encriptar_archivo(archivo_temporal, clave_aes)
    clave_incorrecta = get_random_bytes(16)

    with pytest.raises(ValueError, match="Padding is incorrect."):
        desencriptar_archivo(archivo_cifrado, clave_incorrecta)

def test_encriptar_archivo_con_clave_invalida(archivo_temporal):
    """
    Verifica que `encriptar_archivo` falle si la clave no es de un tamaño válido.

    Parámetros:
        archivo_temporal: El archivo de prueba a cifrar.

    Resultados:
        La función `encriptar_archivo` debe lanzar una excepción `ValueError` si la clave no tiene un tamaño válido (debe ser de 16 bytes).

    Precondiciones:
        La clave proporcionada debe ser inválida (menor a 16 bytes).

    Postcondiciones:
        Se lanza una excepción `ValueError` al intentar cifrar el archivo con una clave inválida.

    Excepciones:
        Lanza una excepción `ValueError` si la clave no es de tamaño 16 bytes.
    """
    clave_invalida = b"clave_corta"  # Clave menor a 16 bytes

    with pytest.raises(ValueError):
        encriptar_archivo(archivo_temporal, clave_invalida)

def test_desencriptar_archivo_con_formato_invalido(archivo_temporal, clave_aes):
    """
    Verifica que `desencriptar_archivo` falle si el archivo cifrado no tiene el formato esperado.

    Parámetros:
        archivo_temporal: El archivo de prueba original.
        clave_aes: La clave de 16 bytes utilizada para cifrar.

    Resultados:
        Si el archivo cifrado no tiene el formato esperado, `desencriptar_archivo` debe lanzar una excepción `ValueError`.

    Precondiciones:
        Se crea un archivo de prueba con contenido inválido.

    Postcondiciones:
        Se lanza una excepción `ValueError` cuando se intenta desencriptar un archivo con formato inválido.

    Excepciones:
        Lanza una excepción `ValueError` si el archivo cifrado no tiene el formato esperado.
    """
    archivo_cifrado = "archivo_invalido.aes"

    with open(archivo_cifrado, "wb") as f:
        f.write(b"contenido_invalido")

    with pytest.raises(ValueError):
        desencriptar_archivo(archivo_cifrado, clave_aes)

    os.remove(archivo_cifrado)