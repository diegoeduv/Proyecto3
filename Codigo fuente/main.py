import sys
import os
from cifrado_AES import encriptar_archivo, desencriptar_archivo
from shamir import generar_fragmentos, reconstruir_secreto
from auxiliares import escribir_fragmentos, obtener_contraseña, validar_argumentos, leer_fragmentos

def main():
    """
    Punto de entrada principal del programa. Gestiona el flujo para cifrar o descifrar archivos
    en función de los argumentos proporcionados.

    **Uso:**
      - Para cifrar: `main.py c <documento.frg> <n> <t> <archivo_claro>`
      - Para descifrar: `main.py d <documento.frg> <archivo_cifrado>`

    **Parámetros (sys.argv):**
      - sys.argv[1]: Modo de operación ('c' para cifrar o 'd' para descifrar).
      - sys.argv[2]: Nombre del archivo de salida (fragmentos o archivo descifrado).
      - sys.argv[3]: (Para cifrado) Número de fragmentos 'n'.
      - sys.argv[4]: (Para cifrado) Umbral 't' necesario para reconstruir la clave.
      - sys.argv[5]: (Para cifrado) Nombre del archivo a cifrar.

    **Precondiciones:**
      - Los archivos especificados deben existir.
      - Se deben proporcionar los argumentos necesarios según el modo de operación.
      - Para cifrar: `n >= t`.

    **Postcondiciones:**
      - En modo 'c': Se genera un archivo cifrado, los fragmentos y el archivo original se elimina.
      - En modo 'd': Se reconstruye el archivo descifrado.

    **Resultados:**
      - Salidas en consola indicando los pasos realizados (clave generada, fragmentos, archivos generados).
      - Archivos creados según el modo de operación.
    """
    if len(sys.argv) < 2:
        print("Uso: main.py [c|d] <otros argumentos>")
        sys.exit(1)

    modo = sys.argv[1]
    directorio = os.path.dirname(__file__)
    ruta_carpeta = os.path.abspath(os.path.join(directorio, "..", "Archivos"))
    if modo == "c": 
        if len(sys.argv) != 6:
            print("Uso: main.py c <documento.frg> <n> <t> <archivo_claro>")
            sys.exit(1)

        archivo_salida = sys.argv[2]
        n = int(sys.argv[3])
        t = int(sys.argv[4])
        archivo_entrada = sys.argv[5]

        validar_argumentos(n, t)

        contraseña = obtener_contraseña()
        clave, fragmentos = generar_fragmentos(contraseña, n, t)
        
        archivo_encriptado = encriptar_archivo(archivo_entrada, clave, ruta_carpeta)

        escribir_fragmentos(archivo_salida, fragmentos, ruta_carpeta)
        print(f"Archivo cifrado generado: {archivo_encriptado}")
        print(f"Archivo de evaluaciones generado: {archivo_salida}")

        ruta_completa = os.path.join(ruta_carpeta, archivo_entrada)
        os.remove(ruta_completa)
        print(f"Archivo original eliminado: {archivo_entrada}")
    
    elif modo == "d": 
        if len(sys.argv) != 4:
            print("Uso: main.py d <documento.frg> <archivo_cifrado>")
            sys.exit(1)
        archivo_fragmentos = sys.argv[2]
        archivo_cifrado = sys.argv[3]

        fragmentos = leer_fragmentos(archivo_fragmentos, ruta_carpeta)

        clave_reconstruida = reconstruir_secreto(fragmentos)

        archivo_descifrado = desencriptar_archivo(archivo_cifrado, clave_reconstruida, ruta_carpeta)
        print(f"Archivo descifrado generado: {archivo_descifrado}")

    else: 
        print("Modo desconocido. Use 'c' para cifrar o 'd' para descifrar.")
        sys.exit(1)

if __name__ == "__main__":
    main()
