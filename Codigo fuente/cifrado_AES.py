from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import os

def encriptar_archivo(entrada_archivo, clave):
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
    pass
