import unittest
import os
from cifrado_AES import encriptar_archivo, desencriptar_archivo
from shamir import generar_fragmentos, reconstruir_secreto
from auxiliares import escribir_fragmentos, leer_fragmentos, obtener_contraseña

class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        """ Configuración previa: crear archivos de prueba """
        self.plain_text_file = "test_plain.txt"
        self.encrypted_file = "test_encrypted.txt"
        self.fragments_file = "test_fragments.frg"
        self.decrypted_file = "test_decrypted.txt"
        with open(self.plain_text_file, "w") as f:
            f.write("Este es un archivo de prueba para cifrado y descifrado.")

    def tearDown(self):
        """ Limpieza: eliminar los archivos generados durante las pruebas """
        for file in [self.plain_text_file, self.encrypted_file, self.fragments_file, self.decrypted_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_cifrado_y_descifrado(self):
        """ Verificar que el archivo se cifra y descifra correctamente """
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
