from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import os

def encriptar_archivo(entrada_archivo, clave):
    """
    Cifra un archivo utilizando el algoritmo AES en modo CBC.

    **Parámetros:**
      - `entrada_archivo` (str): Ruta al archivo de entrada que será cifrado.
      - `clave` (bytes): Clave de 16, 24 o 32 bytes utilizada para el cifrado.

    **Resultados:**
      - Retorna la ruta del archivo cifrado generado, con extensión `.aes`.

    **Precondiciones:**
      - El archivo especificado por `entrada_archivo` debe existir.
      - La clave debe ser del tamaño adecuado para AES (16, 24 o 32 bytes).

    **Postcondiciones:**
      - Se genera un nuevo archivo cifrado con la misma ruta base que el archivo original pero con extensión `.aes`.

    **Funcionamiento:**
      - Lee el contenido del archivo de entrada.
      - Cifra el contenido utilizando el algoritmo AES con un IV (vector de inicialización) generado automáticamente.
      - Escribe el IV seguido del contenido cifrado en el archivo de salida.
    """
    cifrado = AES.new(clave, AES.MODE_CBC)
    iv = cifrado.iv

    with open(entrada_archivo, 'rb') as f:
        texto = f.read()

    texto_cifrado = cifrado.encrypt(pad(texto, AES.block_size))
    salida_archivo = os.path.splitext(entrada_archivo)[0] + '.aes'

    with open(salida_archivo, 'wb') as f:
        f.write(iv + texto_cifrado)

    return salida_archivo

def desencriptar_archivo(entrada_archivo, clave):
    """
    Descifra un archivo previamente cifrado utilizando el algoritmo AES en modo CBC.

    **Parámetros:**
      - `entrada_archivo` (str): Ruta al archivo cifrado con extensión `.aes`.
      - `clave` (bytes): Clave de 16, 24 o 32 bytes utilizada para el descifrado.

    **Resultados:**
      - Retorna la ruta del archivo descifrado generado, con extensión `.txt`.

    **Precondiciones:**
      - El archivo especificado por `entrada_archivo` debe existir y ser válido.
      - La clave debe ser la misma utilizada durante el cifrado y tener el tamaño adecuado (16, 24 o 32 bytes).

    **Postcondiciones:**
      - Se genera un nuevo archivo descifrado con la misma ruta base que el archivo cifrado pero con extensión `.txt`.

    **Funcionamiento:**
      - Lee el IV (vector de inicialización) y el contenido cifrado del archivo.
      - Descifra el contenido utilizando AES en modo CBC.
      - Elimina el relleno (padding) del contenido descifrado.
      - Escribe el contenido descifrado en un nuevo archivo.
    """
    with open(entrada_archivo, 'rb') as f:
        iv = f.read(16)
        texto_cifrado = f.read()

    cifrado = AES.new(clave, AES.MODE_CBC, iv)
    texto = unpad(cifrado.decrypt(texto_cifrado), AES.block_size)

    salida_archivo = os.path.splitext(entrada_archivo)[0] + ".txt"

    with open(salida_archivo, 'wb') as f:
        f.write(texto)

    return salida_archivo
