import unittest
import os
from cifrado_AES import encriptar_archivo, desencriptar_archivo
from shamir import generar_fragmentos, reconstruir_secreto
from auxiliares import escribir_fragmentos, leer_fragmentos, obtener_contraseña

class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        """
        Configuración previa para las pruebas. Crea un archivo de texto plano con contenido de prueba.

        Precondiciones:
            Se debe crear un archivo de texto llamado 'test_plain.txt' con un texto específico 
            que se utilizará para las pruebas de cifrado y descifrado.

        Postcondiciones:
            El archivo 'test_plain.txt' se crea en el sistema de archivos.
        """
        self.plain_text_file = "test_plain.txt"
        self.encrypted_file = "test_encrypted.txt"
        self.fragments_file = "test_fragments.frg"
        self.decrypted_file = "test_decrypted.txt"
        with open(self.plain_text_file, "w") as f:
            f.write("Este es un archivo de prueba para cifrado y descifrado.")

    def tearDown(self):
        """
        Limpieza posterior a las pruebas. Elimina los archivos generados durante las pruebas.

        Precondiciones:
            Después de ejecutar las pruebas, los archivos generados deben eliminarse para evitar
            la acumulación de archivos innecesarios en el sistema.

        Postcondiciones:
            Los archivos generados ('test_plain.txt', 'test_encrypted.txt', 'test_fragments.frg', 
            'test_decrypted.txt') se eliminan del sistema de archivos si existen.
        """
        for file in [self.plain_text_file, self.encrypted_file, self.fragments_file, self.decrypted_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_cifrado_y_descifrado(self):
        """
        Verifica que el archivo se cifra y descifra correctamente, utilizando Shamir para generar fragmentos
        de la contraseña, y asegura que el contenido del archivo descifrado coincida con el original.

        Parámetros:
            No recibe parámetros directamente.

        Resultados:
            El archivo se cifra y descifra correctamente utilizando la clave generada a partir de los fragmentos.
            Además, el contenido del archivo descifrado debe coincidir con el archivo original.

        Precondiciones:
            Se debe generar una clave válida a partir de fragmentos utilizando la contraseña proporcionada.
            El archivo de texto plano debe estar disponible para cifrado.

        Postcondiciones:
            Se genera un archivo cifrado, un archivo de fragmentos y un archivo descifrado.
            El contenido del archivo descifrado debe ser el mismo que el del archivo original.

        Excepciones:
            No se esperan excepciones, pero si el archivo cifrado o descifrado no se genera correctamente, 
            la prueba fallará.
        """
        n, t = 5, 3
        contraseña = "contraseña_prueba"
        clave, fragmentos = generar_fragmentos(contraseña, n, t)

        archivo_encriptado = encriptar_archivo(self.plain_text_file, clave)
        self.assertTrue(os.path.exists(archivo_encriptado), "El archivo cifrado no se generó correctamente")

        escribir_fragmentos(self.fragments_file, fragmentos)
        self.assertTrue(os.path.exists(self.fragments_file), "El archivo de fragmentos no se generó correctamente")

        fragmentos_leidos = leer_fragmentos(self.fragments_file)
        clave_reconstruida = reconstruir_secreto(fragmentos_leidos)

        archivo_descifrado = desencriptar_archivo(archivo_encriptado, clave_reconstruida)
        self.assertTrue(os.path.exists(archivo_descifrado), "El archivo descifrado no se generó correctamente")

        with open(archivo_descifrado, "r") as f:
            contenido = f.read()
        self.assertEqual(contenido, "Este es un archivo de prueba para cifrado y descifrado.")
if __name__ == "__main__":
    unittest.main()
